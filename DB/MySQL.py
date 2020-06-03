import mysql.connector

class MySQL:
    """Code for using a MySQL database"""

    def init(self):
        return

    def Open(self,server,catalog,username,pwd):
        try:
            db = mysql.connector.connect(
                host=server,
                user=username,
                passwd=pwd,
                db=catalog)
        except:
            print("Unable to connect to database")
            exit()

    def Get(self,SQL):
        cur = db.cursor()
        cur.execute(SQL)
        return cur.fetchall()

    def Close():
        db.close()
