
CMSC 125 Problem Set 1  
**Topic Coverage**: Introduction

----

1) An extreme method of spooling, known as staging a tape, is to read the entire contents of a magnetic tape onto disk before using it. Discuss the main advantages of such a scheme. 


2) What is the main advantage of multiprogramming?


3) We have stressed the need for an operating system to make efficient use of the computing hardware. When is it appropriate for the operating system to forsake this principle and *waste* resources? Why is such a system not really wasteful?


4) A time-sharing system is to be designed to support a large number of users. What possible considerations can influence the choice of the time slice? Justify each consideration.


5) Define the essential properties of the following types of operating systems:
```
a) Batch
b) Interactive
c) Time-sharing
d) Real-time
e) Distribute
```

6) How does automatic job sequencing reduce job set-up time?

7) Explain how response time (time interval from the first time the job was submitted for execution to the first time it is allocated the CPU) is reduced by allowing time-sharing.


8) Given the following characteristics of a single-user system: 
```
Card reader   600 cards/minute  
Line printer  100 lines/minutes  
CPU             1 μsec/instruction
```
and suppose that it takes 1,000 instructions to process each line of input and produce one line of output. Compute the efficiency of the system in terms of:
```
a.) CPU utilization
b.) Input and output device utilization (in milliseconds)
```
Show your computations.

9) Explain how throughput (number of completed jobs per unit time) is increased by doing input/output operation in an off-line manner.

10) Differentiate
```
a) Batch OS
b) Multiprogramming OS
c) Time-sharing OS
```
in terms of throughput and response time.