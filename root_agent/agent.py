"""
Shim to expose the top-level `root_agent` as a directory-based agent
so the ADK CLI (which looks for agent directories) can discover it.
"""
from agent import root_agent  # re-export the existing root_agent

__all__ = ["root_agent"]
