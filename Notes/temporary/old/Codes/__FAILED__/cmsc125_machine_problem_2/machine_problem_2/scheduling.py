class SchedulingAlgorithm:
    def __init__(self, process):
        self.process = {}
        self.highest_job    = -1
        self.lowest_job     = -1
        self.data           = []
        self.gant_chart     = []

        self.total_waiting_time     = 0
        self.total_turnaround_time  = 0
        self.total_computing_time   = 0

        for p in process:
            self.process[p]                    = {}
            self.process[p]['arrival_time']    = process[p]['arrival_time']
            self.process[p]['burst_time']      = process[p]['burst_time']
            self.process[p]['priority']        = process[p]['priority']
            self.process[p]['completion_time'] = 0
            self.process[p]['turnaround_time'] = 0
            self.process[p]['waiting_time']    = 0
            self.process[p]['computing_time']  = 0

        self.highest_job    = max(filter(lambda k: isinstance(k, int), self.process.keys()))
        self.lowest_job     = min(filter(lambda k: isinstance(k, int), self.process.keys()))

    
    def calculate_completion_time(self, index):
        if index >= 1:
            self.data[index][1]['completion_time'] = self.data[index][1]['burst_time'] + self.data[index-1][1]['completion_time']
        else:
            self.data[index][1]['completion_time'] = self.data[index][1]['burst_time'] 
    
    def calculate_waiting_time(self, index):
        if index >= 1:
            self.data[index][1]['waiting_time'] = self.data[index][1]['turnaround_time'] - self.data[index][1]['burst_time']
            self.total_waiting_time += self.data[index][1]['waiting_time']

    def calculate_turnaround_time(self, index):
        self.data[index][1]['turnaround_time'] = self.data[index][1]['completion_time']

        self.total_turnaround_time          += self.data[index][1]['turnaround_time']

    def calculate_computing_time(self, index):
        self.data[index][1]['computing_time'] = self.data[index][1]['turnaround_time'] - self.data[index][1]['waiting_time']
        self.total_computing_time += self.data[index][1]['computing_time']

    def calculate_avg_waiting_time(self):
        return self.total_waiting_time / len(self.data)

    def calculate_avg_turnaround_time(self):
        return self.total_turnaround_time / len(self.data)

    def calculate_avg_computing_time(self):
        return self.total_computing_time / len(self.data)

    def append_job_to_gant_chart(self, job, end_time):
        self.gant_chart.append({job : end_time})

    def show_stats(self):
        for p in self.data:
            print(f"job: {p[0]} --> {p[1]}")
            print()
        print("len:", len(self.data))


class FCFSAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['arrival_time'])

    def calculate_completion_time(self, index):
        return super().calculate_completion_time(index)

    def calculate_waiting_time(self, index):
        return super().calculate_waiting_time(index)

    def calculate_turnaround_time(self, index):
        return super().calculate_turnaround_time(index)

    def calculate_computing_time(self, index):
        return super().calculate_computing_time(index)

    def calculate_avg_waiting_time(self):
        return super().calculate_avg_waiting_time()

    def calculate_avg_turnaround_time(self):
        return super().calculate_avg_turnaround_time()

    def calculate_avg_computing_time(self):
        return super().calculate_avg_computing_time()


class SJFAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['burst_time'])

    
    def calculate_completion_time(self, index):
        return super().calculate_completion_time(index)

    def calculate_waiting_time(self, index):
        return super().calculate_waiting_time(index)

    def calculate_turnaround_time(self, index):
        return super().calculate_turnaround_time(index)

    def calculate_computing_time(self, index):
        return super().calculate_computing_time(index)

    def calculate_avg_waiting_time(self):
        return super().calculate_avg_waiting_time()

    def calculate_avg_turnaround_time(self):
        return super().calculate_avg_turnaround_time()

    def calculate_avg_computing_time(self):
        return super().calculate_avg_computing_time()

class SRPTAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['arrival_time'])

        n = len(self.data)
        self.proc = []
        processes = self.proc

        for i in range(n):
            p = self.data[i]
            self.proc.append([i, p[1]['burst_time'], p[1]['arrival_time']]) # [id, burst, arrival]

        self.slice_time = []
        self.slice_job = []

        wt = [0] * n
        tat = [0] * n
     
        self.calc_wt(processes, n, wt)
        self.calc_tat(processes, n, wt, tat)

        for i in range(n):
            self.total_waiting_time = self.total_waiting_time + wt[i]
            self.total_turnaround_time = self.total_turnaround_time + tat[i]

        


        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['turnaround_time'])
        print('length:')
        print(len(self.slice_time))
        print(len(self.slice_job))
        


    def calc_wt(self, processes, n, wt):
        rt = [0] * n
     
        # Copy the burst time into rt[]
        for i in range(n):
            rt[i] = processes[i][1]
        complete = 0
        t = 0
        minm = 999999999
        short = 0
        check = False
        maxm = -9999999999
     
        while (complete != n):
             
            for j in range(n):
                if ((processes[j][2] <= t) and
                    (rt[j] < minm) and rt[j] > 0):
                    minm = rt[j]
                    short = j
                    check = True
                    # self.slice_time.append(t + minm)
                    self.slice_job.append(short)
                    if minm >= maxm-1:
                        self.slice_time.append(t + minm)
                        maxm = minm
                    #     self.slice_job.append(short)

                    print(minm)


            if (check == False):
                t += 1
                continue
                 
            rt[short] -= 1
            minm = rt[short]
            if (minm == 0):
                minm = 999999999
     
            if (rt[short] == 0):
                complete += 1
                check = False
                fint = t + 1
                wt[short] = (fint - self.proc[short][1] -   
                                    self.proc[short][2])
     
                if (wt[short] < 0):
                    wt[short] = 0
             
            t += 1
        
        for i in range(n):
            self.data[i][1]['waiting_time'] = wt[i]
     
    def calc_tat(self, processes, n, wt, tat):
        for i in range(n):
            tat[i] = processes[i][1] + wt[i]
            self.data[i][1]['turnaround_time'] = tat[i]
     
    def calculate_completion_time(self, index):
        pass

    def calculate_waiting_time(self, index):
        pass

    def calculate_turnaround_time(self, index):
        pass
    
    def calculate_computing_time(self, index):
        return super().calculate_computing_time(index)

    def calculate_avg_waiting_time(self):
        return super().calculate_avg_waiting_time()

    def calculate_avg_turnaround_time(self):
        return super().calculate_avg_turnaround_time()

    def calculate_avg_computing_time(self):
        return super().calculate_avg_computing_time()




class SRPTAlgo2(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

        self.data           = self.process
        for key, value in self.data.items():
            self.data[key]['cpu_remaining_time'] = value['burst_time']

        self.total_time = 0
        self.scheduled = None
        self.queue = []
        self.completed = 0

        while self.completed != len(self.data):
            if not self.scheduled:
                for j, v in self.data.items():
                    if self.total_time == v['arrival_time']:
                        self.scheduled = j
                        self.total_time = v['arrival_time']

                        break
            else:
                if self.data[self.scheduled]['cpu_remaining_time'] == 0:
                    self.data[self.scheduled]['completion_time'] = self.total_time
                    self.completed += 1
                    self.scheduled = None

                    # check new arrival
                    for j, v in self.data.items():
                        if self.total_time == v['arrival_time']:
                            self.scheduled = j
                            break

                    # check if new self.scheduled is lower than in the self.queue
                    if self.scheduled and self.queue:
                        self.queue.append(self.scheduled)
                        self.scheduled = None

                    if not self.scheduled and self.queue:
                        self.queue.sort()
                        value = float('inf')
                        for j in self.queue:
                            if self.data[j]['cpu_remaining_time'] < value:
                                value = self.data[j]['cpu_remaining_time']
                                self.scheduled = j
                        self.queue.remove(self.scheduled)
                    
                else:
                    # check new arrival
                    for j, v in self.data.items():
                        if self.total_time == v['arrival_time']:
                            if self.data[self.scheduled]['cpu_remaining_time'] < v['cpu_remaining_time']:
                                self.queue.append(j)
                            elif self.data[self.scheduled]['cpu_remaining_time'] == v['cpu_remaining_time']:
                                if self.data[self.scheduled]['arrival_time'] < v['arrival_time']:
                                    self.queue.append(j)
                                else:
                                    self.queue.append(self.scheduled)
                                    self.scheduled = j
                            else:
                                self.queue.append(self.scheduled)
                                self.scheduled = j
                            break
            
            if self.scheduled:
                self.total_time += 1
                self.data[self.scheduled]['cpu_remaining_time'] -= 1

        self.data           = sorted(list(self.data.items()), key=lambda x: x[1]['completion_time'])

    def calculate_completion_time(self, index):
        pass

    def calculate_turnaround_time(self, index):
        self.data[index][1]['turnaround_time'] = self.data[index][1]['completion_time'] - self.data[index][1]['arrival_time']
        self.total_turnaround_time          += self.data[index][1]['turnaround_time']

    def calculate_waiting_time(self, index):
        return super().calculate_waiting_time(index)

    def calculate_computing_time(self, index):
        return super().calculate_computing_time(index)



class PriorityAlgo(SchedulingAlgorithm):
    def __init__(self, process):
        super().__init__(process)

        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['priority'])

    def calculate_completion_time(self, index):
        return super().calculate_completion_time(index)

    def calculate_waiting_time(self, index):
        return super().calculate_waiting_time(index)

    def calculate_turnaround_time(self, index):
        return super().calculate_turnaround_time(index)

    def calculate_computing_time(self, index):
        return super().calculate_computing_time(index)

    def calculate_avg_waiting_time(self):
        return super().calculate_avg_waiting_time()

    def calculate_avg_turnaround_time(self):
        return super().calculate_avg_turnaround_time()

    def calculate_avg_computing_time(self):
        return super().calculate_avg_computing_time()





class RoundRobinAlgo(SchedulingAlgorithm):
    def __init__(self, process, QUANTUM = 4):
        super().__init__(process)

        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['arrival_time'])

        count = len(self.data)
        burst_time = []

        for j in self.data:
            burst_time.append(j[1]['burst_time'])

        self.slice_time = []
        self.slice_job = []

        waiting_time = [0] * count
        turnaround_time = [0] * count
     
        self.calc_wt(count, burst_time, waiting_time, QUANTUM)
        self.calc_tat(count, burst_time, waiting_time, turnaround_time)
     
        for i in range(count):
            self.total_waiting_time = self.total_waiting_time + waiting_time[i]
            self.total_turnaround_time = self.total_waiting_time + turnaround_time[i]

        self.data = sorted(list(self.process.items()), key=lambda x: x[1]['turnaround_time'])


    def calc_wt(self, job_count, burst_time, waiting_time, QUANTUM):
        remaining_burst_time = [0] * job_count
     
        for i in range(job_count):
            remaining_burst_time[i] = burst_time[i]
        TIME = 0 
     
        while True:
            done = True
     
            for i in range(job_count):
                if (remaining_burst_time[i] > 0) :
                    done = False 
                    if (remaining_burst_time[i] > QUANTUM) :
                        TIME += QUANTUM
                        self.slice_time.append(TIME)
                        self.slice_job.append(i)
                        remaining_burst_time[i] -= QUANTUM
                    else:
                        TIME = TIME + remaining_burst_time[i]
                        waiting_time[i] = TIME - burst_time[i]
                        self.data[i][1]['waiting_time'] = waiting_time[i]
                        remaining_burst_time[i] = 0
                     
            if (done == True):
                break
                 
    def calc_tat(self, n, burst_time, waiting_time, turnaround_time):
        for i in range(n):
            turnaround_time[i] = burst_time[i] + waiting_time[i]
            self.data[i][1]['turnaround_time'] = turnaround_time[i]


    def calculate_completion_time(self, index):
        pass

    def calculate_waiting_time(self, index):
        pass

    def calculate_turnaround_time(self, index):
        pass
    
    def calculate_computing_time(self, index):
        return super().calculate_computing_time(index)

    def calculate_avg_waiting_time(self):
        return super().calculate_avg_waiting_time()

    def calculate_avg_turnaround_time(self):
        return super().calculate_avg_turnaround_time()

    def calculate_avg_computing_time(self):
        return super().calculate_avg_computing_time()

