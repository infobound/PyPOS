import json
from Global.Functions import Functions

class Settings:
    """this is my setting class"""

    # Class variables
    SettingsData=""

    def init(self):
        return

    def LoadSettings(self):
        #read from Settings.json
        with open('Settings.json', 'r') as file:
            #SettingsData is a string
            self.SettingsData = json.load(file)

    def SaveSettings(self):
        #save to Settings.json
        print("to do")

    def Get(self,Path):
        #Path is a URI
        #"//Database/Connection string"
        GlobalFunctions=Functions()
        SettingsPart=self.SettingsData
        PathParts=GlobalFunctions.ParsePathToList(Path)
        for Part in PathParts:
            try:
                SettingsPart=SettingsPart[Part]
            except:
                return "";

        return SettingsPart

    def Set(self,Path,Value):
        #set Value
        print("to do")
