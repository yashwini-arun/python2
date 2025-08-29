import sys, os

# Ensure current directory is in Python path
sys.path.append(os.path.dirname(__file__))

from loyalty import redeem_points

def test_redeem_valid():
    assert redeem_points(500, 50) == 450

def test_invalid_points_not_multiple_of_10():
    try:
        redeem_points(300, 25)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_negative_points():
    try:
        redeem_points(200, -20)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_redeem_more_than_total():
    assert redeem_points(500, 600) == 0

def test_zero_points():
    assert redeem_points(400, 0) == 400

if __name__ == "__main__":
    test_redeem_valid()
    test_invalid_points_not_multiple_of_10()
    test_negative_points()
    test_redeem_more_than_total()
    test_zero_points()
    print("All loyalty tests passed.")