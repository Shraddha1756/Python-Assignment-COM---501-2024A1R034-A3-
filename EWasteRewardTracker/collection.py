"""collection.py - EWasteCollection class (Milestones 3-5, uses recycling_utils)."""
import recycling_utils as utils


class EWasteCollection:
    centre_name = "Jammu Community Recycling Centre"  # shared by all objects

    def __init__(self, collection_id, participant_name, items=None):
        self.collection_id = collection_id.strip().upper()
        self.participant_name = participant_name.strip().title()
        self.items = []  # list of (category, quantity)
        if items:
            for category, quantity in items:
                self.add_item(category, quantity)

    def add_item(self, category, quantity):
        """Validate and store one device entry."""
        category = category.strip().title()
        utils.CATALOGUE[category]  # KeyError if unsupported
        quantity = int(quantity)  # ValueError if not a number
        if quantity <= 0:
            raise ValueError("quantity must be greater than zero")
        self.items.append((category, quantity))

    def total_weight(self):
        return utils.total_weight(self.items, utils.CATALOGUE)

    def base_reward(self):
        return utils.reward(self.items, utils.CATALOGUE, bonus_rate=0)

    def total_reward(self):
        return utils.reward(self.items, utils.CATALOGUE)

    def size_class(self):
        return utils.size_class(self.total_weight())

    def __len__(self):
        return sum(q for _, q in self.items)  # total number of devices

    def display_summary(self):
        print(f"\n===== COLLECTION {self.collection_id} =====")
        print("Centre       :", self.centre_name)
        print("Participant  :", self.participant_name)
        for category, quantity in self.items:
            print(f"  {category:<11} x {quantity}")
        print("Devices      :", len(self))
        print(f"Total weight : {self.total_weight():.2f} kg")
        print("Size class   :", self.size_class())
        print(f"Base reward  : Rs. {self.base_reward():.2f}")
        print(f"Final reward : Rs. {self.total_reward():.2f}")

    def to_record(self):
        """One '|' delimited line for recycling_records.txt (Milestone 5)."""
        item_text = ",".join(f"{c}:{q}" for c, q in self.items)
        bonus = "Yes" if self.total_weight() >= 5 else "No"
        return "|".join([self.collection_id, self.participant_name, item_text,
                         str(len(self)), f"{self.total_weight():.2f}",
                         self.size_class(), bonus, f"{self.total_reward():.2f}"])
