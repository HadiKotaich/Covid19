import sqlite3
import uuid
from sqlite3 import Error
from Message import Message
import datetime

class RecordsTable:
  def __init__(self, dbName, tableName):
    try:
      self.con = sqlite3.connect(dbName)
      self.tableName = tableName
    except Error:
      print(Error)
  
  # creates a new table and drops the old one
  # Primary Key is composite (senderId, date)
  def CreateTable(self, symptoms):
    # drop old table
    query = "DROP TABLE IF EXISTS " + self.tableName
    self.con.execute(query)
    #create the new table
    query = "CREATE TABLE " + self.tableName + """(
              senderId text NOT NULL, 
              date date NOT NULL,
              latitude float DEFAULT -1000,
              longitude float DEFAULT -1000,
              conversation text DEFAULT ''
            """ 

    for symptom in symptoms:
      query += ", " + symptom + " float DEFAULT 0"
    query += ", PRIMARY KEY (senderId, date))"
    self.con.execute(query)
    self.con.commit()

  # inerts a record 
  def Insert(self, senderId, date):
    query = "INSERT INTO " + self.tableName + "(senderId, date) VALUES (?,?)"
    self.con.execute(query, (senderId, date))
    self.con.commit()
  # checks if a record exist
  def Contains(self, senderId, date):
    query = """ 
              SELECT 1
              FROM """ + self.tableName + """
              WHERE senderId = ? and date = ?
            """
    record = self.con.execute(query, (senderId, date)).fetchone()
    return record != None
  # gets a specific record
  def GetRecord(self, senderId, date):
    query = "SELECT * FROM " + self.tableName + " where senderId = ? and date = ?"
    record = self.con.execute(query, (senderId,date)).fetchone()
    return record
  # gets a specific field
  def GetField(self, senderId, date, field):
    query = "SELECT  " + field + " FROM "+ self.tableName + " where senderId = ? and date = ?"
    value = self.con.execute(query, (senderId, date)).fetchone()[0]
    return value
  # sets a specific field
  def SetField(self, senderId, date, field, value):
    query = "UPDATE "+ self.tableName + " SET " + field + " = ?  where senderId = ? and date = ?"
    field = self.con.execute(query, (value,senderId,date)).fetchone()
    self.con.commit()
  # updates the infos of the record based on infos
  def updateRecordInfos(self, senderId, date, infos):
    if len(infos) == 0:
      return
    query = "UPDATE "+ self.tableName +" SET "
    params = []
    
    for i in range(len(infos)):
      info = infos[i]
      query += info[0] + " = ? "
      params.append(info[1])
      if i != len(infos) - 1:
        query += " , "

    query += """ where senderId = ? and date = ?"""    
    params.append(senderId)
    params.append(date)
    self.con.execute(query, params)
    self.con.commit()
  
  #add message to the conversation and returns the new conversation
  def AddMessageToConversation(self, message):
    senderId = message.senderId
    date = message.date
    conversation = self.GetField(senderId, date, "conversation")
    conversation += " " + message.text
    self.SetField(senderId, date, "conversation", conversation)
    return conversation

  # Analytics

  # params:
  #   constraints: list of (attribute, lower value, upper value)
  # return:
  #   returns the count of records satisfying all these constraints
  def CountRecords(self, constraints):
    params = []
    query = "SELECT  COUNT(*) FROM "+ self.tableName
    
    for i in range(len(constraints)):
      if i == 0:
        query += " where "
      else:
        query += " and "
      query += constraints[i][0] + " between ? and ? "
      params.append(constraints[i][1])
      params.append(constraints[i][2])
      
    
    value = self.con.execute(query, params).fetchone()[0]
    return value
    


  

  