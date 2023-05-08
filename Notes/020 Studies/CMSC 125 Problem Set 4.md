CMSC 125 Problem Set 4
**Topic Coverage**: Memory Management

---

### 1.) Explain the difference between internal and external fragmentation.

> [!INFO]- Answer
> **Internal fragmentation** is lost memory caused by memory deemed allocated but is unused while **external fragmentation** is lost memory caused by memory that can be allocated but no taker is available to occupy it.
>
> Which means that internal fragmentation occurs when a process requests a certain amount of memory, and the operating system allocates a larger memory block than what is required resulting in unused memory within the block, which cannot be used by other processes. So, the unused memory is referred to as internal fragmentation because it is internal to the allocated memory block. As for external fragmentation, it occurs when there is enough total memory available to satisfy the allocation requests of all processes, but the available memory is not contiguous. This means that the available memory is divided into small, non-contiguous blocks, which cannot be used to satisfy the memory requests of larger programs or processes. This results in the system appearing to be "out of memory" even though there may be enough free memory available. This unused memory exists outside of the allocated memory blocks.
>
> The first image is an internal fragmentation, the second image is an external fragmentation.
> ![[Pasted image 20230507234241.png]]
> ![[Pasted image 20230507234330.png]]

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 2.) Explain the following allocation algorithms/placement policies:
```
a.) First-fit
b.) Best-fit
c.) Worst-fit
```

> [!INFO]- Answer
> In **first-fit**, the *first chunk of memory in the free list that is big enough* to accomadate the requesting process is allocated. It starts at the beginning of the list and searches sequentially for the first chunk that is big enough. This is the simplest and fastest method but may lead to internal fragmentation.
> 
> In **best-fit**, the chunk of memory in the free list which produces the *smallest left-over* is assigned to the requesting process. This strategy is efficient in terms of memory usage, as it can help minimize internal fragmentation. However, it may take longer to find a suitable block of memory since the entire free list needs to be searched.
> 
> As for **worst-fit**, the chuck of memory in the free list which produces the *largest left-over* is assigned to the requesting process. This results in the most significant leftover memory after the allocation as this strategy can lead to more internal fragmentation and may not be as efficient as the other two methods. However, it can be useful when allocating larger memory blocks.

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 3.) Given memory partitions of 100K, 500K, 200K, 300K and 600K (in order), how would each of the First-fit, Best-fit and Worst-fit algorithms place processes of 212K, 417K, 112K, and 426K (in order)? Which algorithm makes the most efficient use of memory?

> [!INFO]- Answer
>![[Pasted image 20230508090237.png]]
>**Steps:**
>
>0) Memory Initialization
>1) Allocated *212K* memory
>2) Allocated *417K* memory
>3) Allocated *112K* memory
>4) Failure to allocate *426K* memory
> 
> ![[Pasted image 20230508100118.png]]
>**Steps:**
>
>0) Memory Initialization
>1) Allocated *212K* memory
>2) Allocated *417K* memory
>3) Allocated *112K* memory
>4) Allocated *426K* memory
> 
> ![[Pasted image 20230508100805.png]]
>**Steps:**
>
>0) Memory Initialization
>1) Allocated *212K* memory
>2) Allocated *417K* memory
>3) Allocated *112K* memory
>4) Failure to allocate *426K* memory
>
> In this particular example, the **best-fit** algorithm makes the most efficient use of memory as it minimizes the amount of leftover memory after allocation, thereby reducing the possibility of fragmentation.

> [!INFO]- Source
> Me


### 4.) Consider a system where a program can be separated into two parts: code and data. The CPU knows whether it wants an instruction (instruction fetch) or data (data fetch or store). Therefore, two base-limit register pairs are provided: one for the instructions and one for the data. The instruction base-limit register pair is automatically read-only, so programs can be shared among different users. Discuss the advantages and disadvantages of this scheme.

> [!INFO]- Answer
> The scheme where a program is separated into code and data segments, and two base-limit register pairs are provided for each segment has several advantages. One of the major advantages is that it facilitates code and data sharing among different processes, thereby reducing memory usage and improving system efficiency. Since the instruction base-limit register is read-only, it ensures that program code cannot be modified, which enhances system security and prevents unauthorized access and malicious attacks.
> 
> Furthermore, this scheme can be used to enforce memory protection by restricting program access to memory outside of its allocated range, preventing segmentation faults and improving system stability. However, there are some disadvantages to this scheme. For instance, the available address space for each segment is limited, which can become a constraint when dealing with large programs. Additionally, separating code and data segments requires additional overhead on the CPU, which can lead to reduced system performance. Finally, implementing and maintaining this scheme can add complexity to the memory management system, making it difficult to implement and manage.

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 5.) Why is virtual address translation usually done using hardware instead of software?

> [!INFO]- Answer
> Virtual address translation is usually done using hardware instead of software because hardware-based translation is much faster than software-based translation. Hardware-based translation uses a special, small, fast-lookup hardware cache called a translation look-aside buffer (TLB), which is associative, high-speed memory. Each entry in the TLB consists of two parts: a key (or tag) and a value. When the associative memory is presented with an item, the item is compared with all keys simultaneously. If the item is found, the corresponding value field is returned. The search is fast; a TLB lookup in modern hardware is part of the instruction pipeline, essentially adding no performance penalty. On the other hand, software-based translation requires the operating system to perform the translation, which involves accessing the page table and performing calculations to determine the physical address. This process is much slower than hardware-based translation and can significantly slow down the system.

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.

### 6.) Most operating systems go to the extend of exhausting all methods of making available a space for an incoming job just to avoid resorting to compaction. Why is this so?

> [!INFO]- Answer
>

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 7.) Consider a swapping system in which the memory is composed of the following hole sizes (assuming the leftmost hole is the first in the list): 10K, 4K, 20K, 18K, 9K, 12K, 15K Which hole is taken for successive segment requests of 12K, 5K and 10K for first-fit? How about for best-fit and worst-fit?

> [!INFO]- Answer
>

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 8.) What is swapping? What are the motivations for providing swapping? Show how this technique enables a reasonable response time to be given to each user of an interactive system. In what situation is swapping not effective?

> [!INFO]- Answer
>

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.

### 9.) Consider a swapping system. Measured utilization are:
```
CPU utilization 20%
Swapping device (drum) 99.7%
Other I/O devices 5%
What will be the effect on the CPU utilization if we
a.) get a faster CPU?
b.) get a bigger hard disk for swapping?
c.) increase the degree of multiprogramming?
d.) decrease the degree of multiprogramming?
e.) get faster other I/O devices?
```

> [!INFO]- Answer
>

> [!INFO]- Source
> Silberschatz, A., Gagne, G and Galvin, P. (2018). “Operating Systems Concepts Tenth Edition”. John Wiley & Sons Inc.
> Albacea, Eliezer. (2007). “Operating Systems: Basic Concepts Third Edition”. JPVA Publishing House.
