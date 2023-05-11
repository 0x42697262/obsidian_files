import customtkinter as ctk
from tkinter import ttk

def create_tabview(parent):
    tab            = ctk.CTkTabview(parent, width=250)
    tab.grid(row=1, column=1, rowspan=14, padx=(20, 0), pady=(20, 20), sticky="nsew")

    return tab


def modify(tabview):
    tabview_tabs = ["FCFS", "SJF", "SRPT", "Priority", "Round-Robin"]
    for tab in tabview_tabs:
        tabview.add(tab)

    tabview.tab("FCFS").grid_rowconfigure(0, weight=1)  
    tabview.tab("SJF").grid_rowconfigure(0, weight=1)
    tabview.tab("SRPT").grid_rowconfigure(0, weight=1)
    tabview.tab("Priority").grid_rowconfigure(0, weight=1)
    tabview.tab("Round-Robin").grid_rowconfigure(0, weight=1)

    tabview.tab("FCFS").grid_columnconfigure(0, weight=1)  
    tabview.tab("SJF").grid_columnconfigure(0, weight=1)
    tabview.tab("SRPT").grid_columnconfigure(0, weight=1)
    tabview.tab("Priority").grid_columnconfigure(0, weight=1)
    tabview.tab("Round-Robin").grid_columnconfigure(0, weight=1)

    return tabview
