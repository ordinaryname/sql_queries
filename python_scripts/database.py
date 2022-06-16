import os
import pyodbc
import csv

class Database():

    def __init__(self):
        # connect to database on Database() object creation
        # username/password supplied through environment variables
        # as written, function connects to a local ms database hosted in a Docker container
        self.connection = pyodbc.connect("Driver=/usr/local/lib/libmsodbcsql.18.dylib;Server=localhost,1433;Encrypt=no;UID=" + os.environ["PY_DB_UID"] + ";PWD=" + os.environ["PY_DB_PWD"] + ";")
        self.cursor = self.connection.cursor()
        self.cursor.fast_executemany = True
        self.queries = []
        self.data = []

    def query(self, query, values):
        # submit query to database
        # results can be retrieved from Database.cursor
        # see notes.py for sample queries
        self.queries.append(values)
        if values:
            return self.cursor.execute(query, values)
        else:
            return self.cursor.execute(query)

    def saveToFile(self, url, header, rows):
        # save sql query results to csv file
        with open(url, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)
            csvwriter.writerows(rows)

    def csv_to_json(self, path):
        # convert rows in csv file to a list json objects
        ab = []
        with open(path, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for row in csvReader:
                ab.append(row)
        return ab
