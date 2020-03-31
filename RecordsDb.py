import sqlite3
import uuid
from sqlite3 import Error
import datetime

class RecordsDb:
  def __init__(self, dbName, tableName):
    try:
      self.con = sqlite3.connect(dbName)
      self.tableName = tableName
    except Error:
      print(Error)
  
  # creates a new table and drops the old one
  # Primary Key is composite (id, date)
  def CreateTable(self, symptoms):
    # drop old table
    query = "DROP TABLE IF EXISTS " + self.tableName
    self.con.execute(query)
    #create the new table
    query = "CREATE TABLE " + self.tableName + """(
              id text NOT NULL, 
              date date NOT NULL,
              conversation text DEFAULT ''
            """

    for symptom in symptoms:
      query += ", " + symptom + " float DEFAULT 0"
    query += ", PRIMARY KEY (id, date))"
    self.con.execute(query)
    self.con.commit()

  # inerts a record 
  def Insert(self, id, date):
    query = "INSERT INTO " + self.tableName + "(id, date) VALUES (?,?)"
    self.con.execute(query, (id, date))
    self.con.commit()

  # checks if a record exist
  def Contains(self, id, date):
    query = """ 
              SELECT 1
              FROM """ + self.tableName + """
              WHERE id = ? and date = ?
            """
    record = self.con.execute(query, (id, date)).fetchone()
    return record != None

  # updates a field in the specific record 
  def Update(self, id, date, field, value, message):
    query = "UPDATE "+ self.tableName +" SET " + field + " = ?, " +"""
            conversation = conversation || ' { ' ||  ?  || ' [ ' || ? || ' ] ' || ' } ' 
            where id = ? and date = ?"""
    self.con.execute(query, (value, message, field, id, date))
    self.con.commit()

  # gets a specific record
  def Get(self, id, date):
    query = "SELECT * FROM " + self.tableName + " where id = ? and date = ?"
    record = self.con.execute(query, (id,date)).fetchone()
    return record

  