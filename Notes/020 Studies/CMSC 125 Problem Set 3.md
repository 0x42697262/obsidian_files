CMSC 125 Problem Set 3
**Topic Coverage**: Processor Management

---

### 1. Give an event in the system that wil initiate the following transitions:
	a. dispatch
	b. preempt
	c. block
	d. wakeup

> [!INFO]- Answer
> 

### 2. Consider the following set of processes, with the length of the CPU-burst time (time a process will use the CPU for a single time) given in milliseconds:
| Process | Burst Time | Priority |
| ------- | ---------- | -------- |
| P1      | 10         | 3        |
| P2      | 1          | 1        |
| P3      | 2          | 3        |
| P4      | 1          | 4        |
| P5      | 5          | 2         |
^uE5fFx

Processes are assumed to have arrived in the order P1, P2, P3, P4, P5, all at time 0.

	a. Draw four Gantt charts illustrating the execution of these processes using FCFC, SJF, a nonpreemptive priority (a smaller priority number implies a higher priority), and round-robin (assume quantum=1) scheduling.
	b. What is the turnaround time of each process for each of the scheduling algorithms?
	c. What is the waiting time of each process for each of the scheduling algorithms?
	d. Which of the schedules in part (a) results in the minimal average waiting time (overall processes)?

> [!INFO]- Answer
> 

### 3. Five jobs are waiting to be executed. Their expected running time, priority and deadline are as follows:
|     | t   | p   | d   |
| --- | --- | --- | --- |
| j1  | 10  | 4   | 15  |
| j2  | 8   | 2   | 10  |
| j3  | 4   | 1   | 15  |
| j4  | 6   | 3   | 10  |
| j5  | 5   | 5   | 12    |
^bL0v7u

In what order should they be run to minimize:

	a. mean response time
	b. mean weighted response time
	c. maximum lateness

> [!INFO]- Answer
> 

### 4. Differentiate preemptive from non-preemptive scheduling in terms of when to change the program currently in control of the CPU.

> [!INFO]- Answer
> 

### 5. State the effect of
	a. time slicing; and
	b. increasing the time for one interaction
on the response time of a process.

> [!INFO]- Answer
> 

### 6. The scoring system in high-level scheduling is usually “aged”. Why is there a need to “age” the scores?

> [!INFO]- Answer
> 

### 7. State an undesirable feature associated with each of the following scheduling algorithms:
	a. First-come-first-serve
	b. Shortest job first
	c. Shortest remaining processing time

> [!INFO]- Answer
> 

### 8. valuate the scheduling algorithms:
	a. First-come-first-serve
	b. Shortest job first
	c. Shortest remaining processing time
in terms of the following criteria:
1. CPU utilization
2. throughput
3. turnaround time
4. waiting time

> [!INFO]- Answer
> 
