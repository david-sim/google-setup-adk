"""
Google ADK Agent - Main agent logic and entry point.

This is a basic agent setup following the Google ADK documentation at:
https://google.github.io/adk-docs/get-started/python/#installation
"""

from google.adk.agents import LlmAgent
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def get_current_time(city: str) -> dict:
    """Return the current local time for a city using `zoneinfo`.

    This uses a small built-in mapping from common city names to
    IANA timezone names. If the city isn't in the map, the
    function returns an error explaining how to add more entries.
    """
    if not city or not isinstance(city, str):
        return {"status": "error", "error": "Invalid city input", "city": city}

    name = city.strip()

    try:
        # First try: assume user provided an IANA timezone name directly
        try:
            tz = ZoneInfo(name)
            tz_name = name
        except Exception:
            # Second try: attempt to resolve from available timezones by matching
            # the final component (e.g. 'London' -> 'Europe/London') or underscore variants.
            tz_name = None
            try:
                from zoneinfo import available_timezones

                candidates = []
                lname = name.lower().replace(' ', '_')
                for z in available_timezones():
                    last = z.rsplit('/', 1)[-1].lower()
                    if last == lname or last.replace('_', '') == lname.replace('_', ''):
                        candidates.append(z)

                if len(candidates) == 1:
                    tz_name = candidates[0]
                elif len(candidates) > 1:
                    tz_name = candidates[0]

            except Exception:
                # If available_timezones isn't present or fails, we won't be able
                # to search; fall through to error below.
                tz_name = None

            if tz_name is None:
                raise ValueError(
                    "Could not resolve city to an IANA timezone. Provide a valid IANA timezone name like 'Europe/London' or a recognizable city/region."
                )

            tz = ZoneInfo(tz_name)

        now = datetime.now(tz)
        utc_now = datetime.now(timezone.utc)
        offset = now.utcoffset()

        return {
            "status": "success",
            "city": city,
            "timezone": tz_name,
            "local_datetime": now.isoformat(),
            "utc_datetime": utc_now.isoformat(),
            "utc_offset_seconds": int(offset.total_seconds()) if offset else 0,
        }

    except Exception as e:
        return {"status": "error", "error": str(e), "city": city}


# Define the root agent
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='root_agent',
    description="A helpful assistant that can provide information and answer questions.",
    instruction=(
        "You are a timezone assistant that is trained in using ZoneInfo and datetime. "
        "If the user provides a city name and asks for the current time, resolve the data to the input for ZoneInfo class."
        "You can tell the current time in cities. Use the 'get_current_time' tool for this purpose."
    ),
    tools=[get_current_time],
)

# Export a list named `agents` for ADK discovery (ADK looks for an `agents` iterable)
agents = [root_agent]
