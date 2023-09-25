## First-Fit
### Initial State
![[Pasted image 20230602164717.png]]

### Final State
![[Pasted image 20230602164730.png]]

### Statistics
![[Pasted image 20230602164804.png]]
In ***First-Fit*** algorithm, the time it takes for the simulation to complete is *23 seconds* on *6.35 jobs per second*. It has an average queue length of *5.43 jobs* per second. And on average, the average waiting time for all the job is *4.04* seconds. Notice that this algorithm have *57.41%* storage utilization on average in the entire simulation. It also has an average of *9167 bytes* of internal fragmentation.

## Best-Fit
### First State
![[Pasted image 20230602165517.png]]

### Final State
![[Pasted image 20230602165532.png]]

### Statistics
![[Pasted image 20230602165539.png]]
In ***Best-Fit*** algorithm, the time it takes for the simulation to complete is *24 seconds* on *6.08 jobs per second*. It has an average queue length of *5.25 jobs* per second. And on average, the average waiting time for all the job is *4.04* seconds. Notice that this algorithm have *55.01%* storage utilization on average in the entire simulation. It also has an average of *7723 bytes* of internal fragmentation.

## Worst-Fit
### Initial State
![[Pasted image 20230602165719.png]]

### Final State
![[Pasted image 20230602165727.png]]

### Statistics
![[Pasted image 20230602165738.png]]
In ***Worst-Fit*** algorithm, the time it takes for the simulation to complete is *27 seconds* on *5.41 jobs per second*. It has an average queue length of *6.22 jobs* per second. And on average, the average waiting time for all the job is *5.6* seconds. Notice that this algorithm have *48.90%* storage utilization on average in the entire simulation. It also has an average of *10365 bytes* of internal fragmentation.


# Summary

| **Algorithm**   | Time Finished | Average Jobs Processed | Average Queue Length | Average Waiting Time | Storage Utilization | Internal Fragmentation | Percentage Partitions Heavily Used | Percentage Partitions Never Used |
| --------------- | ------------- | ---------------------- | -------------------- | -------------------- | ------------------- | ---------------------- | ---------------------------------- | -------------------------------- |
| ***First-Fit*** | 23s           | 6.35 jobs              | 5.43 jobs            | 4.04s                | 57.41%              | 9167 bytes             | 50%                                |         0%                         |
| ***Best-Fit***  | 24s           | 6.08 jobs              | 5.25 jobs            | 4.04s                | 55.01%              | 7723 bytes             | 50%                                |          0%                        |
| ***Worst-Fit*** | 27s           | 5.41 jobs              | 6.22 jobs            | 5.6s                 | 48.90%              | 10365 bytes            | 60%                                |           10%                       |
Based on this results, ***First-Fit*** has the most storage utilization and jobs processed. ***Best-Fit*** on the other hand is optimized for using lower internal fragmentation and also have lower queue length in average. Based on this small simulation, we can infer that ***First-Fit*** is the best algorithm for getting higher throughput however at the cost of internal fragmentation. But ***Best-Fit*** is the best algorithm for saving more storage space in the memory or most efficient algorithm in terms of memory usage.
**Claims:**
- First-Fit has the highest jobs processed per second and lowest waiting time.
- Best-Fit have the  most efficient internal fragmentation.
- Worst-Fit is just bad.
- Having lower average queue length would mean more jobs are being processed which makes it better.

In order to prove these claim, I created another simulation with different data sets. And  here are the table of results:

| **Algorithm**   | Time Finished | Average Jobs Processed | Average Queue Length | Average Waiting Time | Storage Utilization | Internal Fragmentation | Percentage Partitions Heavily Used | Percentage Partitions Never Used |
| --------------- | ------------- | ---------------------- | -------------------- | -------------------- | ------------------- | ---------------------- | ---------------------------------- | -------------------------------- |
| ***First-Fit*** | 57s           | 21.75 jobs             | 27.32 jobs           | 11.992s              | 40.70%              | 179,574 bytes          | 25%                                | 0%                               |
| ***Best-Fit***  | 57s           | 21.75 jobs             | 27.42 jobs           | 12.04s               | 40.70%              | 184,276 bytes          | 9.38%                              | 0%                               |
| ***Worst-Fit*** | 57s           | 21.75 jobs             | 27.44 jobs           | 12.048s              | 40.70%              | 185,048 bytes          | 31.25%                             | 0%                                 |
The data set used have 32 memory blocks and 125 jobs. It appears that these results does not reflect on to my claims since the internal fragmentation for First-Fit is smaller than Best-Fit.

I made another simulation with different data set to further test the differences between the algorithms. This uses 125 jobs and 32 memory blocks however the memory blocks are of equal sizes. Blocks 1-12 are equal and blocks 13-32 are equal. The same values of jobs are used on this simulation.

| **Algorithm**   | Time Finished | Average Jobs Processed | Average Queue Length | Average Waiting Time | Storage Utilization | Internal Fragmentation | Percentage Partitions Heavily Used | Percentage Partitions Never Used |
| --------------- | ------------- | ---------------------- | -------------------- | -------------------- | ------------------- | ---------------------- | ---------------------------------- | -------------------------------- |
| ***First-Fit*** | 58s           | 18.33 jobs             | 41.60 jobs           | 9.864s              | 43.98%              | 78,005 bytes          | 28.12%                                | 0%                               |
| ***Best-Fit***  | 59s           | 18.02 jobs             | 40.58 jobs           | 9.552s               | 43.24%              | 74,649 bytes          | 6.25%                              | 0%                               |
| ***Worst-Fit*** | 58s           | 18.33 jobs             | 41.60 jobs           | 9.864s              | 43.98%              | 78,005 bytes          | 28.12%                             | 0%                                 |

I noticed that First-Fit and Worst-Fit are exactly the same because the partitions for the memory blocks are already ordered. If the memory block partitions where to be at random points then maybe there would be a different result. Best-Fit still leads in having the lowest internal fragmentation.


This time, the memory blocks are randomly scattered. The purpose of this simulation is to test First-Fit against Worst-Fit

| **Algorithm**   | Time Finished | Average Jobs Processed | Average Queue Length | Average Waiting Time | Storage Utilization | Internal Fragmentation | Percentage Partitions Heavily Used | Percentage Partitions Never Used |
| --------------- | ------------- | ---------------------- | -------------------- | -------------------- | ------------------- | ---------------------- | ---------------------------------- | -------------------------------- |
| ***First-Fit*** | 56s           | 18.98 jobs             | 40.75 jobs           | 9.136s              | 45.55%              | 74,993 bytes          | 46.88%                                | 0%                               |
| ***Best-Fit***  | 59s           | 18.02 jobs             | 40.58 jobs           | 9.552s               | 43.24%              | 74,649 bytes          | 6.25%                              | 0%                               |
| ***Worst-Fit*** | 58s           | 18.33 jobs             | 41.60 jobs           | 9.864s              | 43.98%              | 78,005 bytes          | 28.12%                             | 0%                                 |
With this data, it appears that First-Fit tries to get closer to Best-Fit's internal fragmentation value. This does not imply that Best-Fit is the best algorithm however we can claim that when both the job and memory blocks perfectly aligns each other when being allocated would have the best result.

Another test is made with exact job memory size and memory blocks with random sizes. A fixed job size of 10,000 bytes.

| **Algorithm**   | Time Finished | Average Jobs Processed | Average Queue Length | Average Waiting Time | Storage Utilization | Internal Fragmentation | Percentage Partitions Heavily Used | Percentage Partitions Never Used |
| --------------- | ------------- | ---------------------- | -------------------- | -------------------- | ------------------- | ---------------------- | ---------------------------------- | -------------------------------- |
| ***First-Fit*** | 78s           | 16.04 jobs             | 38.62 jobs           | 24.096s              | 30.52%              | 218,866 bytes          | 34.38%                                | 40.62%                               |
| ***Best-Fit***  | 78s           | 16.04 jobs             | 38.62 jobs           | 24.096s               | 30.52%              | 214,558 bytes          | 34.38%                              | 40.62%                               |
| ***Worst-Fit*** | 78s           | 16.04 jobs             | 38.62 jobs           | 24.096s              | 30.52%              | 221,052 bytes          | 34.38%                             | 40.62%                                 |
Based on this simulation, it appears that only the internal fragmentation has differed and Best-Fit was able to achieve the most efficient way in fitting the job sizes. This simulation have jobs that are not allocated. Which is why a final simulation is necessary.

This time, all the jobs are allocatable to the memory blocks. Job size at 500 bytes.

| **Algorithm**   | Time Finished | Average Jobs Processed | Average Queue Length | Average Waiting Time | Storage Utilization | Internal Fragmentation | Percentage Partitions Heavily Used | Percentage Partitions Never Used |
| --------------- | ------------- | ---------------------- | -------------------- | -------------------- | ------------------- | ---------------------- | ---------------------------------- | -------------------------------- |
| ***First-Fit*** |  51s          | 24.53 jobs             | 29.61 jobs           | 12.08s              | 2.33%              | 390,932 bytes          | 3.12%                                | 0%                               |
| ***Best-Fit*** |  51s          | 24.53 jobs             | 29.61 jobs           | 12.08s              | 2.33%              | 384,089 bytes          | 3.12%                                | 0%                               |
| ***Worst-Fit*** |  51s          | 24.53 jobs             | 29.61 jobs           | 12.08s              | 2.33%              | 393,853 bytes          | 3.12%                                | 0%                               |
As you can see, Best-Fit were able to function as the most efficient algorithm in terms of internal fragmentation.
# Conclusion
 So, therefore, one algorithm is better than other depending on the approach or problem to solve. If the target is to achieve the highest amount of jobs being processed, then ***First-Fit*** is the algorithm to use. If memory space efficiency is necessary, then ***Best-Fit*** algorithm is the best to use. One method is not better than one another except Worst-Fit as it is literally the worst algorithm to use. I would recommend using ***Best-Fit*** as much as possible compared to First-Fit because the time  difference to complete a task is minimal and Best-Fit optimizes more on internal fragmentation which allows the operating system to process more jobs. Going back to the explanations I mentioned above, each algorithms does not hold true in all cases which is why I tested the algorithms with different data sets and this proves the point that each algorithms has its strong points and weak points.