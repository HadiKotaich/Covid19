from RecordsDb import RecordsDb
from InfoExtractor import InfoExtractor
from SymptomsData import SymptomsData
from Message import Message
from MessageManager import MessageManager

symptomsData = SymptomsData()
infoExtractor = InfoExtractor(symptomsData.baseSymptom)
messageManager = MessageManager()
records = RecordsDb("Covid19.db", "Records")
records.CreateTable(symptomsData.symptoms)

while True:
  print("waiting for a new message...")
  # wait for a message
  message = messageManager.GetMessage()
  # analyse the message text
  infos = infoExtractor.ExtractInfo(message.text)
  # update the database
  if records.Contains(message.senderId, message.date) == False:
    records.Insert(message.senderId, message.date)
  records.AddMessageToRecord(message, infos)
  # mark the message as done in the MessageManager
  messageManager.LabelMessageAsDone(message)
  print("Processing ", message.messageId, " done!")