# Alpha Tests and Experiments
## Experiment #1: 12/27/25
### This experiment has no code or hardware, it is just to show the procedure and run through the steps

### Goal:
Test if this program would infer the correct mood of the room, but with no hardware or code yet. 

### Setup:
Assume k=3, with the sensors being light, motion, and noise sensors
Assume that the previously labeled data points are true, and that the labels were given by the same person so there is no subjective errors
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
- (29, 10, 2) → calm 
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
- Distance to chaotic (65, 53, 22) → 25 + 28 +`6 = 69
- Distance to calm (30, 10, 2) → 10 + 15 + 4 = 29
- Distance to calm (31, 11, 3) → 9 + 14 + 3 = 26
- Distance to chaotic (74, 39, 13) → 34 + 14 + 7 = 55
- Distance to chaotic (80, 40, 8) → 40 + 15 + 2 = 57
- Distance to calm (29, 7, 2) → 11 + 18 + 4 = 33
#### Current Chaotic Reading:
- Distance to chaotic (65, 53, 22) → 5 + 10 +`5 = 20
- Distance to calm (30, 10, 2) → 40 + 33 + 15 = 88
- Distance to calm (31, 11, 3) → 39 + 32 + 14 = 85
- Distance to chaotic (74, 39, 13) → 4 + 4 + 4 = 12
- Distance to chaotic (80, 40, 8) → 10 + 3 + 9 = 22
- Distance to calm (29, 7, 2) → 41 + 36 + 15 = 92

### Voting with NN and closest three
#### Current Calm:
##### Nearest Neighbor(NN)
(29, 7, 2) → calm
Final classification: calm
##### Closest three voting (not in order):
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (29, 10, 2) → calm
  
Final classification: calm

#### Current Medium:
##### Nearest Neighbor(NN)
(31, 11, 3) → calm
Final classification: calm
##### Closest three voting (not in order):
- (30, 10, 2) → calm
- (31, 11, 3) → calm
- (29, 10, 2) → calm
  
Final classification: calm

#### Current Chaotic:
##### Nearest Neighbor(NN)
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
- For a calm test reading, the three nearest neighbors were all labeled calm, and majority voting produced a stable classification, just as using the NN did. The voting ignored the far-away chaotic points, and using the Manhattan distance did not cause disproportionate data.
- For a medium test reading, all nearest neighbors were labeled calm, indicating that the model cannot output intermediate moods unless those labels exist in the data. This showed me a design gap in my reasoning. To overcome this, I may need to incorporate more labels or an uncertain response.
- For a chaotic test reading, the three nearest neighbors were all labeled chaotic, and majority voting produced a stable classification, just as using the NN did. The voting ignored the far-away calm points, and using the Manhattan distance did not cause disproportionate data.

#### Tests using 4 and 5 votes:
- For a calm test reading, increasing k from 3 to 4 and 5 did not change the classification for calm inputs, indicating strong cluster seperation. This means that if I keep k as 3, it will be confident and fast, while using k as 4 or 5 means it will be more robust against bad points, such as if a human mislabels a point.
- For a medium test reading, increasing k from 3 to 4 and 5 did not change the classification, indicating that without medium-labeled data the model defaults to the closest existing class. This further supports that this is a dataset limitation.
- For a chaotic test reading, increasing k from 3 to 4 and 5 also did not change the classification, showing us that voting is consistently stable as k increases. This means that any value for k from 3-5 would work for this project.
  
What this means:
- My distance and voting logic works
- My dataset shape controls what outputs are possible, so a safeguard must be put into place so a forced, incorrect answer is not inferred.
- The clusters are well seperated with these made-up data points

## Conclusion

This experiment showed that using Manhattan distance with k-nearest neighbors and majority voting produced stable and accurate classifications for both chaotic and calm inputs while using the made-up datasets. Increasing k from 3 to 4 and 5 did not change the final classification in any of the tests, indicating that clusters in the dataset are well separated and that voting improves robustness. This also shows me that if one data point was mislabeled, having voting will limit the probability of the final answer being inaccurate.

This experiment also revealed an important limitation: when a "medium" input was tested, the system defaulted to the closest existing label (calm) because there was no datasets that had a medium label. This demonstrates that the model cannot infer moods that were not already represented in the dataset.

Overall, this experiment validates the use of Manhattan distance-based voting as an approach that I can use while surfacing the need for better/more labels or an "uncertain" answer option. Based on these results, the next step is to evaluate how temportal averaging and weighted averaging affect classification stability and responsiveness.
