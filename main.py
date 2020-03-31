from RecordsDb import RecordsDb
from InfoExtractor import InfoExtractor
import datetime

infoExtractor = InfoExtractor()
records = RecordsDb("Covid19.db", "Records")
# records.CreateTable(infoExtractor.symptoms)

while True:
  id = input("enter id: ")
  message = input("enter message: ")
  date = datetime.date.today()
  infos = infoExtractor.ExtractInfo(message)
  
  if records.Contains(id, date) == False:
    records.Insert(id, date)

  for info in infos:
    records.Update(id, date, info[0], info[1], message)