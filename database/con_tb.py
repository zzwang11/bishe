import sqlite3


class mydb:
    def __init__(self, db):
        self.db = db

    def one(self, ju):
        conn = sqlite3.connect(f'{self.db}.db')
        c = conn.cursor()
        try:
            c.execute(ju)
            mmm = c.fetchall()
            conn.commit()
        except:
            conn.rollback()
            mmm = []
            print('error')
        conn.close()
        return mmm


class mydb2:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(f'{self.db}.db')
        self.c = self.conn.cursor()

    def pi(self, ju):
        try:
            self.c.execute(ju)
            self.conn.commit()
        except:
            self.conn.rollback()

    def close(self):
        self.conn.close()


# s = mydb('test')
# s.one('create table mytwo (id int primary key,name text);')
# s = mydb('test')
# s.one('insert into myone values (1,"aww")')
# s.one('insert into myone values (2,"aww")')
# s.one('insert into myone values (3,"aww")')
a = mydb('test')
print(a.one("select name from sqlite_master where type='table'"))
