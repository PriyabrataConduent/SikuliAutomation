import xlrd 
import glob
import os
import sys

textFile = "D:\\IncrementalCompile\\deploy\\latestfile.txt"
outFile = "D:\\IncrementalCompile\\deploy\\NewFile.txt"
BASE_DIR = "D:\\IncrementalCompile\\deploy\\"
list_of_files = glob.glob('D:\\IncrementalCompile\\deploy\\*.xlsx')
files = [os.path.join(BASE_DIR, x) for x in os.listdir(BASE_DIR) if x.endswith(".xlsx")]
newest = max(files , key = os.path.getctime)

#latest_file = max(list_of_files, key=os.path.getctime)
loc = (newest)
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0)
with open(textFile, "w") as dataFile:
    for i in range(sheet.nrows):
        dataSet = '"'+sheet.cell_value(i, 0)+'"'
        print(dataSet, file=dataFile)


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
