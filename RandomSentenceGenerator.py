from random import randint
import unicodedata

englishWords = ["cough", "cold", "diarrhea","throat", "sore throat", "Muscle pain","Pain in the body",  "headache", "temperature", "breathing difficulties", "exhaustion", "I travelled ", "14 days", "corona", "Contact with patient" ]
arabicWords = ["سعال", "برد", "إسهال", "حلق", "إلتهاب في الحلق", "ألم عضلي", "ألم في الجسم", "صداع", "حرارة", "صعوبة في التنفس", "إرهاق", "سافرت ", "١٤ يوم", "كورونا", "إتصال بالمصابين" ]

words = arabicWords + englishWords
# words = englishWords

sentences = []
numberOfSentences = 500

for i in range(numberOfSentences):
  sentenceLenght = randint(2, 8)
  sentence = ""
  for j in range(sentenceLenght):
    wordInd = randint(0, len(words) - 1)
    if j != 0:
      sentence += " "
    sentence += words[wordInd]
  sentences.append(sentence)

f = open("randomSentences.txt", 'w', encoding="utf-8")
for sentence in sentences:
  f.write(sentence + "\n")
