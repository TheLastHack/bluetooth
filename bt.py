import os
import time 
os.system("pip install --user pybluez2")
time.sleep(2)
os.system("clear")

import bluetooth


print("Searching for nearby devices...")

cihazlar = bluetooth.discover_devices(lookup_names=True)


for addr, name in cihazlar:
    print("Address :", addr, "Name :", name)
    
