from RecordsTable import RecordsTable
from MessagesTable import MessagesTable
from InfoExtractor import InfoExtractor
from SymptomsData import SymptomsData
from Message import Message
from MessageManager import MessageManager
import datetime

symptomsData = SymptomsData()
infoExtractor = InfoExtractor(symptomsData.baseSymptom)
messageManager = MessageManager()

recordsTable = RecordsTable("Covid19.db", "Records")
recordsTable.CreateTable(symptomsData.symptoms)

messagesTable = MessagesTable("Covid19.db", "Messages")
messagesTable.CreateTable()

while True:
  print("waiting for a new message...")
  # wait for a message
  (filename, messages) = messageManager.GetMessages()
  for message in messages:
    # update the database
    if recordsTable.Contains(message.senderId, message.date) == False:
      recordsTable.Insert(message.senderId, message.date)
    
    # update the location
    if message.isLocation:
      recordsTable.SetField(message.senderId, message.date, "longitude", message.longitude)
      recordsTable.SetField(message.senderId, message.date, "latitude", message.latitude)
    
    # update the conversation
    updatedConversation = recordsTable.AddMessageToConversation(message)

    # analyse the updated conversation
    infos = infoExtractor.ExtractInfo(updatedConversation)
    # update the symptoms
    recordsTable.updateRecordInfos(message.senderId, message.date, infos)
    # adding the message to the message table
    messagesTable.Insert(message)

  # mark the message as done in the MessageManager
  messageManager.LabelFileAsDone(filename)
  print("Processing ", filename, " done!")