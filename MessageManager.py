from Message import Message, EncodeMessage, DecodeMessage, EncodeMessageList, DecodeMessageList
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
    messages = DecodeMessage(open(newPath).read())
    return (fileName, messages)
  
  def LabelFileAsDone(self, fileName):
    oldPath = self.inProgressDirectory / fileName
    newPath = self.doneMessagesDirectory / fileName
    oldPath.replace(newPath)

  # for testing purpouses
  def SaveInNewMessages(self, messages, fileName):
    encodedMessages = EncodeMessageList(messages)
    p = self.newMessagesDirectory / fileName
    p.write_text(encodedMessages, encoding="utf-8") 


# message = messageManager.GetMessage()

# print(message.text, message.senderId, message.date, message.messageId)

# message = Message("Hello I have cough and feaver", "hadi", datetime.date.today(), "message_1.txt")
# messageManager = MessageManager()
# messageManager.SaveInNewMessages(message)

# print(EncodeMessage(message))

