import random
import unicodedata

class RandomSentenceGenerator:
  def __init__(self, arabicWords, englishWords):
    self.englishWords = englishWords
    self.arabicWords = arabicWords
  
  def decision(self, probability):
    return random.random() < probability

  def getRandomAgeArabic(self): 
    age = "عمري "
    age += str(random.randint(0, 100))
    return age

  def GenerateSentence(self, sentenceLength, arabicWordProba):
    assert(sentenceLength < min(len(self.englishWords), len(self.arabicWords))), "sentence too long to be generated without duplication"
    arabicWordsCount = 0
    englishWordsCount = 0
    for i in range(sentenceLength):
      if self.decision(arabicWordProba):
        arabicWordsCount += 1
      else:
        englishWordsCount += 1
    arabicSentence = random.sample(self.arabicWords, arabicWordsCount)
    englishSentence = random.sample(self.englishWords, englishWordsCount)
    sentence = englishSentence + arabicSentence
    # random.shuffle(sentence)
    if self.decision(0.6):
      sentence.append(self.getRandomAgeArabic())
      if englishWordsCount == 0:
        sentence.reverse()
    sentence = " - ".join(sentence)
    return sentence

  def generateSentences(self, numberOfSentences, arabicProba):
    sentences = []
    for i in range(numberOfSentences):
      sentenceLength = random.randint(1, 8)
      sentence = self.GenerateSentence(sentenceLength, arabicProba)
      sentences.append(sentence)
    return sentences

# main
englishWords = ["cough", "cold", "diarrhea","throat", "sore throat", "Muscle pain","Pain in the body",  "headache", "temperature", "breathing difficulties", "exhaustion", "I travelled ", "14 days", "corona", "Contact with patient" ]
arabicWords = ["سعال", "برد", "إسهال", "حلق", "إلتهاب في الحلق", "ألم عضلي", "ألم في الجسم", "صداع", "حرارة", "صعوبة في التنفس", "إرهاق", "سافرت ", "١٤ يوم", "كورونا", "إتصال بالمصابين" ]


sentenceGenerator = RandomSentenceGenerator(arabicWords, englishWords)
sentences = sentenceGenerator.generateSentences(500, 0.9)
f = open("randomSentences.txt", 'w', encoding="utf-8")
for sentence in sentences:
  f.write(sentence + "\n")
  f.write("-----------------------------------------------------------------------\n")
