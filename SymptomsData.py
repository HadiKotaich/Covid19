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
        synonyms['cough'] = ['سعل', 'ساعل', 'مسعول', 'سعال','أسعل','أح','مأحوح', 'مقحوح', 'مكحوح', 'كحكحة', 'كح',

                             'cough'
                             ]

        synonyms['cold'] = ['برد','نزل', 'نازل', 'منزول', 'مصقع', 'صقعة', 'صبرة', 'زكم', 'زاكم', 'مزكوم', 'ثلج', 'رجف',
                            'اِرتِجَاج', 'بارد',

                            'cold','freeze',
                            ]

        synonyms['diarrhea'] = ['إسهال', 'ذرب', 'بطن', 'معدة', 'معده',

                                'diarrhea'
                                ]

        synonyms['sore_throat'] = ['حلق','إلتهاب الحلق', 'كرير', 'حشرج', 'حلقوم', 'حنجر', 'زور', 'زلعوم', 'نحنح',
                                   'نخم', 'زلاعيم',

                                   'sore throat'
                                   ]

        synonyms['body_pain'] = ['جسم','عضل','ألم', 'وجع', 'موجوع', 'موجع' ,'عذب' ,'عذاب', 'جسد',

                                 'body','muscle'
                                 ]

        synonyms['headache'] = ['صداع', 'رأس', 'صدع', 'دائخ', 'مرنح',

                                'headache', 'migraine'
                                ]

        synonyms['temperature'] = ['حرارة', 'حام', 'محموم', 'حمة', 'حمى', 'نوشة', 'سخن', 'ساخن',

                                   'fever', 'feaver'
                                   ]

        synonyms['breathing'] = ['تنفس', 'صعوبة في التنفس', 'مبهور', 'لهثان', 'لهث', 'لاهث', 'نهج', 'ناهج',
                                 'منهوج', 'استرواح', 'ربو',

                                 'trouble breathing'
                                 ]

        synonyms['fatigue'] = ['إرهاق', 'معي', 'مكدود', 'مجهد', 'متخاذل', 'مفروغ', 'هفتان', 'متهالك', 'كل', 'مكل',
                               'رازح', 'تعب', 'تعبان',

                               'exhausted','fatigue'
                               ]

        synonyms['travel_14'] = ['١٤ يوم', 'سافرت', 'مسافر', 'سفر', 'راح', 'رحت',

                                 '14 days'
                                 ]

        synonyms['travel_corona'] = ['مناطق مصابة', 'منطقة مصابة', 'بلد', 'دولة',

                                     'affected region'
                                     ]

        synonyms['direct_contact'] = ['مصاب','إتصال بالمصابين', 'إتصال مباشر', 'فيروس', 'كورونا',
                                      'انصاب', 'منصاب', 'اعتناء', 'أعتني',

                                      'direct contact'
                                      ]
        synonyms['age'] = [ ]

        for symptom in synonyms.keys():
            symptoms.append(symptom)
            
            for synonym in synonyms[symptom]:
                baseSymptom[synonym] = symptom

        return symptoms,baseSymptom

