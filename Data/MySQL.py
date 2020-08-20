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
            print(Settings.Get("Database/Host"))
            print(Settings.Get("Database/User"))
            print(Functions.Decode(Settings.Get("Database/Password")))
            print(Settings.Get("Database/Catalog"))

            connDB = mysql.connector.connect(
                host=Settings.Get("Database/Host"),
                port=3306,
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
    cur.execute("CALL spGetFoodItemGroups")
    results=cur.fetchall()
    cur=None
    Close()

    return results

def GetFoodItemsByGroupRID(intGroupRID):
    global connDB
    Open()

    try:
        cur = connDB.cursor()
    except Exception as e:
        #by opening connection and closing after stopped the connection not availble error
        print(e)
        return None
    
    #huuuuuuuuuuuuuuh!!!! to do
    cur.callproc("spGetFoodItemsByGroupRID", [intGroupRID, ])
    for fixthis in cur.stored_results():
        results=fixthis.fetchall()
        break
    #---------------------------

    Close()
    return results
