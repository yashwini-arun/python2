from order import calculate_total

def test_calculate_total_basic():
    items = [(100, 2), (50, 1)]  # 2 items
    # Subtotal = 100*2 + 50*1 = 250
    # Tax = 250 * 0.05 = 12.5
    # Total = 262.5
    assert calculate_total(items) == 262.5

def test_empty_order():
    assert calculate_total([]) == 0.0

def test_custom_tax_rate():
    items = [(200, 1)]
    # Subtotal = 200
    # Tax = 200 * 0.10 = 20
    assert calculate_total(items, tax_rate=0.10) == 220.0

def test_large_quantity():
    items = [(10, 100)]  # 100 items of ₹10 each
    # Subtotal = 1000
    # Tax = 50
    assert calculate_total(items) == 1050.0
