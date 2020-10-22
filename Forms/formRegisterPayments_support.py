import locale
#import Forms.formRegister_cart as UICart

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

global formPayments
global classCart
#classCart=UICart.Cart

def btnAddPaymentHandler():
    classCart.AddPayment(formPayments.txtAmount.get())
    UpdateMoneyLabels()

def btnExactHandler():
    formPayments.txtAmount.delete(0,tk.END)
    formPayments.txtAmount.insert(0,locale.currency(classCart.GetCartTotal()-classCart.GetCartPaymentTotal()))

def UpdateMoneyLabels():
    btnExactHandler()

    formPayments.lblAmountPaid.configure(text=locale.currency(classCart.GetCartPaymentTotal()))
    formPayments.lblAmountDue.configure(text=locale.currency(classCart.GetCartTotal()))
    formPayments.lblRemaining.configure(text=locale.currency(classCart.GetCartTotal()-classCart.GetCartPaymentTotal()))
