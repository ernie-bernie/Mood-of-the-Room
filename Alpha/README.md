# Alpha – Early Prototype

This folder contains early research, problems, questions, and design notes for the
Mood of the Room project. The goal of Alpha is to explore ideas, identify
problems, and iterate on solutions before formal implementation.

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
- Alpha - -A program that uses data that was previously given to find which one(s) best fit the current data(what is currently going on in the room(No clear method to find that yet)
- Alpha.01 – Basic nearest-point classification. Finds the nearest neighbor on a graph, then uses that mood
- Alpha.02 – Instead of comparing only one point, it will compare with many points and use data voting to find the best mood
- Alpha.03 - I will average three data points taken in a row to reduce noise and smooth out the data(This could pose a problem such as if someone turns off a light last second)
- Alpha.04 - I will now use a WEIGHTED average of points in a specific window. This ensures that the data is basically noiseless, and will make it so that sudden changes dont ruin the data
- 

## Problems & Limitations
- Mood labels are subjective
- Sudden changes are delayed by averaging
- Limited sensor diversity

## Next Steps
- Test different averaging window sizes
- Compare weighted vs simple moving averages
- 
