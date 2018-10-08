import os
import sys


BASE_DIR="D:\\IncrementalCompile\\deploy\\"

files = [os.path.join(BASE_DIR, x) for x in os.listdir(BASE_DIR) if x.endswith(".xlsx")]
newest = max(files , key = os.path.getctime)
print(newest)
