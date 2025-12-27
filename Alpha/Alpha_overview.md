# QUESTIONS:
  - How will it find the best fit?
    - ANSWER: We will use a graph, and find the closest point (or use a different method to find it)
  - Could I use the line of best fit, or is that different?
    - ANSWER: Even if the line of best fit works (which I don't think it would), I think using a graph and distances would be the best way to do it
  - How much data does it need to be accurate?
    - ANSWER: I think that taking three measurements in a row, and taking the average, will be the best method
  - Could I make it so it shows a graph?
    - ANSWER: This poses a problem because showing a graph for more than 3 dimensions is hard, but this doesn't matter if I don't need to show it, since the computer can do it with no problem!
  - How many sensors do I need for an accurate reading?
    - ANSWER: 3-5 sensors would work best, having at least a light sensor, noise sensor, and motion sensor
  - How much will small fluctuations in readings affect it (will they add up)?       
  - How can I make it so constant stuff (white noise, light on in the room, someone walking) doesn't affect it too much
  - What sensors do I need to get that data?
    - ANSWER: a light sensor, noise sensor, and motion sensor are needed
  - Would using nearest neighbor data or weighted data be more efficient
  - Would the noise affect the end result? How could I overcome that

# SPECIFIC RESEARCH:
  - to classify as an AI, it should learn from its past runs
  - Instead of looking for the best fit of data, I could have it graph the points (maybe on a 3D graph depending on the amount of data), and then find the closest point (CALL THIS Alpha.01)
  - Although the system uses multiple sensor inputs, the data is not VISUALIZED in higher dimensions. Each reading is treated as a vector in feature space, and similarity is calculated mathematically. Graphs are used only for human interpretation
  - An AI is something that isn't just doing a set program, it needs to learn from the data provided and reach its own end point
  - If I make an AI, I have to give it data at first, I can't just make it a bunch of if else commands, and it has to get better as it is used more 
  - An AI learns from data
  - A basic AI learns from data, recognizes PATTERNS, and makes predictions. (The pattern part is what I want to focus on in this project)
  - The computer can make a graph of infinite dimensions, only humans need the visuals
  - 3-5 sensors are best
  - I should use data voting and clustering (I don't know what that is yet) to get more accurate results (Alpha.02)
  - To reduce noise, I could average three data points that were taken in a row, which will smooth out the data. However, if there is a sudden change in the room (someone turns off the lights) there will be some latency and the data will be not as accurate.
  - A better way to do this would be to use weighted averages (giving more recent data more "weight"). This would improve stability with the cost of a small increase in latency. (Alpha.03)


# PROBLEMS:
  - I don't know how to compare different data sets, especially because they are comparing different units/subjects
  - I can't use line of best fit, since different moods could produce the same answer ([L:10, N:20, M:10] and [L:10, N:10, M:20])
  - I want to make sure that it is a form of AI, no matter how basic, but I do not really understand the distinctions
  - For Alpha.01, I would need to figure out how to graph the points, and I do not know if that is possible yet
  - For Alpha.01, I want to make sure that it  would find the most correct solution, so finding the closest point may not be enough
  - For Alpha.01, if the human tells it the wrong mood, it will mess up the rest of the data. I need to take the most average data I think
