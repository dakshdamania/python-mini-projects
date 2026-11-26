def generate_bill (customer="Guest", *price, discount=0, tax_rate=0.05, **extra_info):
      subtotal = sum(price)
      after_discount = max(0, subtotal - discount)
      final_total = round(after_discount * (1 + tax_rate), 2)

      print(f"Customer: {customer}")
      print(f"Item_count: {len(price)} | Subtotal: {subtotal}")
      print(f"Discount: {discount} | Tax: ({tax_rate * 100}%): {round(after_discount * tax_rate), 2}")
      print(f"Final Payable: {final_total}")

      if extra_info:
            print("Extra Info:", {k: v for k, v in extra_info.items()})

if __name__ == "__main__":
      generate_bill("Daksh", 250, 400, 150, discount=50, mode="UPI", note="Evening order")
