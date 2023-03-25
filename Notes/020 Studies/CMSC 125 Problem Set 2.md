
CMSC 125 Problem Set 2  
**Topic Coverage**: Basic OS Concepts

----

1. Why are interrupts necessary in a time-sharing system?
>Interrupts are necessary in a time-sharing system to enable efficient multitasking and prevent a single process from monopolizing the CPU. Interrupts allow the system to switch between multiple processes, giving the appearance of simultaneous execution. Since interrupts suspends the current operation, it can then proceed to the next operation and in this case, it's the user's operations. Which when an operation is completed, it resumes the suspended operation. (Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)

2. Why is it necessary to provide supervisor calls in an operating system? Give an instance wherein such call has to be made
>Supervisor calls, or system calls, are necessary to provide a safe and controlled interface between user programs and the operating system's kernel. This sets some sort of boundary between a user application and the kernel by providing an access control.
>
>For instance, a program might make a system call to request access to a file, which the operating system can then grant or deny based on permissions. Since user applications does not have full access or control to the system and its hardware unlike the kernel. (Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)

3. Discuss one problem that is solved by double buffering, but is not properly handled by ordinary buffering.
>Double buffering solves the problem of "tearing" that occurs when the producer and consumer work at different speeds, and the consumer reads data while the producer is still updating it. Ordinary buffering does not handle this issue because it doesn't manage the synchronization between the producer and consumer. (Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)
4. Why was circular buffering introduced?
>Circular buffering was introduced to efficiently manage buffer space by treating it as a circular queue. This eliminates the need to move data through the buffer, reduces overhead, and allows for continuous, simultaneous read and write operations. (Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)
5. Explain the statement: Spooling reduces the amount of time spent by a process waiting for an I/O operation to complete.
>Spooling reduces the amount of time a process spends waiting for I/O by allowing the process to continue executing while I/O operations are performed asynchronously in the background. This decouples the process's execution from I/O device speed. (Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)
6. Explain briefly why interrupts are indispensable in a single-processor system that supports parallel activities.
>Interrupts are indispensable in a single-processor system because they allow the CPU to respond to multiple, concurrent events by temporarily suspending the current process, handling the interrupt, and then resuming the process. This creates the illusion of parallel activities. (Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)
7. When an interrupt occurs, the following are executed:
(1) disable_interrupts()
(2) save_pc_and_registers()
(3) identify_interrupting_device()
(4) device_handler()
Why is there a need to execute (1) and (2) before (3) and (4)?
>(1) and (2) are executed before (3) and (4) to prevent further interrupts from disrupting the interrupt handling process and to preserve the current state of the CPU before handling the interrupt. This ensures a smooth return to the interrupted process once the interrupt is handled. (Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)

8. With interrupts, one can avoid losing data that arrives in the system for processing. Explain how this is possible.
>Interrupts can avoid data loss by signaling the arrival of new data, allowing the CPU to process it before being overwritten or lost due to buffer overflow. The interrupt forces the system to handle the incoming data before continuing with its current process. (Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)
9. An interrupt-driven operating system is usually interrupted by events that need to take control of the CPU. For example, when a set of data arrives in the system, the CPU may be taken away from the process currently in control of it. Describe the actions of the system right after an interrupt occurred up to the time control is given back to the interrupted process.
>After an interrupt occurs, the system saves the current process's state, identifies the interrupt source, executes the corresponding interrupt handler, restores the saved process state, and then resumes the interrupted process. (Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)
10. Which of the following instructions should be privileged?
a. Set value of timer
b) Read the clock
c) Clear memory
d) Turn off interrupts
e) Switch from user to monitor/system mode
>Privileged instructions include: a) Set value of timer, c) Clear memory, d) Turn off interrupts, and e) Switch from user to monitor/system mode. Reading the clock (b) is typically not privileged because it doesn't pose a security risk or system stability concern. (Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)
11. Some early computers protected the operating system by placing it in a memory partition that could not be modified by either the user job or the operating system itself. Describe at least two difficulties that you think could arise with such a scheme.
>Two difficulties with protecting the operating system in a memory partition: a) The operating system might need to modify its own code or data structures, which would be impossible in this scheme, and b) Hardware complexity increases, as additional protection mechanisms are required to enforce the partitioning. (Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)
12. Show how a desire for use of control cards leads naturally to the creation of separate user and monitor (system) modes of operation.
>Control cards can enforce separate user and monitor modes by requiring users to switch to monitor mode to execute privileged instructions. This division provides a protected environment for system operations, preventing unauthorized access to critical system resources. (Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)
13. What is buffering? How might buffering coupled with interrupts
a) avoid loss of data in a system; and
b) increase CPU utilization
>Buffering a) avoids data loss by temporarily storing incoming data while the system is busy, allowing the CPU to process it later, and b) increases CPU utilization by decoupling I/O operations from process execution, allowing the CPU to work on other tasks while waiting for I/O completion. (Stallings, W. "Operating Systems: Internals and Design Principles." Pearson, 2018.)
14. Why do operating systems usually maintain a small kernel? Why not include in the kernel all the facilities available in the operating system?
>Operating systems maintain a small kernel to improve system stability, security, and performance. A smaller kernel reduces the attack surface for security vulnerabilities and minimizes the risk of bugs in critical system components. Additionally, it reduces memory footprint and execution overhead. (Tanenbaum, A. S. "Modern Operating Systems." Pearson, 2015.)
15. Give one change in the system when it is upgraded from a simple multiprogramming system to time-sharing systems.
>