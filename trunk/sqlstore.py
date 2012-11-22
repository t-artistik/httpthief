import sqlite3, datetime

class DB():
    def __init__(self):
        self.dbpath = "t:\\test.db" #NAME OF THE DATABASE FILE (PATH IS OPTIONAL)
        self.dbcon = self.create_db(self.dbpath)
    def __repr__(self):
        return "SQLITE obj: " + self.dbpath
    def db(self):
        return self.dbcon
    def create_db(self, db):
        connection=sqlite3.connect(db)
        cur=connection.cursor()
        try:
            cur.execute('CREATE TABLE cookie (Id INTEGER PRIMARY KEY, Date TEXT, Clientip TEXT, Data TEXT)')
            cur.execute('CREATE TABLE cred (Id INTEGER PRIMARY KEY, Date TEXT, Clientip TEXT, Username TEXT, Password TEXT)')
            connection.commit()
        except sqlite3.OperationalError:
            print "Tables seems to be already created."
        return connection
    def now(self):
        return str(datetime.datetime.now())
    def execute_query(self, query):
        cur = self.db().cursor()
        cur.execute(query)
        self.db().commit()
        return cur.fetchall()
    def insert_cookie(self, client_ip, data):
        date = self.now()
        query = 'INSERT INTO cookie(Date, Clientip, Data) VALUES("%s", "%s", "%s")' % (date, client_ip, data)
        self.execute_query(query)
    def insert_cred(self, client_ip, username, password):
        date = self.now()
        query = 'INSERT INTO cred(Date, Clientip, Username, Password) VALUES("%s", "%s", "%s", "%s")' % (date, client_ip, username, password)
        self.execute_query(query)
    def dump_table(self, table):
        "should be used as a debug"
        query = 'SELECT * FROM %s' % table
        print "-- TABLE DUMP (%s):" % table        
        print self.execute_query(query)
   
"""TEST CODE:
a = DB()

a.insert_cookie('1.2.3.4', 'bgfwew')
a.insert_cred('3.55.21.11', 'userek', 'dumb55')

a.dump_table('cookie')
a.dump_table('cred')
"""