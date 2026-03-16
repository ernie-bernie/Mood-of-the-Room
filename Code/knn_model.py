import math
# Mood of the Room – Prototype Model
# Implements weighted averaging, kNN classification,
# and distance-based confidence

# -------------------------------
# Stored labeled dataset
# -------------------------------

stored_points = [
    {"L": 65, "N": 53, "M": 22, "mood": "chaotic"},
    {"L": 30, "N": 10, "M": 2, "mood": "calm"},
    {"L": 31, "N": 11, "M": 3, "mood": "calm"},
    {"L": 74, "N": 39, "M": 13, "mood": "chaotic"},
    {"L": 80, "N": 40, "M": 8, "mood": "chaotic"},
    {"L": 29, "N": 7, "M": 2, "mood": "calm"},
    {"L": 45, "N": 24, "M": 9, "mood": "medium"},
    {"L": 50, "N": 28, "M": 10, "mood": "medium"},
    {"L": 42, "N": 22, "M": 8, "mood": "medium"}
]
# -------------------------------
# Example recent readings
# ------------------------------
recent_readings = [
    (24, 6, 4),
    (26, 7, 3),
    (23, 5, 5)
]




def weighted_average(readings):
    print("This is where I will first calculate the weighted average of the recent readings.")
  

weighted_average(recent_readings)