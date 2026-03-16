# Code

This folder contains the implementation of the **Mood of the Room** model.

The goal of this stage of the project is to translate the algorithm developed during the research phase into working code.

## Model Overview

The system works in several steps:

1. Collect recent sensor readings (light, noise, motion)
2. Apply **weighted averaging** to reduce sensor noise
3. Compute **Manhattan distances** between the current reading and stored labeled data points
4. Use **k-nearest neighbor voting** to classify the room mood
5. Output the predicted mood along with a **confidence score**

## Mood Labels

The system currently supports three mood labels:

- Calm
- Medium
- Chaotic

## Confidence

Confidence is calculated using the **distance gap** between:

- the predicted class
- the runner-up class

A larger gap indicates a more confident prediction.

## Current Status

This folder currently contains prototype code using simulated data.

The code will be written in Python 3

Hardware integration (real sensors) will be added in a later stage of the project.
