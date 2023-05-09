import tkinter
import tkinter.messagebox, tkinter.filedialog
import customtkinter as ctk
from tkinter import ttk
import inspect, os

import styles, treeview, frame, tabview
import scheduling_algorithms

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.PROCESS    = {}
        self.QUANTUM    = 4



        self.title("Machine Problem 2 – On Processor Management and Job Scheduling")
        self.geometry(f"{1366}x{768}") 


        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1, 2), weight=1)


        self.style   = styles.treeview_theme()


        # create sidebar frame with widgets
        self.frames = frame.create_frame(self)

        self.labels = {}
        
        self.labels['logo']         = ctk.CTkLabel(self.frames['left'], text="Input", font=ctk.CTkFont(size=20, weight="bold"))
        self.labels['logo'].grid(row=0, column=0, padx=20, pady=(20, 10))
        self.labels['output']         = ctk.CTkLabel(self, text="Output", font=ctk.CTkFont(size=20, weight="bold"))
        self.labels['output'].grid(row=0, column=1, sticky="n", pady=(20, 0))
        self.labels['output'].grid_columnconfigure(0, weight=0)

        self.buttons = {}

        self.buttons['input_process']   = ctk.CTkButton(self.frames['left'], text="Open Process File", command=self.open_input_dialog_process)
        self.buttons['clear_process_process']   = ctk.CTkButton(self.frames['left'], text="Clear Input Process", command=self.clear_treeview_data)

        self.buttons['input_process'].grid(row=1, column=0, padx=20, pady=10)
        self.buttons['clear_process_process'].grid(row=2, column=0, padx=20, pady=10)


        self.sidebar_button_3   = ctk.CTkButton(self.frames['left'], command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        
        # treeview table
        self.input_process_tree     = treeview.create_tableview(self.frames['right'])
        treeview.modify(self.input_process_tree)

        # create tabview
        self.tabview            = tabview.create_tabview(self)
        tabview.modify(self.tabview)
        
        self.treeview_algos = {}
        for tv_a in ('FCFS', 'SJF', 'SRPT', 'Priority', 'Round-Robin'):
            self.treeview_algos[tv_a] = treeview.SchedulingTable(self.tabview.tab(tv_a))


        self.combobox_1 = ctk.CTkComboBox(self.tabview.tab("FCFS"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = ctk.CTkButton(self.tabview.tab("FCFS"), text="Open CTkInputDialog",
                                                           command=self.haha)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))




        
    def haha(self):
        for p in self.PROCESS:
            print(self.PROCESS[p])


    def open_input_dialog_process(self):
        process_file    = tkinter.filedialog.askopenfilename()
        print("Dialog:", process_file)
        console_debug(inspect.stack()[0][3], process_file)

        self.PROCESS    = extract_data_from_process_file(process_file)
        console_debug(inspect.stack()[0][3], f"Stored data to self.PROCESS")

        self.clear_treeview_data()

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


    def clear_treeview_data(self):
        for item in self.input_process_tree.get_children():
            self.input_process_tree.delete(item)
        console_debug(inspect.stack()[0][3], "Cleared data for self.input_process_tree")



    def sidebar_button_event(self):
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
