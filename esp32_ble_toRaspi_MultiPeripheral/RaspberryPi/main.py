import motion_detector as md
import time

detctor_list = []
detctor_list.append(md.motion_detector("40:91:51:be:e8:5a"))
detctor_list.append(md.motion_detector("40:91:51:be:f7:8e"))

while True:    
    for detector in detctor_list:
        print(detector.read())
        time.sleep(1)


