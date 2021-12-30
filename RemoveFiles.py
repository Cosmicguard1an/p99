import time
import os
import shutil


path = input('Enter path: ')
days = 30
seconds = time.time() - (days*24*60*60)
if os.path.exists(path):
  for root, dirs, files in os.walk(path):
    for name in files:
      path = os.path.join(root, name)
      ctime = os.stat(path).st_ctime
      if seconds >= ctime:
        os.remove(path)
    for name in dirs:
      path = os.path.join(root, name)
      ctime = os.stat(path).st_ctime
      if seconds >= ctime:
        shutil.rmtree(path)
else:
    print("Not found!")