
CMSC 125 Problem Set 1  
**Topic Coverage**: Introduction

----

1) An extreme method of spooling, known as staging a tape, is to read the entire contents of a magnetic tape onto disk before using it. Discuss the main advantages of such a scheme. 

Magnetic tapes are slow, unreliable, and serial. Unlike disks which is faster, more reliable, can processes jobs in parallel, and has better data management than magnetic tapes. That is because magnetic tapes takes longer time to locate and retrieve data because its sequential unlike disks which is a random-access device so the tape will have to be rewinded at the very beginning in order to locate for the specific data. Magnetic tapes are much more prone to errors and data loss unlike disks. Also, disks can process in parallel as there is no need for I/O when data is being processed. So, many jobs can access the data simultaneously. And disk can also have features such as searching and sorting unlike magnetic tapes. Which is why staging a tape onto a disk is much better and simpler.

Although staging the tape onto the disk has issues with higher startup time and lots of storage space required but the advantages outweighs these disadvantages.

2) What is the main advantage of multiprogramming?

Multiprogramming allows the processor to be on active state rather than being idle because when a job is in waiting stage, the processor will have to idle. To avoid that, the processor proceeds on to the next task that does not require I/O operations so the processor will never be idle. This is ideal when there are multiple jobs to be processed and I/O is busy. Allowing the processor to have faster response time and increased utilization of system resources.

Basically allowing multiple jobs to be executed concurrently in one processor so mutiple jobs are ran simultaneously. Although there is no true parallel processing, just the processor switching jobs very quick.









3) We have stressed the need for an operating system to make efficient use of the computing hardware. When is it appropriate for the operating system to forsake this principle and *waste* resources? Why is such a system not really wasteful?

It is incorrect to say that resources are "wasted" when actually what happens is using a portion of the resource is used for another benefit. Such benefits is redundancy for reliability of storage data and security to ensure protection of the system. In providing better reliability by doing backups in a storage system, resource is "wasted" when those remaining storage space can be used for another data however that's not being wasteful but instead that is providing more reliability to the system by having backups. This backup can be used in such time when the main storage gets corrupted. As for security, cryptography and other security mechanisms requires cpu processing power which requires resources to be allocated, we can say that it's "wasteful" but that is still incorrect as no resource is truly wasted. When security is ensured, reliability of the system is increased.

A popular saying in the world in field of medicine, prevention is better than cure. So, when a prevention method such as providing backup to systems and configuring security mechanisms, this allows us to be completely safe from major catastrophe but instead only have annoyances when it happens. Which is why such systems are not considered **wasteful** at all cost.


4) A time-sharing system is to be designed to support a large number of users. What possible considerations can influence the choice of the time slice? Justify each consideration.

There are five influences that should be considered in the choice of a time slice. These are workload, throughput, responsiveness, overhead, and fairness. 
In a workload, a lower workloads would benefit from having longer time slice and higher workloads would benefit from shorter time slice because higher workloads would be in a state of multiple users using the host computer so a shorter time slice would be far efficient.
In a throughput, it should depend on which duration is much more beneficial but too short of a throughput would lead to no processed data. So, if possible, balance is better.
In responsiveness and overhead, having short time on responsiveness would be better but having too short would mean higher overhead. Every time there is a switch of job, there is always an overhead resource that is being used, so higher time slice would be lower overhead and shorter time slice would be higher overhead. 
Then lastly, fairness, each user should have a balanced and fair time slice based on the amount of CPU time regardless of the workload or priority. So, even if a process or job takes too much cpu time but has shorter time slice would lead to an ineffecient approach in a time-sharing system.








5) Define the essential properties of the following types of operating systems:
```
a) Batch
b) Interactive
c) Time-sharing
d) Real-time
e) Distribute
```
**Batch**:
- Designed to process large amount of jobs in a batch mode without user interaction. It is like being automated. Which is then processed one job at a time so that the processor will not sit idle and then able to utilize the resources efficiently.
**Interactive**:
- Designed to support user interaction mainly through a graphical user interface. This operating system is optimized for the interactivity of the user, so user experience and responsiveness is critical. This is like multiprogramming since processes are switched so fast that a user cannot notice the difference so this operating system acts like processes are ran simultaneously.
**Time-sharing**:
- Designed to support multiple users with one host computer by allocating the resources needed for each user. Since resources are shared amongst other users, a time slice is provided for each user to process their jobs or execute programs. Then after a user finishes their time slice, it then switches to another user and so on. This operating system is optimized for efficiency and fairness where utilization of system resources is critical to ensure interactive environment to its users.
**Real-time**:
- Designed to provide real time computing by prioritizing responsiveness. In this operating system, responsiveness is critical because of critical tasks. So, when jobs are executed, it must be within a specific time constaint so that a quick response to it can be processed. If failures occurs, there must be an instant response so a mechanism is fundamental for handling errors and failures. This operating system must be critically responsive and reliable at all times.
**Distribute**:
- Designed to manage a network of computers like a single system that provides users access to shared resources. This operating system increases the computation speed, functionality, data availability, and reliability. 




6) How does automatic job sequencing reduce job set-up time?

Automatic job sequencing is a technique used  by batch operating systems that automates the processing of job sequencing and resource allocation. This removes the slow input (human) from the process by changing the input process to automation by the system. Since batch operating system performs well on a fully utilized system with few idle times, the automation is one of its critical aspect in handling the input process. Humans are prone to error, mistakes, failures, and sometimes even distractions leading to slower input processing speed. 

So, with automatic job sequencing where no humans is required to handle the input process, the setup time is now a lot faster than before.

7) Explain how response time (time interval from the first time the job was submitted for execution to the first time it is allocated the CPU) is reduced by allowing time-sharing.

Each user using the host system is allocated a time to use the host system's resources, this is called time-slicing. With this, the processor switches tasks very rapidly giving the illusion of having a fast response time and highly interactive environment. This would the help users interact in real-time and get quick feedback, making system faster and responsive. Jobs get quick allocation of resources of the processor after being inputted by the user, thus reducing the response time. Sharing processor can also improve throughput by avoiding waste of processor cycles on idle tasks.


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

Input/Output (I/O) operations are slow so by adressing addressing the issue to a solution by doing offline processing, it is possible to efficiently utilize the system's resources. This happens by doing I/O in the background while the processor focuses on executing jobs Since the I/O process is done in an offline manner, the processor can continue executing other jobs that it needs to execute thus overall reducing the idle time and increasing the throughput. This type of processing also reduces the overhead of the system because I/O operations can be batched together thus further increases its processing speed.

10) Differentiate
```
a) Batch OS
b) Multiprogramming OS
c) Time-sharing OS
```
in terms of throughput and response time.

**Batch OS**:
- Optimized for throughput rather than response time because its purpose is to process jobs one after another automatically. This is because time is not a critical factor which does not require fast response time.
**Multiprogramming OS**:
- Optimized for balancing between throughput and response times because there are multiple jobs running in the system that rapidly switches between jobs. It has lower throughput than batch operating systems.
**Time-sharing OS**:
- Optimized for instantaneous response time for better interactive environment between multiple users in a single host system thus response time is prioritized over throughput causing it to have lower throughput but very high response time.

In short, use batch operating system for a maximum efficient throughputs, time-sharing operating system if user interaction is prioritized due to response time, and multiprogramming for a balance between the two.