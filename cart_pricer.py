items = [("Notebook", 120),("Pen Set", 80),("Backpack", 950),("Sketchbook", 340),]

# Discount apply karne ke liye lambda (10% off)
apply_discount = lambda price: round(price * 0.90, 2)

# Har item ka discounted price nikaalna
discounted_items = [(name, apply_discount(price)) for name, price in items]

# Price kke hishaab se ascending order me short karna (key = lambda)
sorted_items = sorted(discounted_items, key=lambda pair: pair[1])

print("Discounted Item", discounted_items)
print("Sorted Item", sorted_items)