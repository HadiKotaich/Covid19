from RecordsDb import RecordsDb
from InfoExtractor import InfoExtractor
from SymptomsData import SymptomsData
import datetime

symptomsData = SymptomsData()
infoExtractor = InfoExtractor(symptomsData.baseSymptom)
records = RecordsDb("Covid19.db", "Records")
records.CreateTable(symptomsData.symptoms)

while True:
  id = input("enter id: ")
  message = input("enter message: ")
  date = datetime.date.today()
  infos = infoExtractor.ExtractInfo(message)
  
  if records.Contains(id, date) == False:
    records.Insert(id, date)
  
  records.AddMessageToRecord(id, date, message, infos)