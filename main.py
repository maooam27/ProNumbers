from tkinter import *


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
title = Label(text="ProNumbers", font=("Ubuntu", 26, "bold"), bg=bgc, fg=fgc_light)
title.pack(padx=10, pady=3, anchor="nw")

subtitle = Label(text="Choose what kind of conversion you wish to do", font=("Ubuntu", 20, "italic"), bg=bgc, fg=fgc)
subtitle.pack(padx=10, pady=5, anchor="nw")


# TODO: choosing list here

if __name__ == "__main__":
    root.mainloop()
