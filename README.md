# Mood-of-the-Room
**Started:** 12/25/2025  
**Grade:** 8th Grade

## Project Structure:
 - [Alpha](Alpha) - Best idea/Idea #1 overview, my research, questions, and problems are in [Alpha_overview](Alpha/Alpha_overview.md)
 - [Developing Journal](Developing_Journal) - Where I log my progress weekly
 - [Alpha Experiments](Alpha/Alpha_Testing_and_Experiments.md):
   - Experiment #1 - Distance-based voting using Manhattan distance

## PRE-PROJECT ANALYSIS:

  ### Project Question:
      - Can a computer infer the emotional "mood" of a physical space using only simple sensor data? 
  ### Why I want to do this:
      - I want to explore AI models and see how accurately a computer can detect something that is usually limited to animals.
      - This is my way to explore how code can perform a task which is primarily done by humans. I have never looked into what classifies something AI, so I think researching this project will teach me a lot, so I am excited. 
      - Also, understanding environments through data has applications in smart buildings, accessibility, and human-centered AI, so this can help me in the future.
  ### My goals for this project:
      - Research ways to take measurements on different aspects of the room, such as noise level, light level, and movement.
      - Use a data-driven model (initially rule-based or distance-based, later potentially machine-learning-based) to infer room mood from sensor readings.
      - Test in a variety of atmospheres and areas, seeing what will affect the output, either in a positive or negative way.
      - Write an entry on my progress, what I learned, what failed, and my next steps (will try to do weekly).
      - I want to explore simple AI models that can detect patterns in sensor data. I need to look into that.
      - Even if the final system is incomplete, my primary goal is to learn through experimentation.
      - An added bonus would be to add a confidence rating, so the human knows how confident the program is
      - I also want to experiment with my weighted average to see if it makes a huge difference. During the testing stages, I would try to compare the inferences of when the program averaged the data to when it didn't. This will show me how accurate it is, and how much reducing noise can help the final result.

  ### What I want to learn:
      - I know that something called signal noise is involved, but don't know what it is, so learning that is a must
      - I want to learn about AI models and what makes them up, I want to see if I can make some simple ones
      - I want to explore heuristics, and I want to see if I can make an AI incorporate a few of them

  ### Limitations:
      - I am in school doing lots of extracurriculars, so time might be an issue
      - I do not want to spend a lot of money on this, so I will have to try to get most things from previous projects (Arduino from motion sim?)
      - I don't know much about AI models, so this project will be challenging for me
      - Mood labels are subjective, so the data might not be completely "accurate", if accurate is a thing here
      - Noise could distort the data and readings, so I have to overcome that

## MID-PROJECT AND POST-PROJECT ANALYSIS:
  ### What I learned:
    - I learned about something called noise in the data. I found out that this is basically just random changes or electrical interference that change the true data. To overcome this, I think that averaging three sets of data taken consecutively would smooth out the data and reduce noise. However, after looking into this a bit more and thinking of different scenarios, I came across one major trade-off. This is that averaging could potentially introduce latency, which is a delay in the response. For example, if someone turns off the lights suddenly while the readings are being taken, then the data would not reflect light or dark, but somewhere in between, skewed to one side. This could pose an issue.
    - I learned that instead of just taking the average of the points, using a moving average filter would significantly improve accuracy, since then it will give the most recent point the most influence in the final result, meaning if someone turned off the light last second, it will lean more towards the "dark side"
    - I also learned that there is often a trade-off between stability and responsiveness, and that engineering decisions require balancing both.
    - I learned that there are different methods to measuring distances between data points, such as the Manhattan and Euclidean methods. For this project, I concluded that using the Manhattan method would work best, since I found that the Euclidean is very sensitive to a spike or sudden fluctuation in the data, while the Manhattan method is not as sensitive.
    - I learned that to reduce the error margin, I should incorporate data voting, with around 3 points voting for this project. This will reduce the error caused by incorrect human input and label noise, so there is usually a more accurate response


**Detailed plans, experiments, and next steps are documented in the Developing Journal.**
