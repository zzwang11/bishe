import sqlite3


class exe:
    def __init__(self,cc):
        self.cc = cc

    def exee(self,x):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        while(x):
            c.execute(self.cc)
        # print("Table created successfully")
        conn.commit()
        conn.close()
        return c

    def create_tb(name):
        conn = sqlite3.connect(f'{name}.db')
        c = conn.cursor()

        b = '''CREATE TABLE data
                   (ID INT PRIMARY KEY     NOT NULL,
                   TIME       DATETIME    NOT NULL,
                   VALUE1          DOUBLE,     
                   VALUE2          DOUBLE,
                                   TEXT);'''
        c.execute(b)
        conn.commit()
        conn.close()

    def insert(time, value):
        b = f'''INSERT INTO data VALUES ({time},{value});'''
        a = exe(b)
        a.exee()

    def read_db(case):
        b = f'''SELECT * FROM data where {case};'''
        a = exe(b)
        out = a.exee()

    def delete(case):
        b = f'''DELETE from COMPANY where {case};'''
        a = exe(b)
        out = a.exee()

