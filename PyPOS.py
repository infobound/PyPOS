import Global.Settings as Settings
import Global.Functions as Functions
from Forms.formTopLevel import formTopLevel
import Data.DB as posDB

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


#init settings
def main():
    print("Starting PyPOS...")

    print("Loading Settings...")

    Settings.LoadSettings()

    print("Connecting to Database...")

    print("to do: code to use mssql and flat files")

    posDB.Open()

    print("Connecting to Central Processing Server...")
    print("to do: Central Processing Server")

    print("Starting Interface...")
    
    print("USB:")
    Functions.GetAllUSBDevices()


    root=tk.Tk()
    tl=formTopLevel(top=root)
    root.mainloop()

if __name__ == "__main__":
    main()

