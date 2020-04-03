#Note: To use with Python 3.x or later for strings to be considered unicode by default
from SymptomsData import SymptomsData
import unicodedata

#trial function
def isAge(number):
    return number < 36 or number > 41


#check if arabic char
def isArabChar(ch):
    return ('\u0600' <= ch <= '\u06FF' or
    '\u0750' <= ch <= '\u077F' or
    '\u08A0' <= ch <= '\u08FF' or
    '\uFB50' <= ch <= '\uFDFF' or
    '\uFE70' <= ch <= '\uFEFF' or
    '\U00010E60' <= ch <= '\U00010E7F' or
    '\U0001EE00' <= ch <= '\U0001EEFF')

#clean the string from punctuation
#TODO: Should we check for floats? ex: 39.2?
def clean(string):
    ret = ''.join(ch for ch in string if not unicodedata.category(ch).startswith('P'))
    return ret


class InfoExtractor:
    def __init__(self, baseSymptom):
    #baseSymptom is a dictionary as synonym:Symptom from SymptomsData
    #TODO need to decide on attribute names to use
    #TODO single and multiple words
        self.baseSymptom = baseSymptom

    #Given the message as a string, return a list of the information
    #return: list of tuples (attribute, 1 or 0 or value for age)
    def ExtractInfo(self,message):
        baseSymptom = self.baseSymptom
        words = message.split()
        ret = []
        
        for w in words:
            #TODO need if arabic to process it
            #remove punctuation
            w = clean(w)

            #TODO need a way to figure out if a number is age or temperature
            #Idea: could store previous word
            #NOTE: isdecimal() and int() work for arabic digits
            if w.isdecimal():
                #could be age
                if (isAge( int(w) )):
                    ret.append( ('age', int(w)) )
                    
                #could be temperature
                else:
                    temp_test = 1 if float(w)>=37.8 else 0
                    ret.append( ('temperature', temp_test) )

            else:
                #TODO should implement negation also
                #TODO word distance and if multiple keywords?
                if w in baseSymptom:
                    ret.append( (baseSymptom[w], 1) )

        return ret

