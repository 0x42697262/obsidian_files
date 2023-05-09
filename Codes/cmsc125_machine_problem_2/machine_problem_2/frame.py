import customtkinter as ctk
from tkinter import ttk

def create_frame(parent):
    frame = {}

    frame['left']         = ctk.CTkFrame(parent, width=140, corner_radius=0)
    frame['right']        = ctk.CTkFrame(parent, width=350)

    frame['left'].grid(
            row     = 0, 
            column  = 0, 
            rowspan = 14,  
            sticky  = "nsew",
            )
    frame['right'].grid(
            row         = 0, 
            column      = 2, 
            columnspan  = 2, 
            rowspan     = 14, 
            padx        = (20, 20), 
            pady        = (20, 20), 
            sticky      = "nsew",
            )

    frame['left'].grid_rowconfigure(
            14, 
            weight  = 1,
            )
    frame['right'].grid_rowconfigure(
            0, 
            weight  = 1,)
    frame['right'].grid_columnconfigure(
            0, 
            weight  = 1,)

    return frame
