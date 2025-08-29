from restaurant import is_open

def test_open_hours():
    # 14:00 is between 10:00 and 22:00
    assert is_open("14:00", "10:00", "22:00")

def test_closed_hours():
    # 23:00 is after closing
    assert not is_open("23:00", "10:00", "22:00")

def test_open_midnight_shift():
    # Restaurant open from 22:00 to 06:00
    assert is_open("23:30", "22:00", "06:00")

def test_closed_midnight_shift():
    # Restaurant open 22:00 → 06:00, but 12:00 is outside
    assert not is_open("12:00", "22:00", "06:00")
