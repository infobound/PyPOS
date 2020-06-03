from Global.Settings import Settings
from Forms.FormSettings import FormSettings
from DB.MySQL import MySQL
import tkinter

LocalSettings=Settings()

#init settings
def main():
    print("Starting PyPOS...")

    print("Loading Settings...")

    LocalSettings.LoadSettings()

    print("Connecting to Database...")

    db=MySQL()
    db.Open(LocalSettings.Get('Database/Host'),
        LocalSettings.Get('Database/Catalog'),
        LocalSettings.Get('Database/User'),
        LocalSettings.Get('Database/Passwd'))


    print("Connecting to Central Processing Server...")
    print("to do")

    print("Starting Interface...")
    frmSettings=FormSettings()
    frmSettings.Show(LocalSettings)




if __name__ == "__main__":
    main()
