def apply_coupon(total, code):
   
    if code == "SAVE10":
        return max(total * 0.9, 0)   # 10% off
    elif code == "FLAT50":
        return max(total - 50, 0)    # Flat ₹50 off
    return total  # invalid coupon → no discount
