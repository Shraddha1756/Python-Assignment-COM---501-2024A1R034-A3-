"""main.py - Circular Economy E-Waste Collection and Recycling Reward Tracker.

Final program (Milestones 4 and 5).  Start it with:  python main.py
"""
from pathlib import Path

import recycling_utils as utils
from collection import EWasteCollection

RECORDS_FILE = Path(__file__).with_name("recycling_records.txt")


# ------------------------------------------------------------------
# Milestone 4 - test the utility module with one mixed collection
# ------------------------------------------------------------------
def utility_test():
    items = [("Smartphone", 4), ("Laptop", 2), ("Charger", 3), ("Keyboard", 2)]
    catalogue = utils.CATALOGUE

    weight = utils.generate_metric(items, catalogue, utils.total_weight)  # function as argument
    default_reward = utils.reward(items, catalogue)
    high_threshold = utils.reward(items, catalogue, threshold_kg=8.0)
    higher_bonus = utils.reward(items, catalogue, bonus_rate=0.20)
    small_bins = utils.bins_required(weight, capacity_kg=2.5)

    print("\n===== RECYCLING UTILITY TEST =====")
    print(f"generate_metric(total_weight)  : {weight:.2f} kg")
    print(f"reward() defaults (10%, 5 kg)  : Rs. {default_reward:.2f}")
    print(f"reward(threshold_kg=8.0)       : Rs. {high_threshold:.2f}")
    print(f"reward(bonus_rate=0.20)        : Rs. {higher_bonus:.2f}")
    print("bins_required() default 5 kg   :", utils.bins_required(weight))
    print("bins_required(capacity_kg=2.5) :", small_bins)


# ------------------------------------------------------------------
# Milestone 5 - file handling, exceptions and debugging
# ------------------------------------------------------------------
def show_history():
    """Read and display previously saved records."""
    try:
        with open(RECORDS_FILE, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("FileNotFoundError: recycling_records.txt does not exist yet.")
        return
    print("\n===== SAVED COLLECTION HISTORY =====")
    print("ID | Participant | Items | Devices | Weight kg | Size | Bonus | Reward Rs.")
    for line in lines:
        print(" | ".join(line.split("|")))
    print("Total saved collections:", len(lines))


def enter_collection():
    collection_id = input("Collection ID: ")
    participant = input("Participant name: ")
    collection = EWasteCollection(collection_id, participant)
    print("Categories:", ", ".join(utils.CATALOGUE))

    while True:
        category = input("Device category (or DONE): ").strip()
        if category.upper() == "DONE":
            break
        quantity = input("Quantity: ")
        try:
            collection.add_item(category, quantity)
            print("Item added.")
        except KeyError:  # unsupported device lookup
            print(f"KeyError: '{category}' is not in the catalogue.")
        except ValueError as error:  # bad quantity
            print(f"ValueError: invalid quantity '{quantity}' ({error}).")

    if len(collection) == 0:
        print("No valid items, so nothing was saved.")
        return
    collection.display_summary()
    with open(RECORDS_FILE, "a", encoding="utf-8") as file:  # append mode
        file.write(collection.to_record() + "\n")
    print("Summary appended to recycling_records.txt")


def debug_demo():
    """Shows the input() type problem and its correction."""
    print("\n===== DEBUGGING: input() RETURNS TEXT =====")
    quantity = input("Quantity: ")
    unit_weight = 0.18
    try:
        total_weight = quantity * unit_weight  # str * float -> error
    except TypeError as error:
        print("TypeError:", error)
    total_weight = int(quantity) * unit_weight  # corrected conversion
    print(f"Corrected: int({quantity!r}) * {unit_weight} = {total_weight:.2f} kg")


def main():
    print("===== CIRCULAR ECONOMY E-WASTE REWARD TRACKER =====")
    show_history()  # history at start-up
    while True:
        print("\n1. Add collection  2. View history  3. Utility test"
              "  4. Debug demo  5. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            enter_collection()
        elif choice == "2":
            show_history()
        elif choice == "3":
            utility_test()
        elif choice == "4":
            debug_demo()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Choose 1-5.")


if __name__ == "__main__":
    main()
