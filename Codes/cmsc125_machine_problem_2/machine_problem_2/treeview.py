from tkinter import ttk
import customtkinter as ctk

def create_tableview(parent):
    table     = ttk.Treeview(parent, show='headings')
    table.grid(
            row     = 0, 
            column  = 0, 
            rowspan = 14,  
            sticky  = "nsew",
            padx    = (20, 20),
            pady    = (20, 20),
            )

    return table

def modify(table):
    table['columns']  = ("Job", "Arrival Time", "CPU Burst Time", "Priority")
    for c in table['columns']:
        table.heading(c, text=c)

    table.column('Job',             width=48,   anchor=ctk.CENTER)
    table.column('Arrival Time',    width=100,  anchor=ctk.CENTER)
    table.column('CPU Burst Time',  width=120,  anchor=ctk.CENTER)
    table.column('Priority',        width=65,   anchor=ctk.CENTER)


    return table


class SchedulingTable:
    def __init__(self, parent):
        self.table = ttk.Treeview(parent, show='headings')
        self.table.grid(
                row     = 0, 
                column  = 0, 
                sticky  = "nsew",
                padx    = (20, 20),
                pady    = (20, 20),
                )

        self.table['columns']   = ("Job","Arrival Time (ms)", "CPU Burst Time (ms)", "Priority (ms)", "Turnaround Time (ms)", "Waiting Time (ms)", "Computing Time (ms)")
        for c in self.table['columns']:
            self.table.heading(c, text=c)

        self.table.column('Job',                    width=48,   anchor=ctk.CENTER)
        self.table.column('Arrival Time (ms)',      width=98,   anchor=ctk.CENTER)
        self.table.column('CPU Burst Time (ms)',    width=168,   anchor=ctk.CENTER)
        self.table.column('Priority (ms)',          width=108,   anchor=ctk.CENTER)
        self.table.column('Turnaround Time (ms)',   width=168,  anchor=ctk.CENTER)
        self.table.column('Waiting Time (ms)',      width=98,   anchor=ctk.CENTER)
        self.table.column('Computing Time (ms)',    width=128,  anchor=ctk.CENTER)

