def calculate_total(prices, tax_rate):
    """Calculate the total price including tax."""
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    return round(subtotal + tax, 2)


def apply_discount(price, discount_percent):
    """Apply a percentage discount to a price."""
    discount = price * (discount_percent / 100)
    return round(price - discount, 2)


def split_bill(total, num_people):
    """Split a bill evenly among people."""
    return round(total / num_people, 2)
