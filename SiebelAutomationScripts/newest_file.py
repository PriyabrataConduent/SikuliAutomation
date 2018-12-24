import os
import sys


BASE_DIR="D:\\Automation_Siebel_Project\\deploy\\"

files = [os.path.join(BASE_DIR, x) for x in os.listdir(BASE_DIR) if x.endswith(".xls")]
newest = max(files , key = os.path.getctime)
print(newest)
