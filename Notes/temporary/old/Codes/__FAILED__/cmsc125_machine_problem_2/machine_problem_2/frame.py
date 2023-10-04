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


class GantChart:
    def __init__(self, parent, count, right_value = [], jobs = []):
        self.frames = {}

        for i in range(count):
            self.frames[i] = ctk.CTkFrame(parent, height=5, width=5, corner_radius=0, border_width=1, border_color='#FF0090', fg_color='#5080CC')
            self.frames[i].grid(row=(i//10)+1, column=(i%10)+1, sticky="nsew")
            self.frames[i].grid_rowconfigure(0, weight=0)
            self.frames[i].grid_columnconfigure(0, weight=1)

            # Add a box to the frame
            box = ctk.CTkFrame(self.frames[i], bg_color='blue', fg_color='#900040', border_width=1)
            box.grid(row=0, column=0, sticky="nsew")
            box.grid_rowconfigure(0, weight=1)
            box.grid_columnconfigure(0, weight=1)

            # Add a label to the box for the process ID
            process_text = ctk.CTkLabel(box, text=f"P{jobs[i]}", font=("Arial", 20), height=25, width=25)
            process_text.place(relx=0.5, rely=0.5, anchor="center")

            if i == 0:
                    # Add a label to the box for the start time
                    start_time_text = ctk.CTkLabel(box, text=f"0", font=("Arial", 20))
                    start_time_text.place(relx=0.05, rely=0.9, anchor="sw")

            # Add a label to the box for the end time
            end_time_text = ctk.CTkLabel(box, text=f"{right_value[i]}", font=("Arial", 20))
            end_time_text.place(relx=0.95, rely=0.9, anchor="se")

        # Configure the rows and columns of the parent frame
        for i in range(10):
            parent.grid_rowconfigure(i, weight=1)
            parent.grid_columnconfigure(i, weight=1)

        

