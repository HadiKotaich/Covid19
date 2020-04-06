from Message import Message, EncodeMessage
import datetime
import json
import jsonpickle
from pathlib import Path
import shutil
import csv


class MessageManager:
  def __init__(self):
    self.basePath = Path(r"C:/files at work/Covid19/directories")
    self.newMessagesDirectory =  self.basePath / "newMessages"
    self.inProgressDirectory = self.basePath / "progress"
    self.doneMessagesDirectory = self.basePath / "doneMessages"
    self.newMessages = set()

  def GetMessage(self):
    while len(self.newMessages) == 0:
      files = [e for e in self.newMessagesDirectory.iterdir() if e.is_file()]
      for f in files:
        self.newMessages.add(f.name)
    
    currentFileName = self.newMessages.pop()  
    oldPath = self.newMessagesDirectory / currentFileName
    newPath = self.inProgressDirectory / currentFileName
    oldPath.replace(newPath)
    
    message = jsonpickle.decode(open(newPath).read())
    return message
  
  def LabelMessageAsDone(self, message):
    oldPath = self.inProgressDirectory / message.messageId
    newPath = self.doneMessagesDirectory / message.messageId
    oldPath.replace(newPath)

  # for testing purpouses
  def SaveInNewMessages(self, message):
    encodedMessage = EncodeMessage(message)
    p = self.newMessagesDirectory / message.messageId
    p.write_text(encodedMessage, encoding="utf-8") 

  def GetMessageListFromCSV(self, csvfilename) :
    msglist = [] 
    with open( csvfilename) as csvFile : 
        csvReader = csv.DictReader(csvFile, fieldnames=['Sender','Time','Text','IsVoice','IsLocation','VoiceUrl','VoiceExtension','Latitude','Longitude','VoiceLocation'])
        for record in csvReader : 
            msg = Message()
            msg.senderId = record['Sender']
            msg.date = record['Time'] 
            msg.text = record['Text']
            if record['IsVoice'] == 'T' : 
              msg.isVoice = True 
            if record['IsLocation'] == 'T' : 
              msg.isLocation = True 
            msg.voiceUrl = record['VoiceUrl']
            msg.voiceExtension = record['VoiceExtension']
            msg.latitude = record['Latitude']
            msg.longitude = record['Longitude']
            msg.audioFileName = record['VoiceLocation']
            msglist.append(msg) 
    return msglist

  def testGetMessageListFromCSV(self) : 
    msgList = self.GetMessageListFromCSV('aaa.csv')
    print (msgList)
    for msg in msgList : 
      print(msg.senderId + msg.text + msg.date+str(msg.isVoice)) 

# message = messageManager.GetMessage()

# print(message.text, message.senderId, message.date, message.messageId)

# message = Message("Hello I have cough and feaver", "hadi", datetime.date.today(), "message_1.txt")
# messageManager = MessageManager()
# messageManager.SaveInNewMessages(message)

# print(EncodeMessage(message))

msgMngr = MessageManager()
msgMngr.testGetMessageListFromCSV()
