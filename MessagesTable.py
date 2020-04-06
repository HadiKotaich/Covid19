import sqlite3
import uuid
from sqlite3 import Error
from Message import Message
import datetime

class MessagesTable:
  def __init__(self, dbName, tableName):
    try:
      self.con = sqlite3.connect(dbName)
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
    self.con.execute(query, (message.messageId, message.text, message.senderId, message.date, message.isVoice, message.voiceUrl, message.isLocation, message.latitude, message.longitude))
    self.con.commit()
  # checks if a record exist
  def Get(self, messageId):
    query = "SELECT * FROM " + self.tableName + " where messageId = ?"
    record = self.con.execute(query, (messageId,)).fetchone()
    return record
  