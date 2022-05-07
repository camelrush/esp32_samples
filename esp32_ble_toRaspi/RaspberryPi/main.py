#!/usr/bin/env python3

import sys
import asyncio
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO
from blehandler import BleHandler
from typing import List
from bleak import discover

TARGET_ADDRESS = "40:91:51:BE:E8:5A"

async def main():
    while True:
        print('start device scan...')
        tasks = []
        devices:List = await discover()
        for device in devices:
            if device.address == TARGET_ADDRESS:
                handler = BleHandler(TARGET_ADDRESS,)
                tasks.append(asyncio.ensure_future(handler()))
                print(f'found target device : {device}. discover process end.')
        
        if len(tasks) > 0:
            [await task for task in tasks]
        else:
            print('target device not found. rescan after sleep 5s.')
        await asyncio.sleep(5)

asyncio.run(main())

