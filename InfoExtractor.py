#Note: To use with Python 3.x or later for strings to be considered unicode by default
from SymptomsData import SymptomsData
import unicodedata

#check if digit is age from the previous word
def isAge(number, previous):
    ageKeywords = ['عمر','أنا','age','am','im']
    for keyword in ageKeywords:
        if keyword in previous: return True

    return False


#check if arabic char
def isArabChar(ch):
    return ('\u0600' <= ch <= '\u06FF' or
    '\u0750' <= ch <= '\u077F' or
    '\u08A0' <= ch <= '\u08FF' or
    '\uFB50' <= ch <= '\uFDFF' or
    '\uFE70' <= ch <= '\uFEFF' or
    '\U00010E60' <= ch <= '\U00010E7F' or
    '\U0001EE00' <= ch <= '\U0001EEFF')

#clean the string from punctuation (even for Arabic) and capital letters
def clean(string):
    ret = ''.join(ch for ch in string if not unicodedata.category(ch).startswith('P'))
    ret = ret.lower()
    return ret


class InfoExtractor:
    def __init__(self, baseSymptom):
    #baseSymptom is a dictionary as synonym:Symptom from SymptomsData
        self.baseSymptom = baseSymptom

    #Given the message as a string, return a list of the information
    #return: list of tuples (attribute, 1 or 0 or value for age)
    def ExtractInfo(self,message):
        baseSymptom = self.baseSymptom

        #remove punctuation and capital letters
        message = clean(message)
        words = message.split()

        #intermediate dictionary to avoid duplicates in infoList
        symptomValue = {}
        infoList = []

        #string to store the previous word
        previousWord = "عمر"
        
        for w in words:

            #NOTE: isdecimal() and int() work for arabic digits
            if w.isdecimal():
                #could be age
                if (isAge( int(w), previousWord )):
                    symptomValue['age'] = int(w)
                    
                #could be temperature
                else:
                    temp_test = 1 if float(w)>=37.8 else 0
                    symptomValue['temperature'] = temp_test

            else:
                if w in baseSymptom:
                    symptomValue[ baseSymptom[w] ] = 1

            previousWord = w

        for synonym in baseSymptom.keys():
            if synonym in message:
                symptomValue[ baseSymptom[synonym] ] = 1

        for symptom in symptomValue.keys():
            infoList.append( (symptom, symptomValue[symptom]) )
        
        return infoList


