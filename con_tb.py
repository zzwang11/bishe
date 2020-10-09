import sqlite3


class exe:
    def __init__(self,cc):
        self.cc = cc

    def exee(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute(self.cc)
        # print("Table created successfully")
        conn.commit()
        conn.close()
        return c