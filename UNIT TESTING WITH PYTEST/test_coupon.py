from coupon import apply_coupon

def test_valid_percentage_coupon():
    assert apply_coupon(1000, "SAVE10") == 900

def test_valid_flat_coupon():
    assert apply_coupon(200, "FLAT50") == 150

def test_invalid_coupon():
    assert apply_coupon(500, "XYZ") == 500

def test_coupon_not_negative():
    # if coupon > total, it should not go negative
    assert apply_coupon(40, "FLAT50") == 0
