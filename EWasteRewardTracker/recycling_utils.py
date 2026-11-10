"""recycling_utils.py - reusable analytics for the E-Waste Reward Tracker (Milestone 4)."""
import math

# category -> (unit weight in kg, reward rate in Rs. per kg)
CATALOGUE = {
    "Smartphone": (0.18, 40),
    "Laptop": (2.20, 55),
    "Charger": (0.12, 20),
    "Keyboard": (0.65, 15),
}


def total_weight(items, catalogue):
    """Total weight in kg for a list of (category, quantity) pairs."""
    weight = 0.0
    for category, quantity in items:
        unit_weight, _ = catalogue[category]
        weight += unit_weight * quantity
    return weight


def reward(items, catalogue, bonus_rate=0.10, threshold_kg=5.0):
    """Base reward, plus a bonus when the collection reaches threshold_kg."""
    base = 0.0
    for category, quantity in items:
        unit_weight, rate = catalogue[category]
        base += unit_weight * quantity * rate
    if total_weight(items, catalogue) >= threshold_kg:
        return base * (1 + bonus_rate)
    return base


def bins_required(weight, capacity_kg=5.0):
    """Number of recycling bins needed, always rounded up."""
    return math.ceil(weight / capacity_kg)


def generate_metric(items, catalogue, metric_function):
    """Run any metric function that is passed in as an argument."""
    return metric_function(items, catalogue)


def size_class(weight):
    """SMALL (<3 kg), MEDIUM (3-8 kg) or LARGE (>8 kg)."""
    if weight < 3:
        return "SMALL"
    if weight <= 8:
        return "MEDIUM"
    return "LARGE"
