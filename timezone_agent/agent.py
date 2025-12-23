"""
Shim to expose the top-level `timezone_agent` as a directory-based agent
so the ADK CLI (which looks for agent directories) can discover it.
"""
from agent import timezone_agent  # re-export the existing timezone_agent

# Backwards-compatible alias expected by the ADK loader.
# Expose `root_agent` so directory-based discovery works.
root_agent = timezone_agent
app = timezone_agent

__all__ = ["timezone_agent", "root_agent", "app"]
