## Setupの流れ
参考にしたのはこちら

- Raspberry Pi (Central)
[CO2センサを使う⑩ラズパイでBLEセントラル](https://www.denshi.club/cookbook/sensor/co2/co210ble.html)

- ESP32 (Periferal)
[CO2センサを使う⑧AdafruitのSCD-30ボードをESP32につないでBLEペリフェラルに](https://www.denshi.club/cookbook/sensor/co2/co22adafruitscd-30arduino-nano-rp2040-connectble1.html)


## 環境構築
- RaspberryPiに、bluepyをセットアップ
  ``` bash
  $ sudo apt-get install python3-pip libglib2.0-dev
  $ sudo pip3 install bluepy
  ```

