#Note: To use with Python 3.x or later for strings to be considered unicode by default

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
    def __init__(self):
    #hash table to fill with symptom:attribute
    #each line is for an attribute
    #TODO need to decide on attribute names to use
    #TODO single or double words for keys?
        self.database = {'cough':'cough',
                'cold':'cold', 'برد':'cold',
                'diarrhea':'diarrhea', 'إسهال':'diarrhea',
                'sore':'sore_throat', 'حلق':'sore_throat',
                'body':'body_pain', 'muscle':'body_pain',
                'headache':'headache',
                'feaver':'temperature',
                'breathing':'breathing', 'trouble':'breathing',
                'fatigue':'fatigue', 'exhausted':'fatigue', 'إرهاق':'fatigue',
                '14 days':'travel_14',
                'affected region':'travel_corona',
                'direct contact':'direct_contact', 'مصاب':'direct_contact'
                }



    #Given the message as a string, return a list of the information
    #return: list of tuples (attribute, 'true' or 'false' or value for age)
    def ExtractInfo(self,message):
        database = self.database
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
                    temp_test = 'true' if float(w)>=37.8 else 'false'
                    ret.append( ('temperature', temp_test) )

            else:
                #TODO should implement negation also
                #TODO word distance and if multiple keywords?
                if w in database:
                    ret.append( (database[w], 'true') )

        return ret


