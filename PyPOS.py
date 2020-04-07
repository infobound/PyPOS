from Global.Settings import Settings
from Forms.FormSettings import FormSettings
from DB.MySQL import MySQL
import tkinter

#init settings
def main():
    print("Starting PyPOS...")

    print("Loading Settings")
    LocalSettings=Settings()
    LocalSettings.LoadSettings()

    print("Connecting to Database")
    print(LocalSettings.Get("Database/Type"))
    print(LocalSettings.Get("Database/Connection String"))
    db=MySQL()
    db.GetTest()


    print("Connecting to Central Processing Server")
    print("to do")

    print("Starting Interface")
    frmSettings=FormSettings()
    frmSettings.Show()




if __name__ == "__main__":
    main()
