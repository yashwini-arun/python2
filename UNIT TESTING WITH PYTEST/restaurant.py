from datetime import datetime

def is_open(current_time, open_time, close_time):
   
    fmt = "%H:%M"
    current = datetime.strptime(current_time, fmt).time()
    opening = datetime.strptime(open_time, fmt).time()
    closing = datetime.strptime(close_time, fmt).time()

    if opening <= closing:
        # Normal case: 10:00 → 22:00
        return opening <= current <= closing
    else:
        # Crosses midnight: 22:00 → 06:00
        return current >= opening or current <= closing
