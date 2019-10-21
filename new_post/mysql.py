import pymysql

class mysql(object):

    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    def connection(self):
        myConnection = pymysql.connect(
            host = self.host, user = self.user,
            passwd = self.passwd, db = self.db)
        return myConnection

    def close(self, myConnection):
        myConnection.close()
    
    def query(self, myConnection, table):
        values = []
        mysql = myConnection.cursor()
        sql = "select * from {}".format(table)
        mysql.execute(sql)
        queries = mysql.fetchall()
        for value in queries:
            value = value[0]
            values.append(value)
        return values

    def insert(self, myConnection, table,  id):
        mysql = myConnection.cursor()
        sql = "insert into {} (id) values ('{}')".format(table, id)
        mysql.execute(sql)
        myConnection.commit()
