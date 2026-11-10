"""Milestone 2 - Process a mixed e-waste collection."""

# a) Catalogue: category -> (unit weight in kg, reward rate in Rs. per kg)
catalogue = {
    "Smartphone": (0.18, 40),
    "Laptop": (2.20, 55),
    "Charger": (0.12, 20),
    "Keyboard": (0.65, 15),
}

items = []  # c) valid selections as (category, quantity) pairs
unique_categories = set() # c) set of different categories entered

print("Supported categories:", ", ".join(catalogue))

# b) Keep asking until the user types DONE
while True:
    category = input("\nDevice category (or DONE): ").strip().title()
    if category == "Done":
        break

    # d) Reject unsupported categories and carry on
    if category not in catalogue:
        print("Rejected: unsupported category.")
        continue

    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Rejected: quantity must be a whole number.")
        continue

    # d) Reject quantity <= 0
    if quantity <= 0:
        print("Rejected: quantity must be greater than 0.")
        continue

    items.append((category, quantity))
    unique_categories.add(category)
    print(f"Accepted: {category} x {quantity}")

# e) Totals, bonus and classification
total_weight = 0.0
base_reward = 0.0
for category, quantity in items:
    unit_weight, rate = catalogue[category]
    total_weight += unit_weight * quantity
    base_reward += unit_weight * quantity * rate

bonus = 0.10 * base_reward if total_weight >= 5 else 0.0

if total_weight < 3:
    size = "SMALL"
elif total_weight <= 8:
    size = "MEDIUM"
else:
    size = "LARGE"

print("\n===== MIXED COLLECTION SUMMARY =====")
for category, quantity in items:
    print(f"  {category:<11} x {quantity}")
print("Unique categories:", ", ".join(sorted(unique_categories)) or "None")
print(f"Total weight     : {total_weight:.2f} kg")
print("Size class       :", size)
print(f"Base reward      : Rs. {base_reward:.2f}")
print(f"Bonus            : Rs. {bonus:.2f}")
print(f"Final reward     : Rs. {base_reward + bonus:.2f}")
