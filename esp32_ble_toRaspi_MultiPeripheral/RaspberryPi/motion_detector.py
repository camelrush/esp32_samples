from bluepy import btle
import time

CONNECTION_RETRY = 50

BLE_SERVICE_UUID = "D5875408-FA51-4763-A75D-7D33CECEBC31"
BLE_CHARACTERISTIC_UUID = "A4F01D8C-A037-43B6-9050-1876A8C23584"

class motion_detector:

    def __init__(self ,addr):
        self._addr = addr
        self._is_connected= False
        self._peripheral = btle.Peripheral()

    def __try_connect(self):
        try:
            self._peripheral.connect(self._addr)
            self._is_connected = True
            print('connected')
        except  Exception as e:
            print("connection failed cause by" + str(e))
            time.sleep(0.05)

    def __connect(self):
        self._is_connected = False
        for i in range(CONNECTION_RETRY):
            self.__try_connect()
            if (self._is_connected == True):
                return True
        return False

    def read(self):
        if (self._is_connected == False):
            if (self.__connect() == False):
                return ''

        data = ''
        try:
            charas = self._peripheral.getCharacteristics(uuid=BLE_CHARACTERISTIC_UUID)[0]
            data = charas.read()
        except:
            self._is_connected = False

        return data

    def __disconnect(self):
        self._peripheral.__disconnect()
