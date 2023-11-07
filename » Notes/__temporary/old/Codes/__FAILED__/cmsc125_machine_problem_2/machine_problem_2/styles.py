import tkinter.ttk as ttk

def treeview_theme():
    style = ttk.Style()
    style.theme_create(
            "dark", 
            parent="alt", 
            settings={
                "Treeview": {
                    "configure": {"background": "#2d2d2d", "foreground": "white", "rowheight": 25, "fieldbackground": "#2d2d2d"},
                    "map": {"background": [("selected", "#3c3c3c")], "foreground": [("selected", "white")]}
                    },
                "Treeview.Heading": {
                    "configure": {"background": "#2d2d2d", "foreground": "white", "padding": [10, 5]}},
                },
            )
    
    style.theme_use("dark")

    return style
    
