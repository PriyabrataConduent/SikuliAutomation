# Program extracting first column 
import xlrd 
import glob
import os
import sys

BASE_DIR="D:\\Automation_Siebel_Project\\deploy\\xls\\"

files = [os.path.join(BASE_DIR, x) for x in os.listdir(BASE_DIR) if x.endswith(".xls")]
newest = max(files , key = os.path.getctime)
print(newest)
os.remove(newest)


list_of_text_files = glob.glob(BASE_DIR+'*.txt')
for file in list_of_text_files:
    #print(file)
    os.remove(file)
