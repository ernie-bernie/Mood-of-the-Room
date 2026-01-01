# Alpha Tests and Experiments
## Experiment #1: 12/27/25
### This experiment has no code or hardware, it is just to show the procedure and run through the steps

### Goal:
Test if this program would infer the correct mood of the room, but with no hardware or code yet. 

### Setup:
Assume k = 3, with the sensors being light, motion, and noise sensors
  
Assume that the previously labeled data points are true, and that the labels were given by the same person so there are no subjective errors
  
Assume that all of the data points are listed after being normalized
  
No averaging yet

### Data Points
#### Previously Stored Data:
- (L,N,M) → Mood
- (65, 53, 22) → chaotic
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (74, 39, 13) → chaotic
- (80, 40, 8) → chaotic
- (29, 7, 2) → calm 
#### Current Reading:
- (24, 6, 4) → Use for tests for calm
- (40, 25, 6) → Use for tests of medium rooms
- (70, 43, 17) → Use for tests of chaotic rooms 

### Procedure:
- Find the Manhattan distances of the current readings to all of the previously stored data
- Take the k closest neighbors (in this case it is three closest), and take their labels to vote on the current point's label
- Test if just taking the nearest neighbor produces a stable result
- Test if using a point in the middle works (Not too chaotic, not too calm)
- Test if using 4 or 5 values of K would also work, with a calm, chaotic, and a data point directly in the middle

### Distances
#### Current Calm Reading:
- Distance to chaotic (65, 53, 22) → 41 + 47 + 18 = 106​
- Distance to calm (30, 10, 2) → 6 + 4 + 2 = 12
- Distance to calm (31, 11, 3) → 7 + 5 + 1 = 13
- Distance to chaotic (74, 39, 13) → 50 + 33 + 9 = 92
- Distance to chaotic (80, 40, 8) → 56 + 34 + 4 = 94
- Distance to calm (29, 7, 2) → 5 + 4 + 2 = 8
#### Current Medium Reading:
- Distance to chaotic (65, 53, 22) → 25 + 28 + 6 = 69
- Distance to calm (30, 10, 2) → 10 + 15 + 4 = 29
- Distance to calm (31, 11, 3) → 9 + 14 + 3 = 26
- Distance to chaotic (74, 39, 13) → 34 + 14 + 7 = 55
- Distance to chaotic (80, 40, 8) → 40 + 15 + 2 = 57
- Distance to calm (29, 7, 2) → 11 + 18 + 4 = 33
#### Current Chaotic Reading:
- Distance to chaotic (65, 53, 22) → 5 + 10 + 5 = 20
- Distance to calm (30, 10, 2) → 40 + 33 + 15 = 88
- Distance to calm (31, 11, 3) → 39 + 32 + 14 = 85
- Distance to chaotic (74, 39, 13) → 4 + 4 + 4 = 12
- Distance to chaotic (80, 40, 8) → 10 + 3 + 9 = 22
- Distance to calm (29, 7, 2) → 41 + 36 + 15 = 92

### Voting with Nearest Neighbor (NN) and Closest Three
#### Current Calm:
##### Nearest Neighbor (NN)
(29, 7, 2) → calm
Final classification: calm
##### Closest three voting (not in order):
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (29, 7, 2) → calm
  
Final classification: calm

#### Current Medium:
##### Nearest Neighbor (NN)
(31, 11, 3) → calm
Final classification: calm
##### Closest three voting (not in order):
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (29, 7, 2) → calm
  
Final classification: calm

#### Current Chaotic:
##### Nearest Neighbor (NN)
(74, 39, 13) → chaotic
Final classification: chaotic
##### Closest three voting (not in order):
- (74, 39, 13) → chaotic
- (80, 40, 8) → chaotic
- (65, 53, 22) → chaotic
  
Final classification: chaotic

### Voting with 4 and 5 neighbors
#### Current Calm:
Nearest 4:
- (29, 7, 2) → calm
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (74, 39, 13) → chaotic
  
Final classification: calm

Nearest 5:
- (29, 7, 2) → calm
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (74, 39, 13) → chaotic
- (80, 40, 8) → chaotic
  
Final classification: calm

#### Current Medium
Nearest 4:
- (31, 11, 3) → calm
- (30, 10, 2) → calm
- (29, 7, 2) → calm
- (74, 39, 13) → chaotic
  
Final classification: calm

Nearest 5:
- (31, 11, 3) → calm
- (30, 10, 2) → calm
- (29, 7, 2) → calm
- (74, 39, 13) → chaotic
- (80, 40, 8) → chaotic
  
Final classification: calm

#### Current Chaotic:
Nearest 4:
- (74, 39, 13) → chaotic
- (65, 53, 22) → chaotic
- (80, 40, 8) → chaotic
- (31, 11, 3) → calm
  
Final classification: chaotic

Nearest 5:
- (74, 39, 13) → chaotic
- (65, 53, 22) → chaotic
- (80, 40, 8) → chaotic
- (31, 11, 3) → calm
- (30, 10, 2) → calm
   
Final classification: chaotic

### Experiment Notes:
#### Tests using 3 votes and NN:
- For a calm test reading, the three nearest neighbors were all labeled calm, and majority voting produced a stable classification, just as using the NN did. The voting ignored the far-away chaotic points, and using the Manhattan distance did not cause disproportionate influence from any single sensor
- For a medium test reading, all nearest neighbors were labeled calm, indicating that the model cannot output intermediate moods unless those labels exist in the data. This showed me a design gap in my reasoning. To overcome this, I may need to incorporate more labels or an uncertain response.
- For a chaotic test reading, the three nearest neighbors were all labeled chaotic, and majority voting produced a stable classification, just as using the NN did. The voting ignored the far-away calm points, and using the Manhattan distance did not cause disproportionate influence from any single sensor

#### Tests using 4 and 5 votes:
- For a calm test reading, increasing k from 3 to 4 and 5 did not change the classification for calm inputs, indicating strong cluster separation. This means that if I keep k as 3, it will be confident and fast, while using k as 4 or 5 means it will be more robust against bad points, such as if a human mislabels a point.
- For a medium test reading, increasing k from 3 to 4 and 5 did not change the classification, indicating that without medium-labeled data the model defaults to the closest existing class. This further supports that this is a dataset limitation.
- For a chaotic test reading, increasing k from 3 to 4 and 5 also did not change the classification, showing us that voting is consistently stable as k increases. This means that any value for k from 3-5 would work for this project.
  
What this means:
- My distance and voting logic works
- My dataset shape controls what outputs are possible, so a safeguard must be put into place so a forced, incorrect answer is not inferred.
- The clusters are well separated with these made-up data points

## Conclusion

This experiment showed that using Manhattan distance with k-nearest neighbors and majority voting produced stable classifications consistent with the labeled data for both chaotic and calm inputs while using the made-up datasets. Increasing k from 3 to 4 and 5 did not change the final classification in any of the tests, indicating that clusters in the dataset are well separated and that voting improves robustness. This also shows me that if one data point was mislabeled, having voting will limit the probability of the final answer being inaccurate.

This experiment also revealed an important limitation: when a "medium" input was tested, the system defaulted to the closest existing label (calm) because there was no dataset with a medium label. This demonstrates that the model cannot infer moods that were not already represented in the dataset.

Overall, this experiment validates the use of Manhattan distance-based voting as an approach that I can use while surfacing the need for better/more labels or an "uncertain" answer option. Based on these results, the next step is to evaluate how temporal averaging and weighted averaging affect classification stability and responsiveness.


---

## Experiment #2: 12/28/25
### This experiment has no code or hardware, it is just to compare averaging methods

### Goal:
Test how different types of averaging (no averaging, simple average, and weighted average) affect stability, during jitter and sudden changes, and responsiveness

### Setup:
Assume the sensors are light (L), motion (M), and noise sensors (N)
  
Assume that the previously labeled data points are true, and that the labels were given by the same person so there are no subjective errors
  
Assume that all of the data points are listed after being normalized
  
Assume that there are two mood labels: calm and chaotic

Assume that the classifier is k nearest neighbor voting using Manhattan distance (Start with k = 3, maybe do k = 5)

Assume that the data points in each "current reading" section are taking consecutively
### Data Points
#### Previously Stored Data:
(L,N,M) → Mood

- (65, 53, 22) → chaotic
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (74, 39, 13) → chaotic
- (80, 40, 8) → chaotic
- (29, 7, 2) → calm
  
#### Current Readings:
##### Calm With Slight Jitter:
- (24, 6, 4)
- (26, 7, 3)
- (23, 5, 5)
  
##### Calm → Chaotic (Lights turn off with no warning):
- (24, 6, 4) (calm)
- (26, 6, 4) (calm)
- (70, 43, 17) (chaotic)
  
##### Chaotic → Calm:
- (70, 43, 17) (chaotic)
- (70, 43, 17) (chaotic)
- (24, 6, 4) (calm)
  
### Procedure:
For each scenario (Slight jitter, calm → chaotic, chaotic → calm):
- No averaging: classify the third point directly using k nearest neighbor voting
- Simple average: Find the average and classify using k nearest neighbor voting
- Weighted average: Find the weighted average (using 0.2, 0.3, and 0.5 respectively) and classify using k nearest neighbor voting
- Compare the results of these votings, seeing which method produced the most stable inferences and how they affect responsiveness

### No Averaging Distances
#### Calm with Slight Jitter:
##### Reading One: (24, 6, 4):
- Distance to chaotic (65, 53, 22) → 41 + 47 + 18 = 106​
- Distance to calm (30, 10, 2) → 6 + 4 + 2 = 12
- Distance to calm (31, 11, 3) → 7 + 5 + 1 = 13
- Distance to chaotic (74, 39, 13) → 50 + 33 + 9 = 92
- Distance to chaotic (80, 40, 8) → 56 + 34 + 4 = 94
- Distance to calm (29, 7, 2) → 5 + 4 + 2 = 8

##### Reading Two: (26, 7, 3):
- Distance to chaotic (65, 53, 22) → 39 + 46 + 19 = 104​
- Distance to calm (30, 10, 2) → 4 + 3 + 1 = 8
- Distance to calm (31, 11, 3) → 5 + 4 + 0 = 9
- Distance to chaotic (74, 39, 13) → 48 + 32 + 10 = 90
- Distance to chaotic (80, 40, 8) → 54 + 33 + 5 = 92
- Distance to calm (29, 7, 2) → 3 + 0 + 1 = 4

##### Reading Three: (23, 5, 5):
- Distance to chaotic (65, 53, 22) → 42 + 48 + 17 = 107​
- Distance to calm (30, 10, 2) → 7 + 5 + 3 = 15
- Distance to calm (31, 11, 3) → 8 + 6 + 2 = 16
- Distance to chaotic (74, 39, 13) → 51 + 34 + 8 = 93
- Distance to chaotic (80, 40, 8) → 57 + 35 + 3 = 95
- Distance to calm (29, 7, 2) → 6 + 2 + 3 = 11
  
#### Calm → Chaotic:
##### Readings One and Two: (24, 6, 4): 
- Distance to chaotic (65, 53, 22) → 41 + 47 + 18 = 106​
- Distance to calm (30, 10, 2) → 6 + 4 + 2 = 12
- Distance to calm (31, 11, 3) → 7 + 5 + 1 = 13
- Distance to chaotic (74, 39, 13) → 50 + 33 + 9 = 92
- Distance to chaotic (80, 40, 8) → 56 + 34 + 4 = 94
- Distance to calm (29, 7, 2) → 5 + 1 + 2 = 8

##### Reading Three: (70, 43, 17):
- Distance to chaotic (65, 53, 22) → 5 + 10 + 5 = 20​
- Distance to calm (30, 10, 2) → 40 + 33 + 15 = 88
- Distance to calm (31, 11, 3) → 39 + 32 + 14 = 85
- Distance to chaotic (74, 39, 13) → 4 + 4 + 4 = 12
- Distance to chaotic (80, 40, 8) → 10 + 3 + 9 = 22
- Distance to calm (29, 7, 2) → 41 + 36 + 15 = 92

#### Chaotic → Calm:
##### Readings One and Two: (70, 43, 17):
- Distance to chaotic (65, 53, 22) → 5 + 10 + 5 = 20​
- Distance to calm (30, 10, 2) → 40 + 33 + 15 = 88
- Distance to calm (31, 11, 3) → 39 + 32 + 14 = 85
- Distance to chaotic (74, 39, 13) → 4 + 4 + 4 = 12
- Distance to chaotic (80, 40, 8) → 10 + 3 + 9 = 22
- Distance to calm (29, 7, 2) → 41 + 36 + 15 = 92

##### Reading Three: (24, 6, 4):
- Distance to chaotic (65, 53, 22) → 41 + 47 + 18 = 106​
- Distance to calm (30, 10, 2) → 6 + 4 + 2 = 12
- Distance to calm (31, 11, 3) → 7 + 5 + 1 = 13
- Distance to chaotic (74, 39, 13) → 50 + 33 + 9 = 92
- Distance to chaotic (80, 40, 8) → 56 + 34 + 4 = 94
- Distance to calm (29, 7, 2) → 5 + 1 + 2 = 8

### Simple Averaging Distances:
#### Calm with Slight Jitter:
- Distance to chaotic (65, 53, 22) → 40.67 + 47 + 18 = 105.67​
- Distance to calm (30, 10, 2) → 5.67 + 4 + 2 = 11.67
- Distance to calm (31, 11, 3) → 6.67 + 5 + 1 = 12.67
- Distance to chaotic (74, 39, 13) → 49.67 + 33 + 9 = 91.67
- Distance to chaotic (80, 40, 8) → 55.67 + 34 + 4 = 93.67
- Distance to calm (29, 7, 2) → 4.67 + 1 + 2 = 7.67

#### Calm → Chaotic:
- Distance to chaotic (65, 53, 22) → 25 + 34.67 + 13.67 = 73.34​
- Distance to calm (30, 10, 2) → 10 + 8.33 + 6.33 = 24.66
- Distance to calm (31, 11, 3) → 9 + 7.33 + 5.33 = 21.66
- Distance to chaotic (74, 39, 13) → 34 + 20.67 + 4.67 = 59.34
- Distance to chaotic (80, 40, 8) → 40 + 21.67 + 0.33 = 62.00
- Distance to calm (29, 7, 2) → 11 + 11.33 + 6.33 = 28.66

#### Chaotic → Calm:
- Distance to chaotic (65, 53, 22) → 10.34 + 22.34 + 9.34 = 42.02​
- Distance to calm (30, 10, 2) → 24.66 + 20.66 + 10.66 = 55.98
- Distance to calm (31, 11, 3) → 23.66 + 19.66 + 9.66 = 52.98
- Distance to chaotic (74, 39, 13) → 19.34 + 8.34 + 0.34 = 28.02
- Distance to chaotic (80, 40, 8) → 25.34 + 9.34 + 4.66 = 39.34
- Distance to calm (29, 7, 2) → 25.66 + 23.66 + 10.66 = 59.98

### Computations when k = 3
#### No Averaging (Just use third point for voting):
##### Calm With Slight Jitter:
Third point: (23, 5, 5)

k nearest neighbors: 
- calm (30, 10, 2)
- calm (31, 11, 3)
- calm (29, 7, 2)

Final classification: calm

##### Calm → Chaotic:
Third point: (70, 43, 17)

k nearest neighbors:
- chaotic (65, 53, 22)
- chaotic (74, 39, 13)
- chaotic (80, 40, 8)

Final classification: chaotic

##### Chaotic → Calm:
Third point: (24, 6, 4)

k nearest neighbors:
- calm (30, 10, 2)
- calm (31, 11, 3)
- calm (29, 7, 2)

Final classification: calm


#### Simple Averaging Points (Rounded to nearest hundredth):
Averaged Point One: (L1+L2+L3)/3 
Averaged Point Two: (N1+N2+N3)/3
Averaged Point Three: (M1+M2+M3)/3
##### Calm with Slight Jitter:
Current readings:
- (24, 6, 4)
- (26, 7, 3)
- (23, 5, 5)

Averaged Point One Calculations: (24 + 26 + 23) / 3 = 73 / 3 = 24.33
Averaged Point Two Calculations: (6 + 7 + 5) / 3 = 18 / 3 = 6.00
Averaged Point Three Calculations: (4 + 3 + 5) / 3 = 12 / 3 = 4.00

Final Point with Simple Averaging: (24.33, 6.00, 4.00) 

k nearest neighbors:
- calm (30, 10, 2)
- calm (31, 11, 3)
- calm (29, 7, 2)

Final Classification: calm

##### Calm → Chaotic:
Current readings:
- (24, 6, 4) (calm)
- (26, 6, 4) (calm)
- (70, 43, 17) (chaotic)

Averaged Point One Calculations: (24 + 26 + 70) / 3 = 120 / 3 = 40.00
Averaged Point Two Calculations: (6 + 6 + 43) / 3 = 55 / 3 = 18.33
Averaged Point Three Calculations: (4 + 4 + 17) / 3 = 25 / 3 = 8.33

Final Point with Simple Averaging: (40.00, 18.33, 8.33)

k nearest neighbors:
- calm (30, 10, 2)
- calm (31, 11, 3)
- calm (29, 7, 2)

##### Chaotic → Calm:
Current Readings:
- (70, 43, 17) (chaotic)
- (70, 43, 17) (chaotic)
- (24, 6, 4) (calm)

Averaged Point One Calculations: (70 + 70 + 24) / 3 = 164 / 3 = 54.66
Averaged Point Two Calculations: (43 + 43 + 6) / 3 = 92 / 3 = 30.66
Averaged Point Three Calculations: (17 + 17 + 4) / 3 = 38 / 3 = 12.66

Final Point with Simple Averaging: (54.66, 30.66, 12.66)

k nearest neighbors:
- chaotic (74, 39, 13)
- chaotic (80, 40, 8)
- chaotic (65, 53, 22)

Final classification: chaotic

### Experiment Notes:
#### For Tests with No Averaging:
- For all of the test readings ("calm with slight jitter" test reading, there was a stable and accurate result, with all of the 3 nearest neighbors agreeing on the same mood label
- However, the distances to the nearest neighbors changed between readings, meaning the input point was moving due to small changes in sensor values
- This shows that the nearest neighbor voting is enough to handle label noise in the previously stored data, but not the fluctuations in the current sensor readings
- In scenarios with sudden changes, having no averaging allows the system to respond immediately, but may come at the cost of increased sensitivity to noise

#### For Tests with Simple Averaging
# DOOOOO THISS
