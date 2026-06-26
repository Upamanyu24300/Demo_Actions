"""Business logic for the demo orders API."""
from __future__ import annotations

from demo_pkg.middleware import require_auth


def handle_order(token: str, amount: int) -> str:
    """Charge an order only for authenticated, valid requests."""
    if not require_auth(token):
        return "401 Unauthorized"
    if amount <= 0:
        return "400 Bad Request"
    return f"200 OK: charged {amount}
