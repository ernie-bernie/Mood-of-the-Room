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
- Attempt to test how adding more mood labels changes system responses

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
 
## Planned Experiments
### Experiment #2 – Temporal Averaging
Planned comparison:
- No averaging (single reading)
- Simple average of 3 consecutive readings
- Weighted average favoring recent readings

This experiment will focus on how averaging affects mood stability and
response time during sudden changes.

### Experiment #3 - Increasing Mood labels
Planned comparison:
- 2 mood labels (Same as before)
- 3 mood labels (Adding more in-between calm and chaotic)
- 4 mood labels (Adding more in-between calm and chaotic)

This experiment will show me how many mood labels is too many labels. It will also show me how many labels will cause an issue when human input is taken.
  
## Open Problems
- What is a good window size for the averaging?
- Defining what counts as a “sudden change”
- Deciding how to measure responsiveness without real hardware or code
- Avoiding over-smoothing important changes
  
## Notes & Observations
- Experiment 2 taught me a lot about how the different methods (no averaging, simple averaging, and weighted averaging) would affect accuracy and responsiveness, especially when mood flips were involved. No averaging produced a very stable and quick response, but it is affected greatly by reading noise. Simple averaging reduced noise, but introduced a very high amount of latency, meaning that all of the mood labels were the incorrect mood. Finally, using weighted averaging reduced noise just as simple averaging did, but also had less latency, with at least one of the data points being the correct mood in all of the tests. This showed me that using a weighted average would be the most logical choice for this scenario.
  
## End-of-Week Reflection (to be completed later)
- What worked:
- What didn’t:
- What surprised me:
