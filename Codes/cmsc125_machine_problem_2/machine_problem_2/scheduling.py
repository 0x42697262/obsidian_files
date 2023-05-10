class SchedulingAlgorithm:
    def __init__(self, process):
        self.process = {}
        self.highest_job    = -1
        self.lowest_job     = -1
        self.data    = []

        self.total_waiting_time     = 0
        self.total_turnaround_time  = 0
        self.total_computing_time   = 0

        for p in process:
            self.process[p]                    = {}
            self.process[p]['arrival_time']    = process[p]['arrival_time']
            self.process[p]['burst_time']      = process[p]['burst_time']
            self.process[p]['priority']        = process[p]['priority']
            self.process[p]['turnaround_time'] = 0
            self.process[p]['waiting_time']    = 0
            self.process[p]['computing_time']  = 0

        self.highest_job    = max(filter(lambda k: isinstance(k, int), self.process.keys()))
        self.lowest_job     = min(filter(lambda k: isinstance(k, int), self.process.keys()))


    
    def calculate_waiting_time(self, index):
        if index >= 1:
            self.data[index][1]['waiting_time'] = self.data[index-1][1]['turnaround_time']
            self.total_waiting_time += self.data[index][1]['waiting_time']

    def calculate_turnaround_time(self, index):
        if index >= 1:
            self.data[index][1]['turnaround_time'] = self.data[index][1]['burst_time'] + self.data[index][1]['waiting_time']
        else:
            self.data[index][1]['turnaround_time'] = self.data[index][1]['burst_time'] 

        self.total_turnaround_time          += self.data[index][1]['turnaround_time']

    def calculate_computing_time(self, index):
        self.data[index][1]['computing_time'] = self.data[index][1]['turnaround_time'] - self.data[index][1]['waiting_time']
        self.total_computing_time += self.data[index][1]['computing_time']

    def calculate_avg_waiting_time(self):
        pass

    def calculate_avg_turnaround_time(self):
        pass

    def calculate_avg_computing_time(self):
        pass

    def show_stats(self):
        for p in self.data:
            print(f"job: {p[0]} --> {p[1]}")
            print()
        print("len:", len(self.data))


class FCFSAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['arrival_time'])

    def calculate_waiting_time(self, index):
        return super().calculate_waiting_time(index)

    def calculate_turnaround_time(self, index):
        return super().calculate_turnaround_time(index)

    def calculate_computing_time(self, index):
        return super().calculate_computing_time(index)


    def calculate_avg_waiting_time(self) -> float:
        return self.total_waiting_time / len(self.data)

    def calculate_avg_turnaround_time(self) -> float:
        return self.total_turnaround_time / len(self.data)

    def calculate_avg_computing_time(self) -> float:
        return self.total_computing_time / len(self.data)
        




class SJFAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['burst_time'])


    def calculate_waiting_time(self, index):
        return super().calculate_waiting_time(index)

    def calculate_turnaround_time(self, index):
        return super().calculate_turnaround_time(index)

    def calculate_computing_time(self, index):
        return super().calculate_computing_time(index)


    def calculate_avg_waiting_time(self) -> float:
        return self.total_waiting_time / len(self.data)

    def calculate_avg_turnaround_time(self) -> float:
        return self.total_turnaround_time / len(self.data)

    def calculate_avg_computing_time(self) -> float:
        return self.total_computing_time / len(self.data)



class SRPTAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)




class PriorityAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['priority'])


    def calculate_waiting_time(self, index):
        return super().calculate_waiting_time(index)

    def calculate_turnaround_time(self, index):
        return super().calculate_turnaround_time(index)

    def calculate_computing_time(self, index):
        return super().calculate_computing_time(index)


    def calculate_avg_waiting_time(self) -> float:
        return self.total_waiting_time / len(self.data)

    def calculate_avg_turnaround_time(self) -> float:
        return self.total_turnaround_time / len(self.data)

    def calculate_avg_computing_time(self) -> float:
        return self.total_computing_time / len(self.data)


class RoundRobinAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)
