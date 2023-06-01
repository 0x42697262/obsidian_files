"""
    Memory Management Simulation
    
    This program simulates memory management using three different algorithms: First Fit, Best Fit, and Worst Fit.
    It simulates the allocation of jobs in memory blocks and tracks various metrics such as throughput, storage utilization,
    waiting queue length, and internal fragmentation.
    
    The program utilizes dataclasses for defining the Job and Block objects, and a Tick object to represent the state
    of memory allocation at each tick of the simulation.
    
    The main steps of the simulation include:
    1. Defining the Job and Block objects.
    2. Performing memory allocation using First Fit, Best Fit, and Worst Fit algorithms.
    3. Recording the simulation history and tracking metrics.
    4. Displaying the simulation results.
"""

from datetime import timedelta
from copy import deepcopy
from typing import List, Tuple
from prettytable import PrettyTable
import os

class Job:
    def __init__(self, stream: int, current_time: int, size: int) -> None:
        self.stream: int                                = stream
        self.current_time: timedelta                    = timedelta(seconds=current_time)
        self.size: int                                  = size
        self.waiting_time: timedelta                    = timedelta(seconds=0)
        self.assigned_memory_block: MemoryBlock|None    = None
        self.complete: bool                             = False

    def __str__(self) -> str:
        string = ""
        string += (f"Job Stream: {self.stream}\n")
        string += (f"Current Time: {self.current_time}\n") 
        string += (f"Size: {self.size} bytes\n") 
        string += (f"Waiting Time: {self.waiting_time}\n") 
        string += (f"Complete: {self.complete}\n") 
        if self.assigned_memory_block:
            string += (f"Memory Block: {self.assigned_memory_block.stream} | {self.assigned_memory_block.size}\n")  
        else:
            string += (f"MemoryBlock: {self.assigned_memory_block}\n")

        return string






class MemoryBlock:
    def __init__(self, stream: int, size: int) -> None:
        self.stream: int                        = stream
        self.size: int                          = size
        self.fragmentation: int                 = 0
        self.allocations_count: int             = 0
        self.seconds_used_by_a_job: timedelta   = timedelta(seconds=0)
        self.job: Job|None                      = None
        self.bytes_used: int                    = 0

    def __str__(self) -> str:
        string = ""
        string += f"Memory Stream: {self.stream}\n"
        string += f"Size: {self.size} bytes\n"
        string += (f"Fragmentation: {self.fragmentation}\n") 
        string += f"Used Count: {self.allocations_count}\n"
        string += f"Seconds Used: {self.seconds_used_by_a_job}\n"
        string += f"Allocated Job: [{self.job}]\n"
        string += f"Memory Used: {self.bytes_used} bytes\n"

        return string






class MemoryManager:
    def __init__(self, memory: List[MemoryBlock], jobs: List[Job]) -> None:
        self.memory: List[MemoryBlock]      = memory
        self.jobs: List[Job]                = jobs
        self.total_memory: int              = sum(block.size for block in self.memory)
        self.total_fragmentation: int       = 0
        self.memory_used: int               = 0
        self.job_total_memory: int          = sum(job.size  for job in self.jobs)

        self.allocatable_jobs: List[Job]    = []
        self.current_complete: List[Job]    = []

    def recalculate_memory(self) -> None:
        self.total_fragmentation:int    = sum(block.fragmentation   for block in self.memory)
        self.memory_used:int            = sum(block.bytes_used      for block in self.memory)


    def allocate_job(self, block: MemoryBlock, job: Job) -> None:
        job.assigned_memory_block   = block
        block.fragmentation         = block.size - job.size
        block.job                   = job 
        block.bytes_used            = job.size
        block.allocations_count     += 1
        self.recalculate_memory()


    def deallocate_job(self, block: MemoryBlock, job: Job) -> None:
        block.bytes_used    = 0
        block.fragmentation = 0
        block.job           = None
        job.complete        = True
        job.assigned_memory_block = None
        self.current_complete.append(job)
        self.recalculate_memory()





class Metric:
    def __init__(self) -> None:
        self.throughput: int                    = 0
        self.module_storage_utilization: float  = 0
        self.waiting_queue_length: int          = 0
        self.total_waiting_time: timedelta      = timedelta(seconds=0)
        self.total_fragmentation: int           = 0
        self.total_allocations_count: int       = 0
        self.processing_count: int              = 0
        
    def __str__(self) -> str:
        string = ""
        string += f"Throughput: {self.throughput}\n"
        string += f"Storage Utilization: {self.module_storage_utilization*100:.2f}\n"
        string += f"Waiting Queue Length: {self.waiting_queue_length}\n"
        string += f"total_waiting_time: {self.total_waiting_time}\n"
        string += f"Total Internal Fragmentation: {self.total_fragmentation}\n"
        string += f"Total Allocations: {self.total_allocations_count}\n"

        return string












class ModuleSnapshot:
    def __init__(self, timestamp: timedelta, module: MemoryManager) -> None:
        self.timestamp: timedelta   = timestamp
        self.module: MemoryManager  = module
        self.metric: Metric         = Metric()


    def apply_metrics(self) -> None:
        self.metric.throughput                      = len(self.module.current_complete)
        self.metric.module_storage_utilization      = (self.module.memory_used) / self.module.total_memory
        self.metric.waiting_queue_length            = sum(1 for job in self.module.jobs if not job.assigned_memory_block and not job.complete)
        for _ in self.module.jobs:
            self.metric.total_waiting_time          += _.waiting_time
        self.metric.total_fragmentation             = self.module.total_fragmentation
        self.metric.total_allocations_count         = sum(_.allocations_count  for _ in self.module.memory)
        self.metric.processing_count                = sum(1 for _ in self.module.memory if _.job)













class SnapshotsManager:
    def __init__(self) -> None:
        self.snapshots: List[ModuleSnapshot] = []

    def add(self, snapshot: ModuleSnapshot) -> None:
        self.snapshots.append(snapshot)





def simulate(module: MemoryManager) -> SnapshotsManager:
    timestamp: timedelta        = timedelta(seconds=0)
    memory_block_max_size: int  = max(block.size for block in module.memory)

    # only use allocatable jobs
    allocatable_jobs    = [ job for job in module.jobs if job.size <= memory_block_max_size]
    total_jobs          = len(allocatable_jobs)

    # make a snapshot history manager
    all_snapshots: SnapshotsManager     = SnapshotsManager()

    # loop
    while True:
        module.current_complete = []
        # deallocate all jobs in memory
        for block in module.memory:
            if block.job:
                if block.job.current_time == timedelta(seconds=0):
                    module.deallocate_job(block, block.job)
                    total_jobs -= 1
        
        # allocate a job in memory
        for block in module.memory:
            for job in allocatable_jobs:
                if job.size <= block.size and not block.job:
                    allocatable_jobs = [ _ for _ in allocatable_jobs if _.stream != job.stream ]
                    module.allocate_job(block, job)
                    break
        
        if not total_jobs:
            module.current_complete = []

        all_snapshots.add(ModuleSnapshot(timestamp, deepcopy(module)))
        timestamp += timedelta(seconds=1)

        # process all jobs in memory
        for block in module.memory:
            if block.job:
                block.seconds_used_by_a_job += timedelta(seconds=1)
                block.job.current_time -= timedelta(seconds=1)

        # increment all allocated jobs
        for job in allocatable_jobs:
            job.waiting_time += timedelta(seconds=1)


        if not total_jobs:
            break


    return all_snapshots

def calculate(simulation: SnapshotsManager) -> SnapshotsManager:
    for snapshot in simulation.snapshots:
        snapshot.apply_metrics()

    return simulation

def display(simulation: SnapshotsManager, index: int) -> None:
    os.system('clear')
    i = index % len(simulation.snapshots)

    snapshot = simulation.snapshots[i]
    module   = snapshot.module
    memory   = module.memory

    memory_table: PrettyTable   = PrettyTable(["Memory Stream", "Assigned Job Stream", "Memory Size (bytes)", "Memory Used (bytes)", "Internal Fragmentation (bytes)", "Time Utilization", "Allocations Count", "Storage Utilization"])
    job_table: PrettyTable      = PrettyTable(["Job Stream", "Assigned Memory Block", "Job Size (bytes)", "Waiting Time", "Current Time", "Completed"])
    for m in module.memory:
        if m.job:
            memory_table.add_row([m.stream, m.job.stream, m.size, m.bytes_used, m.fragmentation, m.seconds_used_by_a_job, m.allocations_count, f"{(m.bytes_used / m.size) * 100:.2f}%"])
        else:
            memory_table.add_row([m.stream, "-", m.size, m.bytes_used, m.fragmentation, m.seconds_used_by_a_job, m.allocations_count, f"{(m.bytes_used / m.size) * 100: .2f}%"])

    for j in module.jobs:
        if j.assigned_memory_block:
            job_table.add_row([j.stream, j.assigned_memory_block.stream, j.size, j.waiting_time, j.current_time, j.complete])
        else:
            job_table.add_row([j.stream, "-", j.size, j.waiting_time, j.current_time, j.complete])

    memory_table.add_row(["Total", f"{snapshot.metric.processing_count} jobs (working)", f"{module.total_memory} bytes", f"{module.memory_used} bytes", f"{module.total_fragmentation} bytes", "-", f"{snapshot.metric.total_allocations_count} jobs", f"{snapshot.metric.module_storage_utilization*100: .2f}% (average)"])
    job_table.add_row(["Total", f"{snapshot.metric.waiting_queue_length} jobs (queue)", f"{module.job_total_memory} bytes", snapshot.metric.total_waiting_time, "-", f"{sum(1 for _ in module.jobs if _.complete)} jobs ( +{snapshot.metric.throughput} )"])

    print("Timestamp:", simulation.snapshots[i].timestamp)
    print()
    print(memory_table)
    print(job_table)
    print()

    print(simulation.snapshots[i].metric)


def main():
    jobs: List[Job] = [
        Job(1,   5,  5760),
        Job(2,   4,  4190),
        Job(3,   8,  3290),
        Job(4,   2,  2030),
        Job(5,   2,  2550),
        Job(6,   6,  6990),
        Job(7,   8,  8940),
        Job(8,   10, 740),
        Job(9,   7,  3930),
        Job(10,  6,  6890),
        Job(11,  5,  6580),
        Job(12,  8,  3820),
        Job(13,  9,  9140),
        Job(14,  10, 420),
        Job(15,  10, 220),
        Job(16,  7,  7540),
        Job(17,  3,  3210),
        Job(18,  1,  1380),
        Job(19,  9,  9850),
        Job(20,  3,  3610),
        Job(21,  7,  7540),
        Job(22,  2,  2710),
        Job(23,  8,  8390),
        Job(24,  5,  5950),
        Job(25,  10, 760),
    ]

    blocks: List[MemoryBlock] = [
        MemoryBlock(1,  9500),
        MemoryBlock(2,  7000),
        MemoryBlock(3,  4500),
        MemoryBlock(4,  8500),
        MemoryBlock(5,  3000),
        MemoryBlock(6,  9000),
        MemoryBlock(7,  1000),
        MemoryBlock(8,  5500),
        MemoryBlock(9,  1500),
        MemoryBlock(10, 500),
    ]

    m = MemoryManager(blocks, jobs)
    snap = simulate(m)

    snap = calculate(snap)

    index = 0
    while True:
        display(snap, index)
        t = input()
        match t:
            case 'b':
                if t:
                    index -= 1
            case 'q':
                break
            case _:
                if 'b' in t:
                    if t:
                        index -= t.count('b') + 1
                if 'n' in t:
                    index += t.count('n')
                else:
                    index += 1


    

if __name__ == "__main__":
    main()
