import sqlite3
import uuid
from sqlite3 import Error
from Message import Message
import datetime

class MessagesTable:
  def __init__(self, dbName, tableName):
    try:
      self.con = sqlite3.connect(dbName, timeout=10)
      self.tableName = tableName
    except Error:
      print(Error)
  # creates a new table and drops the old one
  # Primary Key is composite (senderId, date)
  def CreateTable(self):
    # drop old table
    query = "DROP TABLE IF EXISTS " + self.tableName
    self.con.execute(query)
    #create the new table
    query = "CREATE TABLE " + self.tableName + """(
              messageId text PRIMARY KEY,
              text text, 
              senderId text, 
              date date, 
              isVoice Integer, 
              voiceUrl text, 
              isLocation Integer, 
              latitude float, 
              longitude float)
            """
    self.con.execute(query)
    self.con.commit()
  # inerts a record 
  def Insert(self, message):
    query = "INSERT INTO " + self.tableName + " VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)"
    print(message.isLocation)
    print(message.latitude)
    print(message.longitude)
    print(message.latitude if message.isLocation else 0)
    print(message.longitude if message.isLocation else 0)
    self.con.execute(query, (
      message.messageId, 
      message.text, 
      message.senderId, 
      message.date, 
      1 if message.isVoice else 0, 
      message.voiceUrl if message.isVoice else '', 
      1 if message.isLocation else 0, 
      message.latitude if message.isLocation else 0, 
      message.longitude if message.isLocation else 0
      ))
    self.con.commit()
  # checks if a record exist
  def Get(self, messageId):
    query = "SELECT * FROM " + self.tableName + " where messageId = ?"
    record = self.con.execute(query, (messageId,)).fetchone()
    return record
  