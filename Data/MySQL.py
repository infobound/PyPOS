import mysql.connector
import Global.Settings as Settings
import Global.Functions as Functions

global connDB
global boolConnected
connDB=None
boolConnected=False

def Open():
    global connDB
    global boolConnected
    
    if boolConnected==False:
        try:
            connDB = mysql.connector.connect(
                host=Settings.Get("Database/Host"),
                port=Settings.Get("Database/Port"),
                user=Settings.Get("Database/User"),
                password=Functions.Decode(Settings.Get("Database/Password")),
                db=Settings.Get("Database/Catalog")
            )
            boolConnected=True
        except Exception as e:
            print(e)
            print("Unable to connect to database")
            exit()

def Close():
    global connDB
    global boolConnected
    
    if boolConnected==True:
        connDB.close()
        boolConnected=False

def GetFoodItemGroups():
    global connDB
    Open()
    cur = connDB.cursor()
    cur.execute("SELECT * FROM pypos.viewfooditemgroups;")
    results=cur.fetchall()
    cur=None
    Close()

    return results

def GetFoodItemsByGroupRID(intGroupRID):
    global connDB
    Open()
    cur = connDB.cursor()
    cur.execute("select * from viewfooditems where fiFoodItemGroupRID="+str(intGroupRID)+";")
    results=cur.fetchall()
    cur=None
    Close()

    return results

def GetFoodItemDetails(intFoodItemRID):
    global connDB
    Open()
    cur = connDB.cursor()
    cur.execute("SELECT fiName, fiDescription, fiPrice, ttAmount FROM pypos.tblfooditems inner join tblTax on fiTaxTableRID=ttRID where fiRID="+str(intFoodItemRID)+";")
    results=cur.fetchall()
    cur=None
    Close()

    return results

def GetUPCItemDetails(strUPCItemRID):
    global connDB
    Open()
    cur = connDB.cursor()
    cur.execute("SELECT upcName, upcDescription, upcUnitPrice, ttAmount FROM pypos.tblupcitems inner join tblTax on upcTaxTableRID=ttRID where upcBarCode='"+strUPCItemRID+"';")
    results=cur.fetchall()
    cur=None
    Close()

    return results
