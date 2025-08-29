def redeem_points(total, points):
    
    if points < 0:
        raise ValueError("Points cannot be negative")
    if points % 10 != 0:
        raise ValueError("Points must be in multiples of 10")

    return max(total - points, 0)
