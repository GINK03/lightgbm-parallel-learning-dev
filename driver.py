import time
import os

while True:
  os.popen("/home/ansible/lightgbm/lightgbm config=train.conf > log.txt")
  time.sleep(1000)
  if os.path.exists("./LightGBM_model.txt ") is True:
    break

os.system("echo finished! >> log.txt")
print("Finished!")
