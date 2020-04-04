import json
import jsonpickle
from json import JSONEncoder

class Message:
  def __init__(self, text, senderId, date, messageId):
    self.text = text
    self.senderId = senderId
    self.date = date
    self.messageId = messageId

def EncodeMessage(message):
  return jsonpickle.encode(message)
  empJSON = jsonpickle.encode(message, unpicklable=False)
  messageJsonData = json.dumps(empJSON, indent=4)
  messageJson = jsonpickle.decode(messageJsonData)
  return messageJson

