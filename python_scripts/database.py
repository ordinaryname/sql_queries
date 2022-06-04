import os
import pyodbc

class Database():

    def __init__(self):
        self.connection = pyodbc.connect("Driver=/usr/local/lib/libmsodbcsql.18.dylib;Server=localhost,1433;Encrypt=no;UID=" + os.environ["PY_DB_UID"] + ";PWD=" + os.environ["PY_DB_PWD"] + ";")
        self.cursor = self.connection.cursor()
        self.queries = []
        self.lines = []

    def query(self, query, values):
        self.queries.append(values)
        if values:
            return self.cursor.execute(query, values)
        else:
            return self.cursor.execute(query)


    def buildCalendar(self, url):
        self.lines = []
        q = 'INSERT INTO Calendar VALUES (?,?,?,?,?,?,?);'
        with open(url, 'r') as listings:
            while True:
                l = listings.readline()
                if not l:
                    break
                ls = l.split('"')
                if len(ls) > 4:
                    ls[1] = ls[1].replace(',', '')
                    ls[3] = ls[3].replace(',', '')
                    s = ''.join(ls)
                else:
                    s = l
                s = s.split(",")
                try:
                    self.lines.append((int(s[0]),s[1],s[2],s[3],s[4],int(s[5]),int(s[6].strip())))
                except:
                    continue
        self.cursor.fast_executemany = True
        #self.cursor.executemany(q, self.lines)
        #for i in range(1, len(self.lines)):
            #self.query(q,self.lines[i])
            #print(i, end="\r")
