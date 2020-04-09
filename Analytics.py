from RecordsTable import RecordsTable
from SymptomsData import SymptomsData

recordsTable = RecordsTable("Covid19.db", "Records")
symptomsData = SymptomsData()

constraints = []
startDate = input("pleae enter start date in this format yyyy-mm-dd: ")
endDate = input("pleae enter end date in this format yyyy-mm-dd: ")
constraints.append(("date", startDate, endDate))

while True:
  constraint = input("please enter any addditional constraint or end: ")
  if constraint == "end":
    break
  lowVal = float(input("please enter lower value: "))
  highVal = float(input("please enter higher value: "))
  constraints.append((constraint, lowVal, highVal))
  
count = recordsTable.CountRecords(constraints)
print("constraints:", constraints)
print("count: ", count)  