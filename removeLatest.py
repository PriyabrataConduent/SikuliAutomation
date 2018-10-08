# Program extracting first column 
import xlrd 
import glob
import os
import sys

BASE_DIR="D:\\IncrementalCompile\\deploy\\"

#list_of_files = glob.glob(BASE_DIR+'*.xlsx')
#print(list_of_files)
#latest_file = max(list_of_files, key=os.path.getctime)
#count=len(list_of_files)
#print(latest_file)
#os.unlink(latest_file)

files = [os.path.join(BASE_DIR, x) for x in os.listdir(BASE_DIR) if x.endswith(".xlsx")]
newest = max(files , key = os.path.getctime)
print(newest)
os.remove(newest)



list_of_text_files = glob.glob(BASE_DIR+'*.txt')
for file in list_of_text_files:
    #print(file)
    os.remove(file)
