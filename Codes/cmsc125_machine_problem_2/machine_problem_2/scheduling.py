class SchedulingAlgorithm:
    def __init__(self, process):
        self.data           = {}
        self.highest_job    = -1
        self.lowest_job     = -1

        for p in process:
            self.data[p]                    = {}
            self.data[p]['arrival_time']    = process[p]['arrival_time']
            self.data[p]['burst_time']      = process[p]['burst_time']
            self.data[p]['priority']        = process[p]['priority']
            self.data[p]['turnaround_time'] = 0
            self.data[p]['waiting_time']    = 0
            self.data[p]['computing_time']  = 0

        self.highest_job    = max(filter(lambda k: isinstance(k, int), self.data.keys()))
        self.lowest_job     = min(filter(lambda k: isinstance(k, int), self.data.keys()))


    def calculate_turnaround_time(self):
        pass
    
    def calculate_waiting_time(self):
        pass

    def calculate_computing_time(self):
        pass

    def show_stats(self):
        for p in self.data:
            print(p, self.data[p])
            print()
        print("len:", len(self.data))


class FCFSAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

        self.total_waiting_time     = 0
        self.total_turnaround_time  = 0
        self.total_computing_time   = 0


    def calculate_waiting_time(self, job):
        if job >= self.lowest_job + 1:
            self.data[job]['waiting_time'] = self.data[job-1]['turnaround_time']
            self.total_waiting_time += self.data[job-1]['turnaround_time']


    def calculate_turnaround_time(self, job):
        if job >= self.lowest_job + 1:
            self.data[job]['turnaround_time']   = self.data[job]['burst_time'] + self.data[job]['waiting_time']
        else:
            self.data[job]['turnaround_time'] = self.data[job]['burst_time']

        self.total_turnaround_time          += self.data[job]['turnaround_time']

    def calculate_computing_time(self, job):
        self.data[job]['computing_time'] = self.data[job]['turnaround_time'] - self.data[job]['waiting_time']
        self.total_computing_time += self.data[job]['computing_time']

    def calculate_avg_waiting_time(self) -> float:
        return self.total_waiting_time / len(self.data)

    def calculate_avg_turnaround_time(self) -> float:
        return self.total_turnaround_time / len(self.data)

    def calculate_avg_computing_time(self) -> float:
        return self.total_computing_time / len(self.data)
        

class SJFAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

class SRPTAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

class PriorityAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

class RoundRobinAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)
