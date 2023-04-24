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
