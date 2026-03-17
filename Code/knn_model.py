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



test_readings= [(24, 6, 4),
(26, 7, 3),
(23, 5, 5)
]

def weighted_average(readings):

    reading_one = readings[0]
    reading_two = readings[1]
    reading_three = readings[2]

    totalL = reading_one[0] * 0.2 + reading_two[0] * 0.3 + reading_three[0] * 0.5
    totalN = reading_one[1] * 0.2 + reading_two[1] * 0.3 + reading_three[1] * 0.5
    totalM = reading_one[2] * 0.2 + reading_two[2] * 0.3 + reading_three[2] * 0.5

    totalL = round(totalL, 3)
    totalN = round(totalN, 3)
    totalM = round(totalM, 3)

    return (totalL, totalN, totalM)

test_average = weighted_average(test_readings)

#Should return (24.1, 5.8, 4.2)
print(test_average)


test_point=(24,6,4)

def manhattan_distance(point, stored_point):

    L = abs(point[0] - stored_point["L"])
    N = abs(point[1] - stored_point["N"])
    M = abs(point[2] - stored_point["M"])

    distance = L + N + M

    return distance

#Should returen 12
print(manhattan_distance(test_point, stored_points[1]))


def compute_all_distances(point, stored_points):

    distances = []
    for stored_point in stored_points:
        distance = manhattan_distance(point, stored_point)
        distances.append((distance, stored_point["mood"]))

    return distances

#Should return [(106, 'chaotic'), (12, 'calm'), (13, 'calm'), (92, 'chaotic'), (94, 'chaotic'), (8, 'calm'), (44, 'medium'), (54, 'medium'), (38, 'medium')]
print(compute_all_distances(test_point, stored_points))

def get_k_neighbors(distances, k):

    sorted_distances = sorted(distances, key=lambda x: x[0])
    neighbors = sorted_distances[:k]
    return neighbors, sorted_distances

def predict_mood(point, stored_points, k):

    distances = compute_all_distances(point, stored_points)
    neighbors, sorted_distances = get_k_neighbors(distances, k)

    calm=0
    medium=0
    chaotic=0

    for neighbor in neighbors:
        if neighbor[1] == "calm":
            calm += 1
        elif neighbor[1] == "medium":
            medium += 1
        elif neighbor[1] == "chaotic":
            chaotic += 1

    if calm > medium and calm > chaotic:
        return "calm"
    elif medium > calm and medium > chaotic:
        return "medium"
    elif chaotic > calm and chaotic > medium:
        return "chaotic"
    else:
        return "tie"

#Should return "calm"
print(predict_mood(test_point, stored_points, 5))


def compute_confidence(point,stored_points, k):

    distances=compute_all_distances(point, stored_points)
    neighbors, sorted_distances = get_k_neighbors(distances, k)
    calm_distance=0
    medium_distance=0
    chaotic_distance=0
    calm_amount=0
    medium_amount=0
    chaotic_amount=0
    for x in neighbors:
        if x[1] == "calm":
            calm_distance += x[0]
            calm_amount += 1
        elif x[1] == "medium":
            medium_distance += x[0]
            medium_amount += 1
        elif x[1] == "chaotic":
            chaotic_distance += x[0]
            chaotic_amount += 1
    calm_distance = calm_distance / calm_amount if calm_amount > 0 else float('inf')
    medium_distance = medium_distance / medium_amount if medium_amount > 0 else float('inf')
    chaotic_distance = chaotic_distance / chaotic_amount if chaotic_amount > 0 else float('inf')
    if calm_amount and medium_amount > chaotic_amount:
        if calm_distance < medium_distance:
            gap = (medium_distance - calm_distance)
        else:
            gap = (calm_distance - medium_distance)
    elif medium_amount and chaotic_amount > calm_amount:
        if medium_distance < chaotic_distance:
            gap = (chaotic_distance - medium_distance)
        else:
            gap = (medium_distance - chaotic_distance)
    elif chaotic_amount and calm_amount > medium_amount:
        if chaotic_distance < calm_distance:
            gap = (calm_distance - chaotic_distance)
        else:
            gap = (chaotic_distance - calm_distance)
    else:
        gap = 0
    if gap>20:
        confidence="high"
    elif gap>10:
        confidence="medium"
    else:
        confidence="low"
    return confidence, gap

#Should return ("high",26.5)
print(compute_confidence((44,23,9), stored_points, 5))