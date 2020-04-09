class Message:
  def __init__(self, text=None, senderId=None, date=None, messageId=0):
    self.text = text
    self.senderId = senderId
    self.date = date
    self.messageId = messageId
    self.isVoice = False
    self.isLocation = False
    self.voiceUrl = None
    self.voiceExtention = None
    self.latitude = None
    self.longitude = None
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


