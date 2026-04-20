import time
import os
import shutil
path = input("enter the path")
days = input("enter how old you want files to be deleted in days")
time2=time.time()
if os.path.exists(path):
    os.walk(path)
    os.path.join(path)
    ctime=os.stat(path).st_ctime
    if ctime>time2:
        os.remove(path)
    else:
        shutil.rmtree(path)
else:
    print("not found")