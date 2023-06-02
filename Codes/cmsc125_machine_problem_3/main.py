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
from typing import List
import os, sys

from prettytable import PrettyTable
from pynput import keyboard

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
        self.time_utilization: timedelta        = timedelta(seconds=0)
        self.job: Job|None                      = None
        self.bytes_used: int                    = 0

    def __str__(self) -> str:
        string = ""
        string += f"Memory Stream: {self.stream}\n"
        string += f"Size: {self.size} bytes\n"
        string += (f"Fragmentation: {self.fragmentation}\n") 
        string += f"Used Count: {self.allocations_count}\n"
        string += f"Seconds Used: {self.time_utilization}\n"
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

    def display_memory_block_average(self) -> None:
        memory_table: PrettyTable = PrettyTable(["Memory Stream", "Memory Size", "Average Memory Usaged", "Average Internal Fragmentation", "Time Utilization", "Average Storage Utilization", "Allocations Count"])

        memory_block_count: int = len(self.snapshots[0].module.memory)
        snapshot_count: int     = len(self.snapshots) - 1 # do not include last

        total_mem_usage           = 0
        total_fragmentation       = 0
        total_storage_utilization = 0
        total_time_util           = timedelta(seconds=0)

        for i in range(memory_block_count):
            mem_usage           = 0
            fragmentation       = 0
            storage_utilization = 0
            for snapshot in self.snapshots:
                mem_usage       += snapshot.module.memory[i].bytes_used
                fragmentation   += snapshot.module.memory[i].fragmentation
                storage_utilization += snapshot.module.memory[i].bytes_used / snapshot.module.memory[i].size

            memory_table.add_row([i+1, f"{self.snapshots[0].module.memory[i].size} bytes", f"{mem_usage/snapshot_count:.2f} bytes", f"{fragmentation/snapshot_count:.2f} bytes", self.snapshots[-1].module.memory[i].time_utilization, f"{storage_utilization/snapshot_count*100:.2f}%", f"{self.snapshots[-1].module.memory[i].allocations_count} jobs"])

        for snap in self.snapshots:
            total_mem_usage += snap.module.memory_used
            total_fragmentation += snap.module.total_fragmentation
            total_storage_utilization += snap.metric.module_storage_utilization

        for memory in self.snapshots[-1].module.memory:
            total_time_util += memory.time_utilization
        memory_table.add_row(["Algorithm Average", "-", f"{total_mem_usage/snapshot_count:.2f} bytes", f"{total_fragmentation/snapshot_count:.2f} bytes", total_time_util/snapshot_count, f"{total_storage_utilization/snapshot_count*100:.2f}%", "-"])
                
        print(memory_table)
        ppnu = sum(1 for block in self.snapshots[-1].module.memory if not block.allocations_count)/memory_block_count*100
        pphu = sum(1 for block in self.snapshots[-1].module.memory if block.allocations_count >= (max(block.allocations_count for block in self.snapshots[-1].module.memory)*0.75))/memory_block_count*100
        print(f"Percentage Partitions Never Used: {ppnu:.2f}%")
        print(f"Percentage Partitions Heavily Used: {pphu:.2f}%")

    def display_job_average(self) -> None:
        job_count: int          = len(self.snapshots[0].module.jobs)
        snapshot_count: int     = len(self.snapshots) - 1 # do not include last

        total_throughput    = 0
        total_waiting_time  = timedelta(seconds=0)
        total_queue_length  = 0
        for snap in self.snapshots:
            total_throughput    += snap.metric.processing_count
            total_queue_length  += snap.metric.waiting_queue_length
        for job in self.snapshots[-1].module.jobs:
            total_waiting_time += job.waiting_time

        print(f"Time: {self.snapshots[-1].timestamp}")
        print(f"Average Waiting Time: {total_waiting_time/job_count} ({self.snapshots[-1].metric.total_waiting_time})")
        print(f"Average Processing Jobs: {total_throughput/snapshot_count:.2f} jobs per unit time")
        print(f"Average Queue Length: {total_queue_length/snapshot_count:.2f} jobs per unit time")





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
                block.time_utilization += timedelta(seconds=1)
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

    memory_table: PrettyTable   = PrettyTable(["Memory Stream", "Assigned Job Stream", "Memory Size (bytes)", "Memory Used (bytes)", "Internal Fragmentation (bytes)", "Time Utilization", "Allocations Count", "Storage Utilization"])
    job_table: PrettyTable      = PrettyTable(["Job Stream", "Assigned Memory Block", "Job Size (bytes)", "Waiting Time", "Current Time", "Completed"])
    for m in module.memory:
        if m.job:
            memory_table.add_row([m.stream, m.job.stream, m.size, m.bytes_used, m.fragmentation, m.time_utilization, m.allocations_count, f"{(m.bytes_used / m.size) * 100:.2f}%"])
        else:
            memory_table.add_row([m.stream, "-", m.size, m.bytes_used, m.fragmentation, m.time_utilization, m.allocations_count, f"{(m.bytes_used / m.size) * 100: .2f}%"])

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

    # print(simulation.snapshots[i].metric)


def show_help():
    keys = PrettyTable(["Key", "Command"])
    keys.add_row(["h", "Show help menu"])
    keys.add_row(["q", "Quit simulation"])
    keys.add_row(["b", "Decrement time"])
    keys.add_row(["n", "Increment time"])
    keys.add_row(["s", "Show statistics"])
    keys.add_row(["t", "Set time"])

    print(keys)


def read_file_jobs(filename: str) -> List[Job]:
    with open(filename, 'r') as file:
        lines = file.readlines()

    jobs = []
    for line in lines:
        j = line.rstrip().split()
        job = Job(int(j[0]), int(j[1]), int(j[2]))
        jobs.append(job)

    return jobs

def read_file_blocks(filename: str) -> List[MemoryBlock]:
    with open(filename, 'r') as file:
        lines = file.readlines()

    blocks = []
    for line in lines:
        j = line.rstrip().split()
        block = MemoryBlock(int(j[0]), int(j[1]))
        blocks.append(block)

    return blocks


def main(args):
    if len(args) == 3:
        jobs: List[Job]             = read_file_jobs(args[0])
        blocks: List[MemoryBlock]   = read_file_blocks(args[1])

        match args[2]:
            case 'ff' | 'first-fit':
                # module = MemoryManager(blocks, jobs)
                pass
            case 'bf' | 'best-fit':
                blocks = sorted(blocks, key=lambda x: x.size)
            case 'wf' | 'worst-fit':
                blocks = sorted(blocks, key=lambda x: x.size, reverse=True)
            case _:
                print("Run: python main.py <job file name> <memory block file name> <algorithm: first-fit | best-fit | worst-fit>")

        module = MemoryManager(blocks, jobs)
        simulation = simulate(module)
        simulation = calculate(simulation)

        index = 0

        while True:
            display(simulation, index)
            t = input()
            match t:
                case 'b':
                    if t:
                        index -= 1
                case 'q':
                    break
                case 'h':
                    os.system("clear")
                    show_help()
                    print()
                    input("PRESS ANY <ENTER> TO CONTINUE")
                case 't':
                    index = int(input("TIMESTAMP > "))
                case 's':
                    os.system("clear")
                    simulation.display_memory_block_average()
                    simulation.display_job_average()
                    input()
                case _:
                    if 'b' in t and t[0] == 'b':
                        if t:
                            index -= t.count('b') + 1
                    if 'n' in t and t[0] == 'n':
                        index += t.count('n')
                    else:
                        index += 1
    else:
        print("Run: python main.py <job file name> <memory block file name> <algorithm: first-fit | best-fit | worst-fit>")



        

if __name__ == "__main__":
    main(sys.argv[1:])
