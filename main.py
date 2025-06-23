from tkinter import *
from tkinter import ttk

# TODO: optimize imports

# Main colors, background and foreground
bgc = "#232A2F"
bgc_light = "#2B3338"
fgc = "#bfbfbf"
fgc_light = "#d0d0d0"


class TemperatureWindow:
    def __init__(self):
        window = Tk()
        window.title("Temperatures conversions")
        window.geometry("800x600")
        window.resizable(False, False)
        window.configure(bg=bgc)
        
        title = ttk.Label(window, text="Temperature", font=("Ubuntu", 26, "bold"), foreground=fgc_light, background=bgc)
        title.pack(padx=10, pady=3, anchor="nw")

        subtitle = ttk.Label(window, text="Insert your data", font=("Ubuntu", 20, "italic"), background=bgc, foreground=fgc)
        subtitle.pack(padx=10, pady=5, anchor="nw")
        
        # Frame
        conversionFrame = Frame(window, background=bgc)
        conversionFrame.pack(padx=10, pady=10)
        
        # Widgets
        self.celsius = StringVar()
        celsiusLabel = ttk.Label(conversionFrame, text="Celsius", font=("Ubuntu", 16), background=bgc, foreground=fgc_light)
        celsiusLabel.grid(padx=2, pady=5, row=0, column=0)
        self.celsiusEntry = ttk.Entry(conversionFrame, textvariable=self.celsius)
        self.celsiusEntry.grid(padx=2, pady=5, row=0, column=1)
        
        self.kelvin = StringVar()
        kelvinLabel = ttk.Label(conversionFrame, text="Kelvin", font=("Ubuntu", 16), background=bgc, foreground=fgc_light)
        kelvinLabel.grid(padx=2, pady=5, row=1, column=0)
        self.kelvinEntry = ttk.Entry(conversionFrame, textvariable=self.kelvin)
        self.kelvinEntry.grid(padx=2, pady=5, row=1, column=1)
        
        self.farenheit = StringVar()
        farenheitLabel = ttk.Label(conversionFrame, text="Farenheit", font=("Ubuntu", 16), background=bgc, foreground=fgc_light)
        farenheitLabel.grid(padx=2, pady=5, row=2, column=0)
        self.farenheitEntry = ttk.Entry(conversionFrame, textvariable=self.farenheit)
        self.farenheitEntry.grid(padx=2, pady=5, row=2, column=1)
        
        # Events: when changing a value -> update celsius -> update everything else based on celsius conversion
        self.farenheitEntry.bind("<KeyRelease>", self.farenheitChanged)
        self.celsiusEntry.bind("<KeyRelease>", self.celsiusChanged)
        self.kelvinEntry.bind("<KeyRelease>", self.kelvinChanged)
        
        # TODO: fix conversion and errors
        
    def farenheitChanged(self, *args):
        try:
            self.celsiusEntry.delete(0, 'end')
            self.kelvinEntry.delete(0, "end")
            cConverted = (int(self.farenheitEntry.get()) - 32) / (9/5)
            self.celsiusEntry.insert(0, str(cConverted))
            kConverted = cConverted + 273.15
            self.kelvinEntry.insert(0, str(kConverted))
        except Exception as e:
            print(e)
            return
        
    def celsiusChanged(self, *args):
        try:
            self.farenheitEntry.delete(0, 'end')
            self.kelvinEntry.delete(0, "end")
            kConverted = int(self.celsiusEntry.get()) + 273.15
            self.kelvinEntry.insert(0, str(kConverted))
            fConverted = (kConverted - 273.15) * (9/5) + 32
            self.farenheitEntry.insert(0, str(fConverted))
        except Exception as e:
            print(e)
            return
        
    def kelvinChanged(self, *args):
        try:
            self.celsiusEntry.delete(0, 'end')
            self.farenheitEntry.delete(0, "end")
            cConverted = int(self.kelvinEntry.get()) - 273.15
            self.celsiusEntry.insert(0, str(cConverted))
            fConverted = (cConverted * 9/5) + 32
            self.farenheitEntry.insert(0, str(fConverted))
        except Exception as e:
            print(e)
            return

        

class DistanceWindow:
    def __init__(self):
        window = Tk()
        window.title("Distances conversions")
        window.geometry("800x600")
        window.resizable(False, False)
        window.configure(bg=bgc)
        
        title = ttk.Label(window, text="Distance", font=("Ubuntu", 26, "bold"), foreground=fgc_light, background=bgc)
        title.pack(padx=10, pady=3, anchor="nw")

        subtitle = ttk.Label(window, text="Insert your data", font=("Ubuntu", 20, "italic"), background=bgc, foreground=fgc)
        subtitle.pack(padx=10, pady=5, anchor="nw")
        
        # Frame
        conversionFrame = Frame(window, background=bgc)
        conversionFrame.pack(padx=10, pady=10)
        
        # Widgets
        self.meter = StringVar()
        meterLabel = ttk.Label(conversionFrame, text="Meters", font=("Ubuntu", 16), background=bgc, foreground=fgc_light)
        meterLabel.grid(padx=2, pady=5, row=0, column=0)
        self.meterEntry = ttk.Entry(conversionFrame, textvariable=self.meter)
        self.meterEntry.grid(padx=2, pady=5, row=0, column=1)
        
        self.foot = StringVar()
        footLabel = ttk.Label(conversionFrame, text="Feet", font=("Ubuntu", 16), background=bgc, foreground=fgc_light)
        footLabel.grid(padx=2, pady=5, row=1, column=0)
        self.footEntry = ttk.Entry(conversionFrame, textvariable=self.foot)
        self.footEntry.grid(padx=2, pady=5, row=1, column=1)
        
        self.yard = StringVar()
        yardLabel = ttk.Label(conversionFrame, text="Yards", font=("Ubuntu", 16), background=bgc, foreground=fgc_light)
        yardLabel.grid(padx=2, pady=5, row=2, column=0)
        self.yardEntry = ttk.Entry(conversionFrame, textvariable=self.yard)
        self.yardEntry.grid(padx=2, pady=5, row=2, column=1)
        
        # Events: when changing a value -> update celsius -> update everything else based on celsius conversion
        self.yardEntry.bind("<KeyRelease>", self.yardChanged)
        self.meterEntry.bind("<KeyRelease>", self.meterChanged)
        self.footEntry.bind("<KeyRelease>", self.footChanged)
        
    def yardChanged(self, *args):
        try:
            self.meterEntry.delete(0, 'end')
            self.footEntry.delete(0, "end")
            mConverted = (float(self.yardEntry.get())) / 1.094
            self.meterEntry.insert(0, str(mConverted))
            fConverted = float(self.yardEntry.get()) * 3
            self.footEntry.insert(0, str(fConverted))
        except Exception as e:
            print(e)
            return
        
    def meterChanged(self, *args):
        try:
            self.yardEntry.delete(0, 'end')
            self.footEntry.delete(0, "end")
            fConverted = float(self.meterEntry.get()) * 3.281
            self.footEntry.insert(0, str(fConverted))
            yConverted = (fConverted) / 3
            self.yardEntry.insert(0, str(yConverted))
        except Exception as e:
            print(e)
            return
        
    def footChanged(self, *args):
        try:
            self.meterEntry.delete(0, 'end')
            self.yardEntry.delete(0, "end")
            mConverted = float(self.footEntry.get()) / 3.281
            self.meterEntry.insert(0, str(mConverted))
            yConverted = float(self.footEntry.get()) / 3
            self.yardEntry.insert(0, str(yConverted))
        except Exception as e:
            print(e)
            return


''' To be added in future
class PressureWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Pressures conversions")
        self.window.geometry("800x600")
        self.window.resizable(False, False)
        self.window.configure(bg=bgc)
        
        
class PowerWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Powers conversions")
        self.window.geometry("800x600")
        self.window.resizable(False, False)
        self.window.configure(bg=bgc)
'''


# Functions

def openWindow(event):
    s = selectedCategory.get()
    if s == "Temperatures":
        window = TemperatureWindow()
    elif s == "Distances":
        window = DistanceWindow()
    #elif s == "Pressure":
    #    window = PressureWindow()
    #elif s == "Power":
    #    window = PowerWindow()
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
selectedCategory = ttk.Combobox(root, state="readonly")
selectedCategory['values'] = ("Temperatures", "Distances") #, "Pressure", "Power")
selectedCategory.current(0)
selectedCategory.pack(padx=10, pady=20)

selectedCategory.bind('<<ComboboxSelected>>', openWindow)

if __name__ == "__main__":
    root.mainloop()
