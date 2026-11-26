def process_expenses(expenses, min_amount=100, discount_rate=0.10):
    # filter(): Sirf min_amount ya usse zyada wale expenses chhanto
    high_expenses = list(filter(lambda item: item[1] >= min_amount, expenses))

    # map(): Un high expenses par discount apply karke naya tuple (name, final_price) banao
    discounted_expenses = list(
        map(
            lambda item: (item[0], round(item[1] * (1 - discount_rate), 2)),
            high_expenses,
        )
    )

    return high_expenses, discounted_expenses


if __name__ == "__main__":
    raw_expenses = [
        ("Tea", 40),
        ("Notebook", 150),
        ("Pen", 25),
        ("Drawing Kit", 600),
        ("Snack", 120),
    ]

    high_list, final_list = process_expenses(raw_expenses, min_amount=100, discount_rate=0.10)

    print("High Expenses (>= 100):", high_list)
    print("After 10% Discount:", final_list)