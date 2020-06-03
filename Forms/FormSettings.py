import tkinter
from tkinter import ttk
from tkinter import messagebox
from Global.Settings import Settings
from Global.Functions import Functions

class FormSettings:
    """this is the form to modify system settings"""

    def init(self):
        return

    def Show(self,LocalSettings):
        strDBType=""
        strConnStr=""

        #define control event methods
        def btnApply_Click():
            messagebox.showinfo(title="Save Changes", message="Changes Saved")
            frmSettings.destroy

        def btnTestDB_Click():
            messagebox.showinfo(title="Test DB Connection", message="Test Succesful")
            return


        #build form controls
        frmSettings = tkinter.Tk()
        frmSettings.title('System Settings')
        frmSettings.attributes("-fullscreen",True)

        frameDB = tkinter.Frame(frmSettings)
        frameDB.config(relief="sunken",borderwidth=2)
        frameDB.place(x=20,y=20,width=500,height=150)

        #database settings
        label = tkinter.Label(frameDB, text='Database')
        label.place(x=0,y=0)

        label = tkinter.Label(frameDB, text='Type:')
        label.place(x=10,y=30)


        cbDBType=ttk.Combobox(frameDB, textvariable=strDBType, values=("MySQL","MSSQL","to do Flat Files"))
        cbDBType.place(x=100,y=30)
        cbDBType['state']="readonly"

        label = tkinter.Label(frameDB, text='Connection String:')
        label.place(x=10,y=60)


        txtConnStr=tkinter.Entry(frameDB, textvariable=strConnStr)
        txtConnStr.place(x=130, y=60, width=300)


        btnTestDB = tkinter.Button(frameDB, text='Test Connection', width=25, command=btnTestDB_Click)
        btnTestDB.place(x=10,y=100)


        btnApply = tkinter.Button(frmSettings, text='Save', width=25, command=btnApply_Click)
        btnApply.place(x=30,y=300)

        btnDiscard = tkinter.Button(frmSettings, text='Cancel', width=25, command=frmSettings.destroy)
        btnDiscard.place(x=300,y=300)



        #set field values
        strDBType=LocalSettings.Get("Database/Type")
        LoopCnt=-1
        for val in cbDBType["values"]:
            LoopCnt+=1
            print(val+"="+strDBType)
            if val==strDBType:
                print(val)
                cbDBType.current(LoopCnt)

        strConnStr=LocalSettings.Get("Database/Connection String")
        Functions.SetEntryInput(txtConnStr,strConnStr)


        frmSettings.mainloop()
