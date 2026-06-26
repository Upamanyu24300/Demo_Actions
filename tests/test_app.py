from demo_pkg.app import handle_order


def test_authorized_order():
    assert handle_order("Bearer abc", 100) == "200 OK: charged 100"


def test_unauthorized_blocked():
    assert handle_order("", 100) == "401 Unauthorized"


def test_bad_amount():
    assert handle_order("Bearer abc", -5) == "400 Bad Request"
