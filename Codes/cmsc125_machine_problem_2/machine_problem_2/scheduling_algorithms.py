class SchedulingAlgorithm:
    def __init__(self):
        self.arrival_time       = []
        self.burst_time         = []
        self.priority           = []
        self.started            = []
        self.completion         = []
        self.turnaround_time    = []
        self.waiting_time       = []
        self.computing_time     = []

        self.data = {
                "job"               : -1,
                "arrival_time"      : 0,
                "burst_time"        : 0,
                "priority"          : 0,
                "started"           : 0,
                "completion"        : 0,
                "turnaround_time"   : 0.0,
                "waiting_time"      : 0.0,
                "computing_time"    : 0.0,
                }


    def a(self):
        pass
