import sys, os

# Ensure current directory is in Python path
sys.path.append(os.path.dirname(__file__))

from tip import suggest_tip

def test_tip_default():
    assert suggest_tip(1000) == 100.0

def test_tip_custom():
    assert suggest_tip(500, 15) == 75.0

def test_tip_zero_percent():
    assert suggest_tip(800, 0) == 0.0

def test_tip_rounding_half_up():
    assert suggest_tip(333, 12.5) == 41.63

def test_negative_total():
    try:
        suggest_tip(-100, 10)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_negative_percent():
    try:
        suggest_tip(500, -5)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_large_bill():
    assert suggest_tip(12345.67, 20) == 2469.13

if __name__ == "__main__":
    test_tip_default()
    test_tip_custom()
    test_tip_zero_percent()
    test_tip_rounding_half_up()
    test_negative_total()
    test_negative_percent()
    test_large_bill()
    print("All tip tests passed.")