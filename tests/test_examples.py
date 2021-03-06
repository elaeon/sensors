#!/usr/bin/python2.7
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from examples.door_sync import check_door
from examples.termopar_1_sync import read_temp
from examples.temperature_humidity_sync import get_humidity_temperature
from utils import check_network
import time
from utils import get_settings

settings = get_settings(__file__, directory="../examples")
carbon_server = settings.get("server", "carbon_server")
carbon_port = int(settings.get("server", "carbon_port"))

def loop(fn, msg):
    count = 0
    while count < 10:
        print(msg, fn())
        time.sleep(.5)
        count += 1

print("[OK] NETWORK" if check_network("www.google.com", 80) else "[ERROR] NETWORK")
print("[OK] CARBON SERVER" if check_network(carbon_server, carbon_port) else "[ERROR] CARBON SERVER")
loop(check_door, "PUERTA")
loop(read_temp, "TERMO PAR")
loop(get_humidity_temperature, "HUMIDITY, TEMP")

