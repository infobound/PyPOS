import Global.Settings as Settings
import Global.Functions as Functions
from Forms.formTopLevel import formTopLevel
import Data.DB as posDB
import Hardware.Hardware
import Forms.formRegister_support as codeReg


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

    #print("Initializing Hardware:")
    #objUSB=Functions.GetAllUSBDevices()
    #objUSB=[
    #    {'id': b'1d6b:0002', 'tag': b'Linux Foundation 2.0 root hub', 'device': "/dev/bus/usb/b'001'/b'001'"}, 
    #    {'id': b'0e0f:0008', 'tag': b'VMware, Inc. ', 'device': "/dev/bus/usb/b'002'/b'005'"}, 
    #    {'id': b'0e0f:0002', 'tag': b'VMware, Inc. Virtual USB Hub', 'device': "/dev/bus/usb/b'002'/b'003'"}, 
    #    {'id': b'0e0f:0003', 'tag': b'VMware, Inc. Virtual Mouse', 'device': "/dev/bus/usb/b'002'/b'002'"}, 
    #    {'id': b'1d6b:0001', 'tag': b'Linux Foundation 1.1 root hub', 'device': "/dev/bus/usb/b'002'/b'001'"}
    #]
    #SystemHardware=Hardware()
    #Hardware.Hardware.Hardware.ListDevices()

    #Setup keyboard capture
    #print(keyboard.is_pressed('ctrl'))

    #rk = keyboard.record(until ='enter')
    #print(rk)

    print("Starting Interface...")

    global root
    root=tk.Tk()
    
    tl=formTopLevel(top=root)
    root.overrideredirect(1)
    root.bind("<Key>",codeReg.key_pressed)
    root.mainloop()


if __name__ == "__main__":
    main()

