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

## Experiment #2: 12/28/25-01/01/26
### This experiment has no code or hardware, it is just to compare averaging methods
### This experiment is organized by method rather than chronological order, reflecting how the analysis was conducted.

### Goal:
Test how different types of averaging (no averaging, simple average, and weighted average) affect stability, during jitter and sudden changes, and responsiveness

### Setup:
Assume the sensors are light (L), noise (N), and moption sensors (M)
  
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
- Compare the results of these votings, seeing which method produced the most stable inferences and how they affect responsiveness and latency

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

### Weighted Averaging Distances
#### Calm with Slight Jitter:
- Distance to chaotic (65, 53, 22) → 40.90 + 47.20 + 17.80 = 105.90​
- Distance to calm (30, 10, 2) → 5.90 + 4.20 + 2.20 = 12.30
- Distance to calm (31, 11, 3) → 6.90 + 5.20 + 1.20 = 13.30
- Distance to chaotic (74, 39, 13) → 40.90 + 33.20 + 8.80 = 91.90
- Distance to chaotic (80, 40, 8) → 55.90 + 34.20 + 3.80 = 93.90
- Distance to calm (29, 7, 2) → 4.90 + 1.20 + 2.20 = 8.30

#### Calm → Chaotic:
- Distance to chaotic (65, 53, 22) → 18 + 29.50 + 11.50 = 58.00​
- Distance to calm (30, 10, 2) → 17 + 14.50 + 8.50 = 40.00
- Distance to calm (31, 11, 3) → 16 + 13.50 + 7.50 = 37.00
- Distance to chaotic (74, 39, 13) → 27 + 14.50 + 2.50 = 44.00
- Distance to chaotic (80, 40, 8) → 33 + 15.50 + 2.50 = 51.00
- Distance to calm (29, 7, 2) → 18 + 17.50 + 8.50 = 44.00

#### Chaotic → Calm:
- Distance to chaotic (65, 53, 22) → 18 + 29.50 + 11.50 = 58.00​
- Distance to calm (30, 10, 2) → 17 + 14.50 + 8.50 = 40.00
- Distance to calm (31, 11, 3) → 16 + 13.50 + 7.50 = 37.00
- Distance to chaotic (74, 39, 13) → 27 + 14.50 + 2.50 = 44.00
- Distance to chaotic (80, 40, 8) → 33 + 15.50 + 2.50 = 51.00
- Distance to calm (29, 7, 2) → 18 + 17.50 + 8.50 = 44.00
  
### Computations
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

#### Weighted Averaging Points (Rounded to nearest hundredth):

Averaged Point One: 0.2*(L1)+0.3*(L2)+0.5*(L3) 

Averaged Point Two: 0.2*(N1)+0.3*(N2)+0.5*(N3) 

Averaged Point Three: 0.2*(M1)+0.3*(M2)+0.5*(M3) 

##### Calm with Slight Jitter:
Current readings:
- (24, 6, 4)
- (26, 7, 3)
- (23, 5, 5)

Averaged Point One Calculations: 0.2 * (24) + 0.3 * (26) + 0.5 * (23) = 4.8 + 7.8 + 11.5 = 24.10

Averaged Point Two Calculations: 0.2*(6) + 0.3*(7) + 0.5*(5) = 1.2 + 2.1 + 2.5 = 5.80

Averaged Point Three Calculations: 0.2 * (4) + 0.3 * (3) + 0.5 * (5) = 0.8 + 0.9 + 2.5 = 4.20

Final Point with Weighted Averaging: (24.10, 5.80, 4.20) 

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

Averaged Point One Calculations: 0.2 * (24) + 0.3 * (24) + 0.5 * (70) = 4.8 + 7.2 + 35 = 47.00

Averaged Point Two Calculations: 0.2 * (6) + 0.3 * (6) + 0.5 * (43) = 1.2 + 1.8 + 21.5 = 24.50

Averaged Point Three Calculations: 0.2 * (4) + 0.3 * (4) + 0.5 * (17) = 0.8 + 1.2 + 8.5 = 10.50

Final Point with Weighted Averaging: (47.00, 24.50, 10.50)

k nearest neighbors:
- calm (30, 10, 2)
- calm (31, 11, 3)
- chaotic (74, 39, 13)

Final Classification: calm

##### Chaotic → Calm:

Current readings:
- (70, 43, 17) (chaotic)
- (70, 43, 17) (chaotic)
- (24, 6, 4) (calm)

Averaged Point One Calculations: 0.2 * (70) + 0.3 * (70) + 0.5 * (24) = 14 + 21 + 12 = 47.00

Averaged Point Two Calculations: 0.2 * (43) + 0.3 * (43) + 0.5 * (6) = 8.6 + 12.3 + 3 = 24.50

Averaged Point Three Calculations: 0.2 * (17) + 0.3 * (17) + 0.5 * (4) = 3.4 + 5.1 + 2 = 10.50

Final Point with Weighted Averaging: (47.00, 24.50, 10.50)

k nearest neighbors:
- calm (30, 10, 2)
- calm (31, 11, 3)
- chaotic (74, 39, 13)

Final Classification: calm

### Experiment Notes:
#### For Tests with No Averaging:
- For all of the test readings ("calm with slight jitter", calm → chaotic, chaotic → calm), there was a stable and accurate result, with all of the 3 nearest neighbors agreeing on the same mood label
- However, the distances to the nearest neighbors changed between readings, meaning the input point was moving due to small changes in sensor values
- This shows that the nearest neighbor voting is enough to handle label noise in the previously stored data, but not the fluctuations in the current sensor readings
- In scenarios with sudden changes, having no averaging allows the system to respond immediately, but may come at the cost of increased sensitivity to noise

#### For Tests with Simple Averaging
- For the first test reading ("calm with slight jitter"), the result was accurate. Averaging helped find a calm middle ground, reducing the effect of noise.
- However, for the other two test readings (calm → chaotic and chaotic → calm), the final classifications were incorrect and showed noticeable lag.
- This confirms the presence of latency: even though the room’s mood had already changed, simple averaging kept the averaged point closer to the previous state, resulting in an incorrect output.
- The main limitation of simple averaging is that the model "remembers" older states too strongly. While this greatly stabilizes noise, it reduces responsiveness to sudden changes, motivating the need for weighted averaging.

#### For Tests with Weighted Averaging
- For the first test reading ("calm with slight jitter"), the result was accurate. Averaging helped find a calm middle ground, similar to the simple averaging tests, with slight favor for the more recent readings.
- In the calm → chaotic and chaotic → calm tests, weighted averaging reduced latency compared to simple averaging by shifting the averaged point closer to the most recent state. This caused one of the nearest neighbors to shift toward the correct mood, indicating reduced latency compared to simple averaging.
- However, weighted averaging did not immediately change the mood based on sudden changes, showing that some latency was still present due to the influence of older readings.
- Compared to simple averaging, using weighted averaging represents a better balance between stability and responsiveness. It also reduces noise in the readings while allowing the system to respond faster to changes, making it a more suitable approach for mood inference.

#### Overall

- No averaging produced the fastest responses to changes in room conditions, correctly reflecting sudden mood shifts immediately. However, this approach is highly sensitive to noise and small fluctuations in sensor readings.

- Simple averaging greatly reduced noise and stabilized the system’s output, but introduced significant latency. In both calm → chaotic and chaotic → calm tests, the system lagged behind the true room state, with none of the nearest neighbors matching the true mood

- Weighted averaging provided a compromise between these two approaches. It reduced noise while responding faster than simple averaging, though some latency still remained due to the influence of older readings, with one of the nearest neighbors matching the true mood
  
## Conclusion:

This experiment demonstrated that averaging and voting address different sources of instability in the system. Voting improves robustness against mislabeled or imperfect stored data, while averaging stabilizes noisy sensor inputs over time.

Simple averaging is effective for noise reduction but causes unacceptable latency when room conditions change suddenly. Weighted averaging improves responsiveness by prioritizing recent readings while still smoothing noise, making it a better choice for real-time inference.

Based on these results, weighted averaging combined with distance-based voting is the most appropriate approach moving forward. Future work will focus on tuning weights, defining uncertainty thresholds, and expanding mood labels to improve accuracy and expressiveness.


---

## Experiment #3: 3/14/26-3/15/26
### This experiment has no code or hardware, it is just to add some key features and test what they will do

### Goal:

Add one more mood label (medium) and add a confidence rating based on the split of the votes. Test if adding these things helps with a more accurate final answer.

### Setup:
Assume the sensors are light (L), noise (N), and moption sensors (M)
  
Assume that the previously labeled data points are true, and that the labels were given by the same person so there are no subjective errors
  
Assume that all of the data points are listed after being normalized
  
Assume that there are three mood labels: calm, medium, and chaotic

Assume that the classifier is k nearest neighbor voting using Manhattan distance (k = 5)

Assume that the points were averaged with weights of 0.2, 0.3, and 0.5, with the last being the most recent point

Assume that the data points in each "current reading" section are taking consecutively

###  *Part 1*
### Data Points
#### Previously Stored Data:
(L,N,M) → Mood

- (65, 53, 22) → chaotic
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (74, 39, 13) → chaotic
- (80, 40, 8) → chaotic
- (29, 7, 2) → calm
- (45, 24, 9) → medium
- (50, 28, 10) → medium
- (42, 22, 8) → medium

#### Current Data Points:
##### Clearly Calm:
- (24, 6, 4)
##### Clearly Medium:
- (44, 23, 9)
##### In-between Medium and Chaotic:
- (56, 31, 11)

### Procedure
For each point:
- Compute Manhattan distances to all stored data
- Find the k closest neighbors (k=5 for now)
- Find the predicted mood using majority voting
- Calculate the "confidence rating" by finding the proportion of the k nearest neighbors that agree
- Compare whether the middle label helps improve accuracy
- Compare whether the confidence score gives a good understanding on uncertain cases

### Calculations:
#### Clearly Calm:

Current reading: (24, 6, 4)

##### Distances:
- Distance to chaotic (65, 53, 22) → 41 + 47 + 18 = 106
- Distance to calm (30, 10, 2) → 6 + 4 + 2 = 12
- Distance to calm (31, 11, 3) → 7 + 5 + 1 = 13
- Distance to chaotic (74, 39, 13) → 50 + 33 + 9 = 92
- Distance to chaotic (80, 40, 8) → 56 + 34 + 4 = 94
- Distance to calm (29, 7, 2) → 5 + 1 + 2 = 8
- Distance to medium (45, 24, 9) → 21 + 18 + 5 = 44
- Distance to medium (50, 28, 10) → 26 + 22 + 6 = 54
- Distance to medium (42, 22, 8) → 18 + 16 + 4 = 38

##### Voting:

k nearest neighbors (k = 5):
- calm (29, 7, 2)
- calm (30, 10, 2)
- calm (31, 11, 3)
- medium (42, 22, 8)
- medium (45, 24, 9)

Final Classification: Calm
Confidence Rating: 3/5 = 0.60

#### Clearly Medium

Current Reading: (44, 23, 9)

##### Distances:
- Distance to chaotic (65, 53, 22) → 21 + 30 + 13 = 64
- Distance to calm (30, 10, 2) → 14 + 13 + 7 = 34
- Distance to calm (31, 11, 3) → 13 + 12 + 6 = 31
- Distance to chaotic (74, 39, 13) → 30 + 16 + 4 = 50
- Distance to chaotic (80, 40, 8) → 36 + 17 + 1 = 54
- Distance to calm (29, 7, 2) → 15 + 16 + 7 = 38
- Distance to medium (45, 24, 9) → 1 + 1 + 0 = 2
- Distance to medium (50, 28, 10) → 6 + 5 + 1 = 12
- Distance to medium (42, 22, 8) → 2 + 1 + 1 = 4

##### Voting:

k nearest neighbors (k = 5):
- medium (45, 24, 9)
- medium (42, 22, 8)
- medium (50, 28, 10)
- calm (31, 11, 3)
- calm (30, 10, 2)

Final Classification: Medium
Confidence Rating: 3/5 = 0.60

#### In-between

Current Reading: (56, 31, 11)

##### Distances:

- Distance to chaotic (65, 53, 22) → 9 + 22 + 11 = 42
- Distance to calm (30, 10, 2) → 26 + 21 + 9 = 56
- Distance to calm (31, 11, 3) → 25 + 20 + 8 = 53
- Distance to chaotic (74, 39, 13) → 18 + 8 + 2 = 28
- Distance to chaotic (80, 40, 8) → 24 + 9 + 3 = 36
- Distance to calm (29, 7, 2) → 27 + 24 + 9 = 60
- Distance to medium (45, 24, 9) → 11 + 7 + 2 = 20
- Distance to medium (50, 28, 10) → 6 + 3 + 1 = 10
- Distance to medium (42, 22, 8) → 14 + 9 + 3 = 26

##### Voting:

k nearest neighbors (k = 5):
- medium (50, 28, 10)
- medium (45, 24, 9)
- medium (42, 22, 8)
- chaotic (74, 39, 13)
- chaotic (80, 40, 8)

Final Classification: Medium
Confidence RatingL 3/5 = 0.60

### Part 1 Conclusion
This experiment showed that adding a medium label improved the model’s ability
to represent in-between moods. However, defining confidence only by vote
strength was not sufficient, since both clearly medium and borderline cases
received the same score. This suggests that a better confidence method should
also account for distance separation between competing classes. This makes me think that using the distances between the current point and the nearest neighbors will be helpful

### *Part 2*

In this part, I am going to test out using the distances between the current reading and the nearest neighbors to see if that provides for a more accurate confidence rating. In other words, a prediction should have higher confidence when the winning class is much closer than the runner-up class.

To calculate this, I am going to:
- Find the predicted class as done before
- Take the neighbors from the predicted class and the runner-up class
- Compute the average distances for each
- Compare them

I am going to use the previously determined current points, stored data points, distance calculations, and predictions as before, and am not going to rewrite all of them.

### Clearly Calm
Current Point: (24, 6, 4)
#### Final Prediction: Calm
Calm Stored Points:
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (29, 7, 2) → calm

Distances:
- Distance to calm (30, 10, 2) → 6 + 4 + 2 = 12
- Distance to calm (31, 11, 3) → 7 + 5 + 1 = 13
- Distance to calm (29, 7, 2) → 5 + 1 + 2 = 8

Average Distance:
(12 + 13 + 8) / 3 = 33 / 3 = **11**

#### Runner-up: Medium
Closest Medium Stored Points:
- (45, 24, 9) → medium
- (50, 28, 10) → medium
- (42, 22, 8) → medium

Distances:
- Distance to medium (42, 22, 8) → 18 + 16 + 4 = 38
- Distance to medium (45, 24, 9) → 21 + 18 + 5 = 44


Average Distance:
(44 + 38) / 3 = 82 / 2 = **41**

#### Distance Gap
41 - 11 = 30

Since a gap of 30 is large, the confidence rating will be "high", although I need to make specific thresholds for the different ratings

### Clearly Medium
Current Point: (44, 23, 9)
#### Final Prediction: Medium
Medium Stored Points:
- (45, 24, 9) → medium
- (50, 28, 10) → medium
- (42, 22, 8) → medium

Distances:
- Distance to medium (45, 24, 9) → 1 + 1 + 0 = 2
- Distance to medium (50, 28, 10) → 6 + 5 + 1 = 12
- Distance to medium (42, 22, 8) → 2 + 1 + 1 = 4

Average Distance:
(2 + 12 + 4) / 3 = 18 / 3 = **6**

#### Runner-up: Calm
Closest Calm Stored Points: 
- (30, 10, 2) → calm
- (31, 11, 3) → calm

Distances:
- Distance to calm (30, 10, 2) → 14 + 13 + 7 = 34
- Distance to calm (31, 11, 3) → 13 + 12 + 6 = 31

Average Distance:
(34 + 31) / 2 = 65 / 2 = **32.5**

#### Distance Gap
32.5 - 6 = 26.5

Since a gap of 26.5 is large, the confidence rating will be "high", although I need to make specific thresholds for the different ratings

### In-between
Current Point: (56, 31, 11)
#### Final Prediction: Medium
Medium Stored Points:
- (45, 24, 9) → medium
- (50, 28, 10) → medium
- (42, 22, 8) → medium

Distances:
- Distance to medium (45, 24, 9) → 11 + 7 + 2 = 20
- Distance to medium (50, 28, 10) → 6 + 3 + 1 = 10
- Distance to medium (42, 22, 8) → 14 + 9 + 3 = 26

Average Distance:
(20 + 10 + 26) / 3 = 56 / 3 ≈ **18.67**

#### Runner-up: Chaotic
Closest Chaotic Points:
- chaotic (74, 39, 13)
- chaotic (80, 40, 8)

Distances:
- Distance to chaotic (74, 39, 13) → 18 + 8 + 2 = 28
- Distance to chaotic (80, 40, 8) → 24 + 9 + 3 = 36

Average Distance:
(28 + 36) / 2 = 64 / 2 = **32**

#### Distance Gap
32 - 18.67 = 13.33

Since this is a smaller gap compared to the other two tests, this should be classified as a "medium" confidence, although I need to make specific thresholds for the different ratings

### Part 2 Conclusion:
Changing the way I calculated the confidence rating improved the accuracy of these. When testing points that were clearly one mood, the confidence rating was high, as opposed to when I tested a point which was more in-between two labels, where it gave me a medium rating. This shows that the usage of distances in the calculation for the confidence score helps give an accurate result.

## Conclusion

This experiment tested whether adding a middle mood label and a confidence rating would improve the system’s ability to interpret room states.

Adding the medium label improved the model’s expressiveness. In the earlier experiments, the classifier was forced to output either calm or chaotic even when the input was somewhere between the two. After introducing medium-labeled points, the model was able to correctly classify intermediate states that were not clearly calm or chaotic.

The first confidence method defined confidence using only vote strength (agreeing neighbors divided by k). However, this method produced the same confidence score for clearly medium points and borderline points. This showed that vote strength alone does not fully capture how certain the model’s prediction actually is.

To address this limitation, confidence was revised to also consider distance separation between the predicted class and the next closest competing class. By comparing the average distance of neighbors belonging to the predicted class with the average distance of neighbors belonging to the runner-up class, the confidence score better reflected how strongly the predicted mood dominated the local neighborhood.

Using this revised method, clearly calm and clearly medium cases showed large distance gaps and therefore high confidence, while borderline cases showed smaller gaps and lower confidence. This confirms that distance-based confidence provides a more informative measure of prediction certainty than vote strength alone.

Overall, this experiment demonstrates that adding a middle mood label improves the system’s ability to represent real-world room states, while a distance-based confidence measure helps communicate how reliable a prediction is. Based on these results, the final system design will use:

- weighted averaging for noise reduction
- Manhattan distance with k-nearest neighbor voting for classification
- three mood labels: calm, medium, and chaotic
- a distance-based confidence measure

These results complete the design phase of the model and provide a clear framework for implementing the algorithm in code, which is most likely the next step.










