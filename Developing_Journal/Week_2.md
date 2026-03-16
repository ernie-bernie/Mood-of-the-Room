# Week #2, Started 12/27/25

### Context
This week begins immediately after completing Paper Experiment #1.
The results from that experiment validated the use of Manhattan distance
and voting, and revealed limitations related to missing labels and
uncertainty handling.

Although this entry is labeled Week 2, it began earlier than a full calendar
week because Experiment #1 reached a clear conclusion and motivated new
questions.

The focus of this week is to build on those results rather than repeat
earlier research.

## Goals for This Week
- Design and run a second paper experiment focused on averaging methods
- Compare no averaging vs simple averaging vs weighted averaging
- Decide whether weighted averaging meaningfully improves responsiveness
- Think about how confidence or uncertainty could be reported to the user
- Attempt to test how adding more mood labels changes the system's response

## What I’m Starting With
From Experiment #1, I now know:
- Distance-based voting is stable for known classes
- Increasing k from 3–5 does not change results
- The system cannot infer moods that are not represented in the dataset
- An uncertainty or “unknown” output may be necessary

These conclusions will help me with this week's work.

## New Questions This Week
- How much noise reduction is actually gained by averaging?
- How much do different types of averaging affect responsiveness?
- Does weighted averaging respond faster to sudden changes?
- Does weighted averaging make the response more accurate?
- How should recent sensor readings be weighted?
- How could a confidence rating help and how would it work?
 
## Planned Experiments
### Experiment #2 – Temporal Averaging
Planned comparison:
- No averaging (single reading)
- Simple average of 3 consecutive readings
- Weighted average favoring recent readings

This experiment will focus on how averaging affects mood stability and response time during sudden changes.

### Experiment #3 - Increasing Mood labels and Adding Confidence
Planned additions:
- 3 mood labels (Adding a "medium" in-between calm and chaotic)
- A confidence rating found by using the proportion of votes

This experiment will show me the benefits of two major additions.

## Open Problems
- What is a good window size for the averaging?
- Defining what counts as a “sudden change”
- Deciding how to measure responsiveness without real hardware or code
- Avoiding over-smoothing important changes
  
## Notes & Observations
- Experiment 2 taught me a lot about how the different methods (no averaging, simple averaging, and weighted averaging) would affect accuracy and responsiveness, especially when mood flips were involved. No averaging produced a very fast response, but it was highly sensitive to sensor noise. Simple averaging reduced noise, but introduced a very high amount of latency, which meant that the predicted mood labels were often incorrect. Finally, using weighted averaging reduced noise just as simple averaging did, but also had less latency, with at least one of the nearest neighbors matching the correct mood in all tests. This showed me that using a weighted average would be the most logical choice for this scenario.
- Using nearest-neighbor voting handles label noise, while using weighted averaging handles sensor noise, so using both is ideal
- After completing Experiment 2, I stopped working on this project for a while, and am starting to get back into it mid-March.
- Experiment 3 helped me understand the benefit of using another "middle" mood. It improved the accuracy of the final answer, and allowed for a less forced, incorrect answer. In addition to this, adding a confidence rating by just finding the proportion of votes could get the same "confidence" for two completely different inputs. This led me to factor in distances between the input and the point stored as the moods. This increased the effectiveness of the confidence rating and helps the user understand how reliable a prediction is.
- At this point, the conceptual design of the system is mostly complete. The next stage of the project will focus on implementing the model in code and testing it using simulated data before connecting real sensors.
  
## End-of-Week Reflection
- What worked: Experiment 2 taught me a lot about how I should be averaging my points, and Experiment 3 showed me the benefit of adding a 3rd mood as well as the confidence rating.
- What didn’t: At first, the confidence rating did not provide the correct confidence, since it had the same confidence on both a borderline and a clearly calm input. This took some thought on how to fix.
- What surprised me: I was surprised that different averaging methods could provide such different results. I thought that using a weighted average would provide the same result as a simple average, but I learned that this was not the case.

## Next Steps
- Decide if I want to incorporate any additional features before coding
- Begin implementing the model in code using simulated data (no hardware yet)
- Finalize a working algorithm that includes weighted averaging, k-nearest neighbor voting, and the confidence rating
