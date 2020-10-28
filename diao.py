from con_tb import exe

'''
创建表格
'''


def create_tb():
    b = '''CREATE TABLE data
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               VALUE            INT     NOT NULL,
               SALARY         TEXT);'''
    a = exe(b)
    a.exee()


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




