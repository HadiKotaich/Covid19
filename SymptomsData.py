class SymptomsData:
    def __init__(self):

        tmp1, tmp2 = self.generateSynonyms()
        #for now we have 12 symptoms, as in the SymptomTrackingQuestions
        self.symptoms = tmp1

        #dictionary of synonym:symptom
        self.baseSymptom = tmp2


    def generateSynonyms(self):
        synonyms = {}
        symptoms = []
        baseSymptom = {}

        #divide the symptoms into separate lists of synonyms

        #add here the synonyms in each list
        #separated in each list Arabic from English
        synonyms['cough'] = ['سعال','أسعل',

                             'cough'
                             ]

        synonyms['cold'] = ['برد','نزلات البرد',

                            'cold',
                            ]

        synonyms['diarrhea'] = ['إسهال',

                                'diarrhea'
                                ]

        synonyms['sore_throat'] = ['حلق','إلتهاب في الحلق'

                                   'sore throat'
                                   ]

        synonyms['body_pain'] = ['جسم','عضل','ألم',

                                 'body','muscle'
                                 ]

        synonyms['headache'] = ['صداع',

                                'headache'
                                ]

        synonyms['temperature'] = ['حرارة',

                                   'feaver'
                                   ]

        synonyms['breathing'] = ['تنفس', 'صعوبة في التنفس',

                                 'trouble breathing'
                                 ]

        synonyms['fatigue'] = ['إرهاق',

                               'exhausted','fatigue'
                               ]

        synonyms['travel_14'] = ['١٤ يوم', 'سافرت'

                                 '14 days'
                                 ]

        synonyms['travel_corona'] = ['مناطق مصابة',

                                     'affected region'
                                     ]

        synonyms['direct_contact'] = ['مصاب','إتصال بالمصابين',

                                      'direct contact'
                                      ]
        synonyms['age'] = ['عمر',
                        'age'
                        ]

        for symptom in synonyms.keys():
            symptoms.append(symptom)
            
            for synonym in synonyms[symptom]:
                baseSymptom[synonym] = symptom

        return symptoms,baseSymptom

