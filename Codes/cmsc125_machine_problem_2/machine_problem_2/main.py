import tkinter
import tkinter.messagebox, tkinter.filedialog
import customtkinter as ctk
from tkinter import ttk
import inspect, os

import styles, treeview, frame, tabview
import scheduling

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.PROCESS    = {}
        self.QUANTUM    = 4

        self.algorithms = ('FCFS', 'SJF', 'SRPT', 'Priority', 'Round-Robin')



        self.title("Machine Problem 2 – On Processor Management and Job Scheduling")
        self.geometry(f"{1716}x{768}") 


        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1, 2), weight=1)


        self.style   = styles.treeview_theme()


        # create sidebar frame with widgets
        self.frames = frame.create_frame(self)

        self.labels = {}
        
        self.labels['input']         = ctk.CTkLabel(self.frames['left'], text="Input", font=ctk.CTkFont(size=20, weight="bold"))
        self.labels['input'].grid(row=0, column=0, padx=20, pady=(20, 10))
        self.labels['output']         = ctk.CTkLabel(self, text="Output", font=ctk.CTkFont(size=20, weight="bold"))
        self.labels['output'].grid(row=0, column=1, sticky="n", pady=(20, 0))
        self.labels['output'].grid_columnconfigure(0, weight=0)

        self.buttons = {}

        self.buttons['input_process']           = ctk.CTkButton(self.frames['left'], text="Open Process File",      command=self.open_input_dialog_process)
        self.buttons['clear_process_process']   = ctk.CTkButton(self.frames['left'], text="Clear Input Process",    command=self.clear_treeview_data)
        self.buttons['calculate']               = ctk.CTkButton(self.frames['left'], text="Calculate",              command=self.calculate)

        self.buttons['input_process'].grid(row=1, column=0, padx=20, pady=10)
        self.buttons['clear_process_process'].grid(row=2, column=0, padx=20, pady=10)
        self.buttons['calculate'].grid(row=3, column=0, padx=20, pady=10)


        self.sidebar_button_3   = ctk.CTkButton(self.frames['left'], command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)

        
        # treeview table
        self.input_process_tree     = treeview.create_tableview(self.frames['right'])
        treeview.modify(self.input_process_tree)
        def item_selected(event):
            for tv_a in self.algorithms:
                self.treeview_algos[tv_a].table.selection_set(self.input_process_tree.selection())
        self.input_process_tree.bind('<<TreeviewSelect>>', item_selected)

        # create tabview
        self.tabview            = tabview.create_tabview(self)
        tabview.modify(self.tabview)
        
        self.treeview_algos = {}
        for tv_a in self.algorithms:
            self.treeview_algos[tv_a] = treeview.SchedulingTable(self.tabview.tab(tv_a))

        self.scheduling_algorithms = {}

        


    def open_input_dialog_process(self):
        self.clear_treeview_data()

        process_file    = tkinter.filedialog.askopenfilename()
        print("Dialog:", process_file)
        console_debug(inspect.stack()[0][3], process_file)

        self.PROCESS    = extract_data_from_process_file(process_file)
        console_debug(inspect.stack()[0][3], f"Stored data to self.PROCESS")


        for p in self.PROCESS:
            self.input_process_tree.insert(
                    '', 
                    'end', 
                    values=(
                        p, 
                        self.PROCESS[p]['arrival_time'], 
                        self.PROCESS[p]['burst_time'], 
                        self.PROCESS[p]['priority']
                        )
                    )
        console_debug(inspect.stack()[0][3], "Inserted data of self.PROCESS to self.input_process_tree")


    def calculate(self):
        self.scheduling_algorithms['FCFS']          = scheduling.FCFSAlgo(self.PROCESS)
        self.scheduling_algorithms['SJF']           = scheduling.SJFAlgo(self.PROCESS)
        self.scheduling_algorithms['SRPT']          = scheduling.SRPTAlgo(self.PROCESS)
        self.scheduling_algorithms['Priority']      = scheduling.PriorityAlgo(self.PROCESS)
        self.scheduling_algorithms['Round-Robin']   = scheduling.RoundRobinAlgo(self.PROCESS)

        console_debug(inspect.stack()[0][3], "Copied data of self.PROCESS to self.scheduling_algorithms")

        # calculate
        for algo in self.algorithms:
            for index in range(len(self.scheduling_algorithms[algo].data)):
                self.scheduling_algorithms[algo].calculate_waiting_time(index)
                self.scheduling_algorithms[algo].calculate_turnaround_time(index)
                self.scheduling_algorithms[algo].calculate_computing_time(index)


        # place
        for algo in self.algorithms:
            for p in self.scheduling_algorithms[algo].data:
                self.treeview_algos[algo].table.insert(
                        '',
                        'end',
                        values = (
                            p[0], # job
                            p[1]['arrival_time'],
                            p[1]['burst_time'],
                            p[1]['priority'],
                            p[1]['waiting_time'],
                            p[1]['turnaround_time'],
                            p[1]['computing_time'],
                            )
                        )
            self.treeview_algos[algo].table.insert(
                        '',
                        'end',
                        values = (
                            'avg',
                            '-',
                            '-',
                            '-',
                            self.scheduling_algorithms[algo].calculate_avg_turnaround_time(),
                            self.scheduling_algorithms[algo].calculate_avg_waiting_time(),
                            self.scheduling_algorithms[algo].calculate_avg_computing_time(),
                            )
                        )

            console_debug(inspect.stack()[0][3], f"Copied data of self.scheduling_algorithms[{algo}].data to self.treeview_algos[{algo}].table")


    def clear_treeview_data(self):
        self.PROCESS = {}
        console_debug(inspect.stack()[0][3], "Cleared data for self.PROCESS")

        for item in self.input_process_tree.get_children():
            self.input_process_tree.delete(item)
        console_debug(inspect.stack()[0][3], "Cleared data for self.input_process_tree")

        for sa in self.scheduling_algorithms:
            self.scheduling_algorithms[sa].data = []
        console_debug(inspect.stack()[0][3], "Cleared data for self.scheduling_algorithms")

        # dont forget to clear the treeviews in tabview
        for algo in self.algorithms:
            for item in self.treeview_algos[algo].table.get_children():
                self.treeview_algos[algo].table.delete(item)
            console_debug(inspect.stack()[0][3], f"Cleared data for self.treeview_algos[{algo}]")








    def sidebar_button_event(self):
        for sa in self.algorithms:
            self.scheduling_algorithms[sa].show_stats()

        console_debug(inspect.stack()[0][3], "Clicked!")






def console_debug(function, message: str = ""):
    print(f"{function}()\n--------> {message}")
    print()


def extract_data_from_process_file(file: str) -> dict: 
    raw_data    = None
    with open(file) as f:
        raw_data = f.readlines()
    console_debug(inspect.stack()[0][3], f"Read contents of a file ({os.path.getsize(file)} bytes)")


    contents    = {}
    for i in range(1, len(raw_data)):
        split           = raw_data[i].strip('\n').split('\t')
        clean_strip     = [int(s) for s in split if s.strip()] 
        contents[clean_strip[0]]   = {
                "arrival_time"  : clean_strip[1],
                "burst_time"    : clean_strip[2],
                "priority"      : clean_strip[3],
                }

        console_debug(inspect.stack()[0][3], f"Stored {clean_strip} to contents[{clean_strip[0]}]")

    return contents



if __name__ == "__main__":
    app = App()
    app.mainloop()
