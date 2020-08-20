import Global.Settings as Settings

strDBType=Settings.Get("Database/Type")
if strDBType=="MySQL":
    import Data.MySQL as posDB
elif strDBType=="MSSQL":
    import Data.MSSQL as posDB
else:
    import Data.FlatFiles as posDB


def Open():
    posDB.Open()

def Close():
    posDB.Close()

def GetFoodItemGroups():
    return posDB.GetFoodItemGroups()

def GetFoodItemsByGroupRID(intGroupRID):
    return posDB.GetFoodItemsByGroupRID(intGroupRID)


