# Week #1, 12/25/25-01/01/26
### This repository currently reflects the research and design phase. Code implementation will begin once core assumptions and approaches are validated
## Goals for this week:
  - I want to keep this week's focus on researching, particularly on AI models and how I can make one.
  - I want to brainstorm a few ideas for what framework I can use.
  - I want to see what stuff I would need to overcome
  - I want to edit my best idea, making more and more iterations, finalizing an idea by the end of the week

## IDEAS:
  - IDEA #1 (We'll call it "Alpha"):
    - Make a program that uses data that was previously given to find which one(s) best fit the current data(what is currently going on in the room)
    - It will then use the best fit of data to provide the mood of the current room
    - It will ask the person in the room how accurate its assumption was, and if accurate, will then store the data for future reference
    - Eventually will not only tell the mood when asked, but will update every minute or so
    - Eventually will also store the results even if it was not right, so it will know what not to do

  - IDEA #2 (We'll call it "Beta"):
    - Make a program (not AI) that will use already given formulas to output the mood of the room (if all measurements are low, it is calm)
    - This will not store more data on if it was correct or not, but the formulas will be updated as time goes on
    - This can also be done automatically
    - Would be easier (BUT IS LAME)
    - Could use as backup plan...we shall see

## Open Challenges This Week:
- I do not know how to compare different data sets with different units
- I do not know if graphing high-dimensional data is possible yet
- I do not know if nearest neighbor is enough
- I do not know about data clustering yet
- I do not know what qualifies as AI
- There are different ways to measure the distance, I need to look into that
- I do not really know what k-NN is and how voting works
- What if there is a split in the votes, or if the program is uncertain? Would forcing a mood or saying that it is uncertain be better? I need to look into that
- 
  

## OVERVIEW OF WEEK:
- I had thought of two separate ways to infer the mood of the room, finding the nearest neighbor on a graph, or by using some weighted distances. (write if you chose and how u chose it)
- I realized that instead of trying to visualize this, I should trust that the computer can "visualize" it by itself, and I should focus on refining data and the other logistical stuff
- I now understand that instead of making a set program, I need to make something that "grows" and learn through time to be considered an AI
- This week, I created many different versions of Alpha, and eventually ended on using (put version of alpha)
- I do not know if k=3 or k=5 will work better, I think that starting with 3 would be best, maybe testing and comparing k=5 I realized that I cannot just use the data straight from the sensors, but should instead normalize it by doing min-max normalization (Linear scaling)
- I decided on using Manhattan distance because it treats each sensor contribution independently and is less sensitive to large deviations in a single sensor channel.
- To handle label noise (and wrong user input), I think that using multiple neighbor voting would work best, as this will make it so one wrong data point will not affect it too much
- Data voting would be good to use, as it will reduce noise and choose the best option. For now, I think using 3 votes would be best (Non-weighted, I can incorporate that later if needed)
- Experiment #1 showed me the need of a safeguard to overcome the issue of the system defaulting to the closest label even when it is not correct. I believe that either adding an "uncertain" option for the program to choose or adding a confidence rating would counteract this, as then the program is not forced to choose a label that could be incorrect without a warning. I could just add many more moods, as then there would most likely be a valid option to choose.
- Experiment #1 was very succesful in my opinion, as it revealed an issue in the process while also validating some of my other methods. It showed me that k=3, k=4, and k=5 all produce stable answers, so I can pick one of those when the time comes.
- 

## NEXT STEPS:
- Decide what version of Alpha will be the first implementation
- Figure out what k should equal
