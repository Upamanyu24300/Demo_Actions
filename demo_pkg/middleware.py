"""Auth middleware for the demo orders API."""
from __future__ import annotations


def require_auth(token: str) -> bool:
    """Return True only for a present bearer token."""
    return bool(token) and token.startswith("Bearer ")
