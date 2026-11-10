"""Milestone 1 - Estimate one e-waste collection."""

# a) Input (input() always returns text)
participant = input("Participant name: ").strip().title()
device = input("Device category: ").strip().title()
quantity = input("Quantity: ")
unit_weight = input("Unit weight (kg): ")
recovery_pct = input("Recovery (%): ")
rate = input("Reward rate (Rs. per recyclable kg): ")

# b) Convert numeric inputs to suitable types
quantity = int(quantity)
unit_weight = float(unit_weight)
recovery_pct = float(recovery_pct)
rate = float(rate)

# c) Calculations
total_weight = quantity * unit_weight
recyclable_weight = total_weight * recovery_pct / 100
estimated_reward = recyclable_weight * rate

# d) 5-character collection code: 3 letters of name + 2 letters of device
collection_code = participant[:3].upper() + device[:2].upper()

print("\n===== SINGLE COLLECTION ESTIMATE =====")
print("Participant      :", participant)
print("Device category  :", device)
print("Type of quantity :", type(quantity))
print("Type of unit wt  :", type(unit_weight))
print(f"Total weight     : {total_weight:.2f} kg")
print(f"Recyclable weight: {recyclable_weight:.3f} kg")
print(f"Estimated reward : Rs. {estimated_reward:.2f}")
print("Collection code  :", collection_code)
