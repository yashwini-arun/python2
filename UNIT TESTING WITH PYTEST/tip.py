from decimal import Decimal, ROUND_HALF_UP

def suggest_tip(total, percent=10):
    
    if total < 0:
        raise ValueError("Total bill cannot be negative")
    if percent < 0:
        raise ValueError("Tip percent cannot be negative")

    tip = Decimal(str(total)) * Decimal(str(percent)) / Decimal("100")
    return float(tip.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
