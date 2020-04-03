from Message import Message, EncodeMessage
import datetime
import json
import jsonpickle
from pathlib import Path
import shutil


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


# message = messageManager.GetMessage()

# print(message.text, message.senderId, message.date, message.messageId)

# message = Message("Hello I have cough and feaver", "hadi", datetime.date.today(), "message_1.txt")
# messageManager = MessageManager()
# messageManager.SaveInNewMessages(message)

# print(EncodeMessage(message))

