import tkinter
from tkinter import messagebox

class FormSettings:
    """this is the form to modify system settings"""

    def init(self):
        return

    def Show(self):
        #define control event methods
        def btnApply_Click():
            messagebox.showinfo(title="Save Changes", message="Changes Saved")
            frmSettings.destroy


        #build form controls
        frmSettings = tkinter.Tk()
        frmSettings.title('System Settings')





        
        btnApply = tkinter.Button(frmSettings, text='Save', width=25, command=btnApply_Click)
        btnApply.pack()

        btnDiscard = tkinter.Button(frmSettings, text='Cancel', width=25, command=frmSettings.destroy)
        btnDiscard.pack()

        frmSettings.mainloop()
