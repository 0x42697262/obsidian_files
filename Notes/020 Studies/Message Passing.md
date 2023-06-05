> [!INFO]
> Status:
> Tags: #ParallelSystems #OperatingSystem #ComputerScience #InterconnectionNetwork #DistributedSharedMemory

> [!INFO]- Compass
> **From**: [[Parallel Systems]], [[Distributed Shared Memory]], [[Communication Paradigm]], [[Interconnection Network]]
> **Leads to:** 
> **Similar ideas:** 
> **Opposite ideas:** 

----
# Message Passing

In a message passing system, processes or threads are considered as isolated entities that communicate solely by exchanging messages. They do not share memory directly, unlike in shared memory models. Instead, they rely on message passing to transmit data and synchronize their actions.

- Messages are sent from one processor to another.
- Each processor has its own memory
	- No shared address space
- A processor cannot **directly access** a remote memory found in another processor
	- To access a remote memory, make a *request* (using message passing) by the processor to the remote processor
- Possible to have pseudo-shared-memory because message-passing is distributed memory through providing each processor with a *cache*   
	- This is because a pseudo-shared-memory is an abstraction for a simplified programming model
	- Implemented through [[Cache Coherent Non-Uniform Memory Access]] (ccNUMA)

By equipping each process with a cache and utilizing an advanced address-mapping scheme, the distributed memory can be conceptually represented as a single shared memory space residing in each processor's cache. This representation simplifies the programming model by allowing processes to interact with shared variables as if they were directly accessing a shared memory space.

Variants:
1. Completely Connected Interconnections
2. Line/Ring Interconnections
3. Mesh Interconnections
4. Tree Interconnections
5. Hypercube Interconnections


> [!INFO]- Figure
> ![[Pasted image 20230528200637.png]]