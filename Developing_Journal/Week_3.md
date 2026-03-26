# Week #3, Started 3/15/26

### Context
This week begins after completing Experiment #3, which tested the addition of a middle mood label and a revised confidence rating based on distance
separation. With Experiments 1–3 complete, the conceptual design of the system is now mostly finalized.

The focus of this week is to begin transitioning from research and paper experiments into implementation.

## Goals for This Week
- Finalize the algorithm based on the results of Experiments 1–3
- Create the Code folder and document the implementation phase
- Begin writing a Python prototype using simulated data
- Implement weighted averaging, Manhattan distance, and k-nearest neighbor voting
- Start implementing the distance-based confidence measure

## What I’m Starting With
From the completed experiments, I now know:
- Manhattan distance works well for comparing stored points
- k-nearest neighbor voting improves robustness compared to a single nearest neighbor
- Weighted averaging is the best balance between noise reduction and responsiveness
- Adding a medium label improves the model’s expressiveness
- Vote-strength confidence was too weak, but distance-based confidence is more informative

These conclusions define the system that I will now begin implementing in code.

## New Questions This Week
- How should I structure the Python code so each step of the model is clear?
- What should be stored as labeled training data in the first prototype?
- How should I represent confidence thresholds in code?
- How can I test the implementation against the paper experiments?
- What parts of the system should be implemented first?

## Planned Work
### Algorithm Finalization
- Write down the final step-by-step logic of the model
- Confirm the order of operations from sensor readings to final output

### Prototype Implementation
- Create a Python file for the first version of the model
- Hardcode labeled points and test inputs
- Implement weighted averaging
- Implement Manhattan distance
- Implement k-nearest neighbor voting
- Implement distance-gap confidence
- Test whether the code reproduces the same results as the paper experiments

## Open Problems
- Defining exact thresholds for confidence categories
- Deciding how to store and organize labeled data points
- Making sure the code stays readable and modular
- Determining when to move from simulated data to real sensors

## Notes & Observations
- On 3/20/26, I completed my first prototype of the code, putting together all of the functions I had created and getting the final output of the predicted mood and the confidence. I am now going to move into testing it with points from Experiment 3
- After testing with points from Experiment 3, I have concluded that I have successfully created a full working prototype of the mood prediction and confidence rating system. This means I can now move on into testing with many more points, and expand the stored data set
- After testing more points, all of them had the expected result, which means I will move onto expanding the stored data set. I will need to decide if asking the user for the accuracy of the predicted mood or basing it off of confidence is better.
- After some consideration, I believe that I will do the following to add the point to th stored data set.
  - If the confidence is "high" for 6 or more consectutive readings, ONE representative point will be added to the stored data
  - If the confidence is "low" for 6 or more consecutive readings, the user will be asked for the accurate mood of the room. (This may be implemented later on)


## End-of-Week Reflection
- What worked:
- What didn’t:
- What surprised me:

## Next Steps
- Finish the first prototype
- Verify that the code matches the paper experiments
- Decide when to move toward real sensor integration
