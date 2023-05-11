import customtkinter as ctk
from tkinter import ttk

def create_frame(parent):
    frame = {}

    frame['left']         = ctk.CTkFrame(parent, width=140, corner_radius=0)
    frame['right']        = ctk.CTkFrame(parent, width=350)
    frame['gant_chart']   = ctk.CTkFrame(parent)

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
    frame['gant_chart'].grid(
            row     = 1, 
            column  = 1, 
            rowspan = 2,
            sticky  = "nsew",
            padx        = (20, 20), 
            pady        = (20, 20), 
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


class GantChart:
    def __init__(self, parent):
        self.frames = {}

        for i in range(30):
                self.frames[i] = ctk.CTkFrame(parent, height=50, width=50, corner_radius=0,border_width=1, border_color='#FF0090', fg_color='#5080CC')
                self.frames[i].grid(
                                row=(i//10)+1,
                                column=(i%10)+1,
                                sticky="nw",
                                )
                self.frames[i].grid_rowconfigure(1, weight=1)
                self.frames[i].grid_columnconfigure(3, weight=1)
                self.process_text = ctk.CTkLabel(self.frames[i], text=f"P{i}")
                self.process_text.grid(row=0, column=3, sticky="nsew", padx=(10,10), pady=(10, 10))
                # self.process_text.grid_rowconfigure(1, weight=1)
                # self.process_text.grid_columnconfigure(1, weight=1)
                self.time_text = ctk.CTkLabel(self.frames[i], text=f"{i}")
                self.time_text.grid(row=1, column=0, sticky="nsew", padx=(10,10), pady=(10, 10))

                # self.time_text.grid_rowconfigure(1, weight=1)
                # self.time_text.grid_columnconfigure(1, weight=1)
                self.time_text2 = ctk.CTkLabel(self.frames[i], text=f"{i+100}")
                self.time_text2.grid(row=1, column=5, sticky="nsew", padx=(10,10), pady=(10, 10))

        



