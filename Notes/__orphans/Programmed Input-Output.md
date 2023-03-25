> [!INFO]
> Status:
> Tags: #I/O

----
# Programmed Input-Output
- this approach is `polling`
- the processor has to continuously check the device for update (status register) to determine if the operation is complete
- this method is slow because:
	- processor has to continously check which consumes a huge amount of resources
	- waiting = slow