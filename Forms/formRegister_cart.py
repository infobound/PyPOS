#Cart
#-Cart RID
#-Register RID
#-Employee RID
#-Items Array
#--Seq
#--Item Type (Food Item/UPC Item/Discount)
#--RID (Food RID/UPC Code/Discount RID)
#--Name
#--Description
#--Price
#--Tax Percent
#--Qty
#-Patron
#--Patron RID
#--Patron Name
#-Payments
#--Seq
#--Type (Payment/Refund)
#--Method (Cash/Credit)
#--Amount
#--Date Processed
#--Mode (Live/Batch)
#-Date Created
#-Date Last Modified
#-Date Closed
#-Closed (true/false)

import Global.Settings as Settings
import Data.DB as posDB
from enum import Enum
import datetime

class CartItem:
    class ItemType(Enum):
        FoodItem=0
        UPCItem=1
        
    Type=-1
    RID=-1
    Name=""
    Desc=""
    Price=0
    TaxRate=0
    Qty=0

class CartPatron:
    RID=-1
    Name=""

class CartPayment:
    class TransactionTypes(Enum):
        Payment=0
        Refund=1
        Discount=2

    class PaymentMethod(Enum):
        Cash=0
        Credit=1
        Debit=2

    class ProcessMethod(Enum):
        Live=0
        Batch=1

    Seq=-1
    Type=-1
    Method=-1
    Amount=0
    DateProcessed=0
    Mode=-1

class Cart():

    CartRID=-1
    RegisterRID=-1
    EmployeeRID=-1
    Items=[]
    Patron=CartPatron()
    test=CartPayment
    Payments=[test]
    DateCreated=1/1/1900
    DateLastModified=1/1/1900
    DateClosed=1/1/1900
    Closed=False


    def __init__(self, top=None):

        self.SubTotal=0
        self.TaxTotal=0
        self.DiscountTotal=0
        self.Total=0
        self.PaymentTotal=0

        #current order not set
        #could be the system crashed
        #check for local file for temp save cart
        #strFilePath=Settings.Get("General\Working Directory")+"\tempcart.json"
        print("to do - if file exists, read it")

    def GetSubTotal(self):
        return self.SubTotal

    def GetCartTax(self):
        return self.TaxTotal

    def GetDiscountTotal(self):
        return self.DiscountTotal

    def GetCartPaymentTotal(self):
        return self.PaymentTotal

    def GetCartTotal(self):
        return self.Total

    def GetDBOrder(intRID):
        print("to do - getdborder")

    def AddFoodItem(self, intRID):
        if(self.Closed==True):
            return False

        for item in self.Items:
            if(item.RID==intRID and item.Type==CartItem.ItemType.FoodItem):
                item.Qty+=1
                self.CalculateCart()
                return True

        ci=CartItem()
        FoodItemRS=posDB.GetFoodItemDetails(intRID)[0]
        ci.RID=intRID
        ci.Type=CartItem.ItemType.FoodItem
        ci.Name=FoodItemRS[0]
        ci.Desc=FoodItemRS[1]
        ci.Price=FoodItemRS[2]
        ci.TaxRate=FoodItemRS[3]
        ci.Qty=1

        self.Items.append(ci)
        self.CalculateCart()
        self.SaveCartToFile()
        return True
        
    def AddUPCItem(self, strUPC):
        if(self.Closed==True):
            return False

        for item in self.Items:
            if(item.RID==strUPC and item.Type==CartItem.ItemType.UPCItem):
                item.Qty+=1
                self.CalculateCart()
                return True

        ci=CartItem()
        UPCItemRS=posDB.GetUPCItemDetails(strUPC)
        if(UPCItemRS==[]):
            #display screen for new item
            print("to do - new item add")
            return False

        UPCItemRS=UPCItemRS[0]
        ci.RID=strUPC
        ci.Type=CartItem.ItemType.UPCItem
        ci.Name=UPCItemRS[0]
        ci.Desc=UPCItemRS[1]
        ci.Price=UPCItemRS[2]
        ci.TaxRate=UPCItemRS[3]
        ci.Qty=1

        self.Items.append(ci)
        self.CalculateCart()
        self.SaveCartToFile()
        return True

    def RemoveItem(intSeq):
        print("to do - remove item")

    def AddDiscount(strCode):
        print("to do - add discount")

    def RemoveDiscount(strCode):
        print("to do - remove discount")

    def CalculateCart(self):
        self.SubTotal=0
        self.TaxTotal=0
        self.DiscountTotal=0
        self.PaymentTotal=0
        self.Total=0

        print("to do - Calculate Cart: recalc discounts")

        for item in self.Items:
            itemtotal=item.Qty*item.Price
            itemtax=itemtotal*item.TaxRate
            self.SubTotal=self.SubTotal+itemtotal
            self.TaxTotal=self.TaxTotal+itemtax

        self.Total=self.SubTotal+self.TaxTotal

        for payment in self.Payments:
            if payment.Type==CartPayment.TransactionTypes.Refund:
                self.PaymentTotal=self.PaymentTotal+payment.Amount
            else:
                self.PaymentTotal=self.PaymentTotal-payment.Amount

            if payment.Type==CartPayment.TransactionTypes.Discount:
                self.DiscountTotal=self.DiscountTotal+payment.Amount


    def SaveCartToFile(self):
        print("to do - save to temp file")

    def AddPayment(self,Amount=0):
        payment=CartPayment
        try:
            payment.Seq=Size(self.Payments)
        except:
            payment.Seq=0

        payment.Type=payment.TransactionTypes.Payment
        payment.Method=payment.PaymentMethod.Cash
        payment.Amount=Amount
        payment.DateProcessed=datetime.datetime.utcnow()
        payment.Mode=payment.ProcessMethod.Live
        self.Payments.append(payment)
        self.CalculateCart()
        self.SaveCartToFile()
        return True
        