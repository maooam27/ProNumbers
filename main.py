from tkinter import *
from tkinter import ttk

# TODO: optimize imports

# Main colors, background and foreground
bgc = "#232A2F"
bgc_light = "#2B3338"
fgc = "#bfbfbf"
fgc_light = "#d0d0d0"

# Functions

def openWindow(s: str):
    if s == "Temperatures":
        window = Tk()
        window.title(f"{s} conversions")
        window.geometry("800x600")
        window.resizable(False, False)
        window.configure(bg=bgc)
    elif s == "Distances":
        window = Tk()
        window.title(f"{s} conversions")
        window.geometry("800x600")
        window.resizable(False, False)
        window.configure(bg=bgc)
    elif s == "Pressure":
        window = Tk()
        window.title(f"{s} conversions")
        window.geometry("800x600")
        window.resizable(False, False)
        window.configure(bg=bgc)
    elif s == "Power":
        window = Tk()
        window.title(f"{s} conversions")
        window.geometry("800x600")
        window.resizable(False, False)
        window.configure(bg=bgc)
    else:
        return


# Make root window
root = Tk()
root.title("ProNumbers - Converting values <3")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg=bgc)

# Asking for user input
title = ttk.Label(root, text="ProNumbers", font=("Ubuntu", 26, "bold"), foreground=fgc_light, background=bgc)
title.pack(padx=10, pady=3, anchor="nw")

subtitle = ttk.Label(root, text="Choose what kind of conversion you wish to do", font=("Ubuntu", 20, "italic"), background=bgc, foreground=fgc)
subtitle.pack(padx=10, pady=5, anchor="nw")


# TODO: choosing list here
selectedCategory = ttk.Combobox(root)
selectedCategory['values'] = ("Temperatures", "Distances", "Pressure", "Power")
selectedCategory.pack(padx=10, pady=20)

def cambiato():
    print("dd")

# TODO: find error

selectedCategory.bind("<<ComboboxSelected>>", cambiato) #openWindow(selectedCategory.get()))

if __name__ == "__main__":
    root.mainloop()
