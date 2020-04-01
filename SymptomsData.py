class SymptomsData:
    def __init__(self):
        #for now we have 12 symptoms, as in the SymptomTrackingQuestions
        self.symptoms = ['cough','cold','diarrhea','sore_throat','body_pain','headache',
                         'temperature','breathing','fatigue','travel_14','travel_corona','direct_contact']

        #dictionary of synonym:symptom
        self.synonyms = self.generateSynonyms()


    def generateSynonyms(self):
        ret = {}

        #divide the symptoms into separate lists of synonyms
        #assume the number of lists is the number of symptoms
        num = len(self.symptoms)
        masterList = []

        #add here the synonyms in each list
        #separated in each list Arabic from English
        coughList = ['سعال','أسعل',
                     
                     'cough'
                     ]

        coldList = ['برد','نزلات البرد',
                    
                    'cold',
                    ]

        diarrheaList = ['إسهال',

                        'diarrhea'
                        ]

        sore_throatList = ['حلق','إلتهاب في الحلق'
                           
                           'sore throat'
                           ]

        body_painList = ['جسم','عضل','ألم',

                         'body','muscle'
                         ]

        headacheList = ['صداع',
                        
                        'headache'
                        ]

        temperatureList = ['حرارة',

                           'feaver'
                           ]

        breathingList = ['تنفس', 'صعوبة في التنفس',

                         'trouble breathing']

        fatigueList = ['إرهاق',

                       'exhausted','fatigue'
                       ]

        travel_14List = ['١٤ يوم', 'سافرت'

                         '14 days'
                         ]

        travel_coronaList = ['مناطق مصابة',

                             'affected region'
                             ]

        direct_contactList = ['مصاب','إتصال بالمصابين',

                              'direct contact'
                              ]

        masterList.append(coughList)
        masterList.append(coldList)
        masterList.append(diarrheaList)
        masterList.append(sore_throatList)
        masterList.append(body_painList)
        masterList.append(headacheList)
        masterList.append(temperatureList)
        masterList.append(breathingList)
        masterList.append(fatigueList)
        masterList.append(travel_14List)
        masterList.append(travel_coronaList)
        masterList.append(direct_contactList)
        
        for i in range(num):
            curList = masterList[i]
            symptom = self.symptoms[i]
            for elem in curList:
                ret[elem] = symptom

        return ret

