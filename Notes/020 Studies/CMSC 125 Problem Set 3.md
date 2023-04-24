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
>a. **Dispatch**: Dispatch occurs when a process is selected by the scheduler to be executed on the CPU. This can be initiated by various events such as the completion of a previous process, a timer interrupt, or the arrival of a new process.
>
>b. **Preempt**: Preemption occurs when a running process is interrupted and its execution is paused, allowing another process to run. This can be initiated by various events such as a higher priority process becoming ready to run, a time slice expiring, or an I/O operation completing.
>
>c. **Block**: Blocking occurs when a process is unable to proceed with its execution and is put into a waiting state. This can be initiated by various events such as a request for I/O or a semaphore, a synchronization operation, or a resource allocation failure.
>
>d. **Wakeup**: Wakeup occurs when a blocked process is signaled to resume its execution. This can be initiated by various events such as the completion of an I/O operation, a semaphore release, or a timer expiration.

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

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

	a. Draw four Gantt charts illustrating the execution of these processes using FCFS, SJF, a nonpreemptive priority (a smaller priority number implies a higher priority), and round-robin (assume quantum=1) scheduling.
	b. What is the turnaround time of each process for each of the scheduling algorithms?
	c. What is the waiting time of each process for each of the scheduling algorithms?
	d. Which of the schedules in part (a) results in the minimal average waiting time (overall processes)?

> [!INFO]- Answer
> 

**a)**
FCFS:
![[Pasted image 20230424200038.png]]

SJF:
![[Pasted image 20230424211535.png]]

Priority (Nonpreemptive):
![[Pasted image 20230424213723.png]]

Round-Robin:
![[Pasted image 20230424220351.png]]

**b)**
FCFS: 
`P1` = 10ms; `P2` = 11ms; `P3` = 13ms; `P4` = 14ms; `P5` = 19ms;
```matlab
(10 + 11 + 13 + 14 + 19) / 5 = 67 / 5 = 13.4
```
Turnaround time: `13.4` ms

SJF:
`P1` = 19ms; `P2` = 1ms; `P3` = 4ms; `P4` = 2ms; `P5` = 9ms;
```matlab
(19 + 1 + 4 + 2 + 9) / 5 = 35 / 5 = 7
```
Turnaround time: `7` ms

Priority(Nonpreemptive):
`P1` = 16ms; `P2` = 1ms; `P3` = 18ms; `P4` = 19ms; `P5` = 6ms;
```matlab
(16 + 1 + 18 + 19 + 6) / 5 = 60 / 5 = 12
```
Turnaround time: `12` ms

Round-Robin:
`P1` = 19ms; `P2` = 2ms; `P3` = 7ms; `P4` = 4ms; `P5` = 14ms;
```matlab
(19 + 2 + 7 + 4 + 14) / 5 = 46 / 5 = 9.2
```
Turnaround time: `9.2` ms

**c)**
FCFS:
`P1` = 0ms; `P2` = 10ms; `P3` = 11ms; `P4` = 13ms; `P5` = 14ms;
```matlab
(0 + 10 + 11 + 13 + 14) / 5 = 48 / 5 = 9.6
```
Waiting time: `9.6` ms

SJF:
`P1` = 9ms; `P2` = 0ms; `P3` = 2ms; `P4` = 1ms; `P5` = 4ms;
```matlab
(9 + 0 + 2 + 1 + 4) / 5 = 16 / 5 = 3.2
```
Waiting time: `3.2` ms

Priority(Nonpreemptive):
`P1` = 6ms; `P2` = 0ms; `P3` = 16ms; `P4` = 18ms; `P5` = 1ms;
```matlab
(6 + 0 + 16 + 18 + 1) / 5 = 41 / 5 = 8.2
```
Waiting time: `8.2` ms

Round-Robin:
`P1` = 9ms; `P2` = 1ms; `P3` = 5ms; `P4` = 3ms; `P5` = 9ms;
```matlab
(9 + 1 + 5 + 3 + 9) / 5 = 27 / 5 = 5.4
```
Waiting time: `5.4` ms

**d)** SJF since it has an average of `3.2` ms of waiting time.



> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

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

|       | 1   | 2   | 3   | 4   | 5   |
| ----- | --- | --- | --- | --- | --- |
| MMRT  | j3  | j5  | j4  | j2  | j1  |
| WMMRT | j5  | j4  | j1  | j3  | j2  |
| MML   | j4  | j2  | j5  | j3  | j1  | 
^KtSyxi

> [!INFO]- Source
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 4. Differentiate preemptive from non-preemptive scheduling in terms of when to change the program currently in control of the CPU.

> [!INFO]- Answer
>Preemptive and non-preemptive are two types of CPU scheduling algorithms.
>
>In preemptive scheduling, the currently running process can be interrupted by the scheduler to allocate the CPU to another process. The scheduler decides when to preempt the currently running process based on the scheduling algorithm. For example, in a preemptive round-robin scheduling, each process is given a time slice, and once the time slice expires, the scheduler preempts that process and gives another process a chance to run.
>
>In non-preemptive scheduling, once the CPU is allocated to a process, the process keeps the CPU until it releases the CPU either by terminating or switching to the waiting state. The scheduler cannot preempt the currently running process. For example, in first-come first-serve scheduling, the process that requests the CPU first is allocated the CPU and keeps it until it completes or waits for an I/O.> 

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.

### 5. State the effect of
	a. time slicing; and
	b. increasing the time for one interaction
on the response time of a process.

> [!INFO]- Answer
> a. The effect of time slicing on the response time of a process depends on how the time slices are allocated. If the time slices are too short, a process may not be able to complete its task within a single time slice, which will result in an increase in the response time of the process. On the other hand, if the time slices are too long, a process may monopolize the processor, resulting in other processes experiencing longer response times.
>
>b. Increasing the time for one interaction can have different effects on the response time of a process, depending on the nature of the process.
>
>In some cases, it may result in a longer response time for the process overall. This can happen when the process depends on a series of interactions, and increasing the time for one interaction increases the total time required for the process.
>
>So, basically, the shorter the time slice the faster the response time. This is because the process will get its share of the CPU faster if the time slice is small compared to when it's large.
>

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 6. The scoring system in high-level scheduling is usually “aged”. Why is there a need to “age” the scores?

> [!INFO]- Answer
> Scores are aged to prevent starvation of lower-priority processes. As time passes, the scores of waiting processes increase, giving them a better chance to be scheduled and to be processed by the CPU. This prevents a process from being stuck in a perpetual hold.

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 7. State an undesirable feature associated with each of the following scheduling algorithms:
	a. First-come-first-serve
	b. Shortest job first
	c. Shortest remaining processing time

> [!INFO]- Answer
> a. FCFS - Can lead to long waiting times for short processes behind long ones.
> b. SJF - Can lead to job starvation for longer jobs.
> c. SRPT - Can lead to frequent preemptions and more overhead, and longer jobs are at even worse disadvantage.

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 8. Evaluate the scheduling algorithms:
	a. First-come-first-serve
	b. Shortest job first
	c. Shortest remaining processing time
in terms of the following criteria:
1. CPU utilization
2. throughput
3. turnaround time
4. waiting time

> [!INFO]- Answer

|      | CPU Utilization | Throughput | Turnaround Time | Waiting Time |
| ---- | --------------- | ---------- | --------------- | ------------ |
| FCFS | Low             | Low        | High            | Long         |
| SJF  | High            | High       | Low             | Short        | 
| SRPT | Very High            | Very High       | Low             | Short        |
^LQLtDu

**Explanation:**
a. First-come-first-serve (FCFS):

`CPU utilization`: FCFS has low CPU utilization as it does not prioritize short processes over long processes.
`Throughput`: FCFS has low throughput as long processes can block the CPU, leading to slower processing of other processes.
`Turnaround time`: FCFS has high turnaround time as longer processes are given preference over shorter ones, leading to longer waiting times for shorter processes.
`Waiting time`: FCFS has high waiting time as shorter processes have to wait for longer processes to complete.


b. Shortest job first (SJF):

`CPU utilization`: SJF has higher CPU utilization as it prioritizes shorter processes over longer ones, allowing the CPU to process more processes in a given time.
`Throughput`: SJF has higher throughput as it prioritizes shorter processes, which reduces the waiting time for shorter processes and allows more processes to be processed in a given time.
`Turnaround time`: SJF has low turnaround time as shorter processes are given priority and processed quickly, leading to shorter waiting times for all processes.
`Waiting time`: SJF has short waiting time as shorter processes are given priority and processed quickly, reducing the time that shorter processes have to wait.


c. Shortest remaining processing time (SRPT):

`CPU utilization`: SRPT has the highest CPU utilization as it dynamically prioritizes processes based on their remaining processing time, allowing the CPU to process more processes in a given time.
`Throughput`: SRPT has the highest throughput as it dynamically prioritizes processes based on their remaining processing time, reducing the waiting time for all processes and allowing more processes to be processed in a given time.
`Turnaround time`: SRPT has low turnaround time as it dynamically prioritizes processes based on their remaining processing time, leading to shorter waiting times for all processes.
`Waiting time`: SRPT has short waiting time as it dynamically prioritizes processes based on their remaining processing time, reducing the time that processes have to wait.

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.