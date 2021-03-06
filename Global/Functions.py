import re #regulare expression
import subprocess
import usb.core

def ParsePathToList(Path):
    #turns a url type string to a list of nodes
    #Expected: Path="C:\Windows\system32\regedit.exe"
    #Expected: Path="//server/share/folder"
    Path=Path.replace("\\\\","/")
    Path=Path.replace("\\","/")
    if Path.find("//",0,2)=="//":
        Path=Path[2]

    PathList=Path.split("/")
    return PathList

def SetEntryInput(entControl,strText):
    entControl.delete(0,"end")
    entControl.insert(0, strText)

def Log(intLevel,strEntry):
    print(strEntry)

def Encode(Decoded):
    print("to do: function encode")
    return Decoded

def Decode(Encoded):
    print("to do: function Decode")
    return Encoded

def GetAllUSBDevices():
    device_re = re.compile(b"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    print(device_re)
    df = subprocess.check_output("lsusb")
    print(df)
    #df=df.split(b"\n")
    devices = []
    for i in df.split(b"\n"):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)
                #print(dinfo)
    #print(devices)
    return devices

