def calculate_total(items, tax_rate=0.05):
    
    if not items:
        return 0.0

    subtotal = sum(price * qty for price, qty in items)
    tax = subtotal * tax_rate
    return round(subtotal + tax, 2)
