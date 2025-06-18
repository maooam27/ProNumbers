from tkinter import *
from tkinter import ttk


# Main colors, background and foreground
bgc = "#232A2F"
bgc_light = "#2B3338"
fgc = "#bfbfbf"
fgc_light = "#d0d0d0"

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
country = ttk.Combobox(root)
country['values'] = ("usa", "italy", "europe", "yay")
country.pack()

# country.state(["readonly"]) to make it read-only

get_data = ttk.Button(text="get data", command=lambda: print(country.get()))
get_data.pack()

if __name__ == "__main__":
    root.mainloop()
