import xlrd 
import glob
import os
import sys

textFile = "D:\\Automation_Siebel_Project\\deploy\\xls\\latestfile.txt"
outFile = "D:\\Automation_Siebel_Project\\deploy\\xls\\NewFile.txt"
BASE_DIR = "D:\\Automation_Siebel_Project\\deploy\\xls\\"
list_of_files = glob.glob('D:\\Automation_Siebel_Project\\deploy\\xls\\*.xls')
files = [os.path.join(BASE_DIR, x) for x in os.listdir(BASE_DIR) if x.endswith(".xls")]
newest = max(files , key = os.path.getctime)

#latest_file = max(list_of_files, key=os.path.getctime)
loc = (newest)
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0)
with open(textFile, "w") as dataFile:
    for i in range(sheet.nrows):
        dataSet = '"'+sheet.cell_value(i, 0)+'"'
        print(dataSet, file = dataFile)


with open(textFile, 'r') as f:
    lines = f.read()
    with open(outFile, 'w') as w:
        w.write(lines[:-1])


with open(outFile, "r") as data:
    for each_line in data:
        try:
            objList = each_line.replace("\n", " or ")
            print(objList, end='')

        except ValueError:
            pass
