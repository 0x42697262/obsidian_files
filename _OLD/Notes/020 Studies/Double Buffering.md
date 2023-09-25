> [!INFO]
> Status:
> Tags: #I/O #Buffering #OperatingSystem 

----
# Double Buffering
- also known as `buffer swapping`
- uses two memory locations to temporarily store data
	- one can be used for reading data in the buffer
	- one can used for writing data in another buffer (or while it's being emptied or filled by the operating system)
 
Double buffering may be inadequate if the process performs rapid burts of I/O.  This is solved by using more than two buffers ([[Circular Buffering]])