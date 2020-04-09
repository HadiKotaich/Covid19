from Message import Message
import json
from pathlib import Path
import shutil
import csv
import uuid 
from datetime import datetime

class MessageManager:
  def __init__(self):
    self.basePath = Path(r"C:/files at work/Covid19/directories")
    self.newMessagesDirectory =  self.basePath / "newMessages"
    self.inProgressDirectory = self.basePath / "progress"
    self.doneMessagesDirectory = self.basePath / "doneMessages"
    self.newFiles = set()

  def GetMessages(self):
    while len(self.newFiles) == 0:
      files = [e for e in self.newMessagesDirectory.iterdir() if e.is_file()]
      for f in files:
        self.newFiles.add(f.name)
    
    fileName = self.newFiles.pop()  
    oldPath = self.newMessagesDirectory / fileName
    newPath = self.inProgressDirectory / fileName
    oldPath.replace(newPath)
    messages = self.GetMessageListFromCSV(newPath.absolute())
    return (fileName, messages)
  
  def LabelFileAsDone(self, fileName):
    oldPath = self.inProgressDirectory / fileName
    newPath = self.doneMessagesDirectory / fileName
    oldPath.replace(newPath)

  def GetMessageListFromCSV(self, csvfilename) :
    msglist = [] 
    with open(csvfilename, encoding="utf-8") as csvFile : 
      csvReader = csv.DictReader(csvFile, fieldnames=['Sender','Time','Text','IsVoice','IsLocation','VoiceUrl','VoiceExtension','Latitude','Longitude','VoiceLocation'])
      for record in csvReader : 
        msg = Message()
        msg.messageId = str(uuid.uuid4())
        msg.senderId = record['Sender']
        msg.date = datetime.strptime(record['Time'].split('T')[0], '%Y-%m-%d').date()
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

