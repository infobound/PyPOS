import mysql.connector

class MySQL:
    """Code for using a MySQL database"""

    def init(self):
        return

    def GetTest(self):
        db = mysql.connector.connect(host="localhost", user="root", passwd="0321", db="edens_wrath")
        #db = MySQLDatabase(host="localhost", user="root", passwd="0321", db="edens_wrath")
        cur = db.cursor()
        cur.execute("SELECT * FROM elements")
        for row in cur.fetchall():
            print(row[0])

        db.close()
