import json
import Global.Functions as Functions

global SettingsData
SettingsData=""

def LoadSettings():
    global SettingsData

    #read from Settings.json
    with open('Settings.json', 'r') as file:
        #SettingsData is a string
        SettingsData = json.load(file)

def SaveSettings():
    global SettingsData

    #save to Settings.json
    print("to do: save settings")

def Get(Path):
    global SettingsData

    #Path is a URI
    #"//Database/Connection string"
    if SettingsData=='':
        LoadSettings()
    SettingsPart=SettingsData
    PathParts=Functions.ParsePathToList(Path)
    for Part in PathParts:
        try:
            SettingsPart=SettingsPart[Part]
        except:
            return "";

    return SettingsPart

def Set(Path,Value):
    global SettingsData

    #set Value
    print("to do: set variable")
