> [!INFO]
> Status:
> Tags: #I/O 

----
# Interrupt-Driven Input-Output
- issues an I/O command to a module (device?) then proceeds to perform another operation
	- making interrups faster than polling (programmed)
- while waiting for an I/O to complete, it performs another operation
	- generates an interrupt to the processor to request its attention
	- suspends current work then executes data transfer with the I/O module
	- once complete, **resumes the interrupted processs**