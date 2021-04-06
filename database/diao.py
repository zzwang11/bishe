from database.con_tb import mydb
import sqlite3
'''
创建表格
'''


def create_tb(db,tb):
    a = mydb(db)
    b = f'''CREATE TABLE {tb}
               (ID INTEGER PRIMARY KEY,
               VALUE1          DOUBLE,     
               VALUE2          DOUBLE);'''
    a.one(b)


def insert(db,tb, real,mag):
    a = mydb(db)
    b = f'''INSERT INTO {tb} VALUES ({time},{value});'''



def read_db(case):
    b = f'''SELECT * FROM data where {case};'''
    a = (b)
    out = a.exee()

def delete(case):
    b = f'''DELETE from COMPANY where {case};'''
    a = exe(b)
    out = a.exee()




