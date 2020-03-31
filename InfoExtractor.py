class InfoExtractor:
  def __init__(self):
    self.symptoms = ["cough", "temperature", "age"]

  def ExtractInfo(self, message):
    infos = []
    for symptom in self.symptoms:
      if symptom in message:
        infos.append((symptom, 1))
    return infos