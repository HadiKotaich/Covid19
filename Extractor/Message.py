import json
import jsonpickle
from json import JSONEncoder

class Message:
  def __init__(self, text=None, senderId=None, date=None, messageId=0):
    self.text = text
    self.senderId = senderId
    self.date = date
    self.messageId = messageId
    self.isVoice = False
    self.isLocation = False
    self.VoiceUrl = None
    self.VoiceExtention = None
    self.Latitude = None
    self.Longitude = None
    self.audioFileName = None
    self.cough = 0
    self.cold = 0
    self.headache = 0
    self.breathing = 0
    self.throat = 0
    self.muscle = 0
    self.pain = 0
    self.fever = 0
    self.tired = 0
    self.contact = 0
    self.travel = 0
    self.overlap = 0 

def EncodeMessage(message):
  return jsonpickle.encode(message)
  empJSON = jsonpickle.encode(message, unpicklable=False)
  messageJsonData = json.dumps(empJSON, indent=4)
  messageJson = jsonpickle.decode(messageJsonData)
  return messageJson

