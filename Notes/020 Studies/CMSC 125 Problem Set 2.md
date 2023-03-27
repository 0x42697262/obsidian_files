CMSC 125 Problem Set 2  
**Topic Coverage**: Basic OS Concepts

----

1. Why are interrupts necessary in a time-sharing system?
>Interrupts are necessary in a time-sharing system to enable efficient multitasking and prevent a single process from monopolizing the CPU. Interrupts allow the system to switch between multiple processes, giving the appearance of simultaneous execution. Since interrupts suspends the current operation, it can then proceed to the next operation and in this case, it's the user's operations. Which when an operation is completed, it resumes the suspended operation. (Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)

2. Why is it necessary to provide supervisor calls in an operating system? Give an instance wherein such call has to be made
>Supervisor calls, or system calls, are necessary to provide a safe and controlled interface between user programs and the operating system's kernel. This sets some sort of boundary between a user application and the kernel by providing an access control.
>
>For instance, a program might make a system call to request access to a file, which the operating system can then grant or deny based on permissions. Since user applications does not have full access or control to the system and its hardware unlike the kernel. 
>
>(Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)

3. Discuss one problem that is solved by double buffering, but is not properly handled by ordinary buffering.
>Double buffering solves the problem of "tearing" that occurs when the producer and consumer work at different speeds, and the consumer reads data while the producer is still updating it. When the producer and consumer works at different speeds, like having different read, write, and cpu clock, this can cause tearing which is the corruption of the data because while the consumer is still reading the data, the producer might have already overwritten it already. 
>
>Ordinary buffering does not handle this issue because it doesn't manage the synchronization between the producer and consumer. It cannot be determined by the consumer if it reads the data completely and accurately produced by the producer. Double Buffering solves this problem by having two memory locations where the producer writes the data on one buffer and the consumer reads data from the other buffer. Once complete, they switch buffers until the transfer is complete. Which is why double buffering is also called as buffer swapping.
>
>(Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)

4. Why was circular buffering introduced?
>Circular buffering was introduced to efficiently manage buffer space by treating it as a circular queue. Meaning that data is stored in a circular pattern just like in circular linked-lists. This eliminates the need to move data through the buffer, reduces overhead, and allows for continuous, simultaneous read and write operations allowing the system to read and write to the buffer simultaneously without having to wait for the buffer to be filled or empty.
>
>When the buffer is in circular manner, this makes sure that the buffer is always in use and no data is being wasted. This method is much more efficient for continuous and, simultaneous read and write operations.
>
>(Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)

5. Explain the statement: Spooling reduces the amount of time spent by a process waiting for an I/O operation to complete.
>Spooling reduces the amount of time a process spends waiting for I/O by allowing the process to continue executing while I/O operations are performed asynchronously in the background. Meaning that the process doesn't have to wait for the I/O operations to complete before it can move on to the next task. This decouples the process's execution from I/O device speed meaning that the process can execute at its own speed without being slowed down by the I/O device resulting in a much more efficient overall processing time.
>
>(Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)

6. Explain briefly why interrupts are indispensable in a single-processor system that supports parallel activities.
>Interrupts are indispensable in a single-processor system because they allow the CPU to respond to multiple, concurrent events by temporarily suspending the current process, handling the interrupt, and then resuming the process. This creates the illusion of parallel activities. 
>
>(Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)

7. When an interrupt occurs, the following are executed:
(1) disable_interrupts()
(2) save_pc_and_registers()
(3) identify_interrupting_device()
(4) device_handler()
Why is there a need to execute (1) and (2) before (3) and (4)?
>`disable_interrupts()` and `save_pc_and_registers()` are executed before `identify_interrupting_device()` and `device_handler()` to prevent further interrupts from disrupting the interrupt handling process and to preserve the current state of the CPU before handling the interrupt. If interrupts are not disabled and if the registers were not saved when a new interrupt occurs, it would corrupt the current data or would not allow the possibility of coming back to the previous process. Which is why its needed to stop new interrupts and save the current state.
>
>(Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)

8. With interrupts, one can avoid losing data that arrives in the system for processing. Explain how this is possible.
>Interrupts can avoid data loss by signaling the arrival of new data, allowing the CPU to process it before being overwritten or lost due to buffer overflow. The interrupt forces the system to handle the incoming data before continuing with its current process. 
>
>(Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)

9. An interrupt-driven operating system is usually interrupted by events that need to take control of the CPU. For example, when a set of data arrives in the system, the CPU may be taken away from the process currently in control of it. Describe the actions of the system right after an interrupt occurred up to the time control is given back to the interrupted process.
>After an interrupt occurs, the system saves the current process's state, identifies the interrupt source, executes the corresponding interrupt handler, restores the saved process state, and then resumes the interrupted process. 
>
>(Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)

10. Which of the following instructions should be privileged?
a. Set value of timer
b) Read the clock
c) Clear memory
d) Turn off interrupts
e) Switch from user to monitor/system mode
>Privileged instructions include: 
>**a) Set value of timer, 
>c) Clear memory, 
>d) Turn off interrupts, and 
>e) Switch from user to monitor/system mode** 
>
>**Reading the clock (b)** is typically not privileged because it doesn't pose a security risk or system stability concern. When we save privileged, only an authorized person or the kernel system should be allowed to modify changes to the host system. Which is why these four intructions listed above are considered as such.
>
>(Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)

11. Some early computers protected the operating system by placing it in a memory partition that could not be modified by either the user job or the operating system itself. Describe at least two difficulties that you think could arise with such a scheme.
>Two difficulties with protecting the operating system in a memory partition: 
>**a) The operating system might need to modify its own code or data structures, which would be impossible in this scheme, and 
>b) Hardware complexity increases, as additional protection mechanisms are required to enforce the partitioning.** 
>
> For (a), it would be difficult to patch or update the system since it is protected by the operating system. Other case would be difficulty in saving sensitive information only for the system to access. Such problem arises when an unauthorized user is able to access sensitive information saved on the system. As for (b), old computer operating systems are hardcoded to the hardware itself thus it adding more instructions for having a separate memory partition would require additional components however it is still a possibility to have the same hardware were its instructions for protection are implemented similarly.
>
>(Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)

12. Show how a desire for use of control cards leads naturally to the creation of separate user and monitor (system) modes of operation.
>Control cards can enforce separate user and monitor modes by requiring users to switch to monitor mode to execute privileged instructions. This division provides a protected environment for system operations, preventing unauthorized access to critical system resources. Since there is separation, the flow of event would eventually lead to that distinction that it would eventually happen.
>
>(Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)

13. What is buffering? How might buffering coupled with interrupts
a) avoid loss of data in a system; and
b) increase CPU utilization
> Buffering is a technique to temporarily store data in a buffer or memory location useful for transfering data on different devices with different speeds. When a data is transfered on the buffer, the faster device does not need to wait for the slower device. 
>
> Buffering a) avoids data loss by temporarily storing incoming data while the system is busy, allowing the CPU to process it later, and b) increases CPU utilization by decoupling I/O operations from process execution, allowing the CPU to work on other tasks while waiting for I/O completion. 
>
> Data can be avoided when there is a buffer as devices (consumer and producer) that has different speeds would be able to work asynchronously without problems and with circular buffer, the CPU utilization will be used to the maximum or as efficient as possible.
>
>(Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)

14. Why do operating systems usually maintain a small kernel? Why not include in the kernel all the facilities available in the operating system?
>Operating systems maintain a small kernel to improve system stability, security, and performance. A smaller kernel reduces the attack surface for security vulnerabilities and minimizes the risk of bugs in critical system components. Additionally, it reduces memory footprint and execution overhead. Not only that, a kernel has only one purpose and it is to create an environment for users to develop softwares for. If the kernel ships with all the facilities, then there is no point of creating an operating system. 
>
>(Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)

15. Give one change in the system when it is upgraded from a simple multiprogramming system to time-sharing systems.
>