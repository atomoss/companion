#!/usr/bin/python -tt

import os
from time import sleep
home = os.environ['HOME']

# os.system("sudo chmod 777 /dev/autopilot")

while True:
  while ((os.system("ls /dev/autopilot 2>/dev/null") != 0) or (os.path.isfile(home+"/companion/scripts/start_mavproxy_telem_splitter.sh")==0)):
    sleep(2)

  os.system(home+"/companion/scripts/start_mavproxy_telem_splitter.sh")
  sleep(2)

