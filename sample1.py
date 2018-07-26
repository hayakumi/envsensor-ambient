#! /usr/bin/env pyhton3
from envstatus import EnvStatus
import os
import time
import datetime


BLUETHOOTH_DEVICEID = os.environ.get('BLUETHOOTH_DEVICEID', 0)
CHECK_SPAN = int(os.environ.get('CHECK_SPAN', '10'))

o = EnvStatus(bt=BLUETHOOTH_DEVICEID)
o.start()

latest_update = datetime.datetime.now()
while True:
    mac = os.environ.get('BLUETHOOTH_DEVICE_ADDRESS', None)
    if mac is None:
        print('No sensors found.')
        time.sleep(CHECK_SPAN)
        continue

    uId = o.setRequest(mac)
    data = o.getLatestData(uId)
    if data is not None:

        if data.tick_last_update > latest_update:
            print('Illumination: {} lx'.format(data.val_light))

        latest_update = data.tick_last_update

    o.rmRequest(uId)
    time.sleep(CHECK_SPAN)
