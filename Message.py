import json
import jsonpickle
from json import JSONEncoder

class Message:
  def __init__(self, text, senderId, date, isVoice, voiceUrl, isLocation, latitude, longitude, messageId):
    self.text = text
    self.senderId = senderId
    self.date = date

    self.isVoice = isVoice 
    self.voiceUrl = voiceUrl
    self.isLocation = isLocation 
    self.latitude = latitude
    self.longitude = longitude

    self.messageId = messageId

def EncodeMessage(message):
  return jsonpickle.encode(message)

def DecodeMessage(encodedMessage):
  return jsonpickle.decode(encodedMessage)

def EncodeMessageList(messageList):
  return jsonpickle.encode(messageList)

def DecodeMessageList(encodedMessageList):
  return jsonpickle.decode(encodedMessageList)