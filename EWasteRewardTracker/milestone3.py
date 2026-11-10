"""Milestone 3 - Two EWasteCollection objects."""
from collection import EWasteCollection

first = EWasteCollection("c101", "aarav", [
    ("Smartphone", 4), ("Laptop", 2), ("Charger", 3), ("Keyboard", 2),
])

second = EWasteCollection("c102", "meera")  # start empty, then add items
second.add_item("Smartphone", 5)
second.add_item("Charger", 4)

for collection in (first, second):
    collection.display_summary()
    print("len(collection) =", len(collection))
