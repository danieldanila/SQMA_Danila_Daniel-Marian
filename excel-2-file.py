from xlrd import *
from datetime import datetime, timedelta
import sys

# =====================
#Excel
book = open_workbook('fructe.xls',on_demand=True)
sheet = book.sheet_by_index(0)
print("Cautam fructele ...")
for i in range(sheet.nrows):
     row = sheet.row_values(i)
     for j in range(len(row)):
          if row[j] == "MERE":
              ce1 = sheet.cell(i,j+1).value
              print(ce1)
          elif row[j] == "PERE":
              ce2 = sheet.cell(i,j+1).value
          elif row[j] == "GUTUI":
              ce3 = sheet.cell(i,j+1).value
          elif row[j] == "LAMAIE":
              ce4 = sheet.cell(i,j+1).value

f = open('fructe.txt', 'w')
filename = "Test1"
f.write('Merele sunt:'+ str(ce1)+ ' lei')
f.write('\nPerele sunt:'+ str(ce2)+ ' lei')
f.write('\nGutuile sunt:'+ str(ce3)+' lei')
f.write('\nLamaile sunt:'+ str(ce4)+ ' lei')
f.close()
