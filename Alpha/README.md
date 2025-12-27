# Alpha – Early Prototype

This folder contains early research, problems, questions, and design notes for the
Mood-of-the-Room project. The goal of Alpha is to explore ideas, identify
problems, and iterate on solutions before formal implementation.

- Main work is in [Alpha_overview.md](Alpha_overview.md)
- Testing and experiments are in [Alpha Testing](Alpha_Testing_and_Experiments.md)

## Research Questions
- Can room “mood” be inferred from sound, motion, and light data?
- How does sensor noise affect classification accuracy?
- Does temporal averaging improve stability?

## Current Approach
- Collect sensor data (sound, motion, light)
- Apply noise reduction using a moving average
- Classify mood by finding the nearest labeled data point
- Use user feedback to improve future predictions

## Versions
- Alpha.00 – A program that uses previously collected data to infer the current state of the room (what is currently going on in the room), right now, there is no clear method to find that yet
- Alpha.01 – Basic nearest-point classification. Finds the nearest neighbor on a graph, then uses that mood
- Alpha.02 – Instead of comparing only one point, it will compare with many points and use data voting to find the best mood
- Alpha.03 - I will average three data points taken in a row to reduce noise and smooth out the data (this could pose a problem such as if someone turns off a light last second)
- Alpha.04 - I will now use a WEIGHTED average of points in a specific window. This significantly reduces noise, and will make it so that sudden changes don't ruin the data
- Alpha.05 - In this version, before using the data collected, I will make sure it is scaled properly by using min-max normalization. This ensures that one data point will not dramatically change the result

## Starting Problems & Limitations
- Mood labels are subjective
- Sudden changes are delayed by averaging
- Limited sensor diversity

## Next Steps
- Test different averaging window sizes
- Compare weighted vs simple moving averages
- 
