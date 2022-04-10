#define WAKEUP_PIN GPIO_NUM_33

void setup() {
  // シリアル出力初期化
  Serial.begin(115200);

  // LigthSleepモードを設定
  pinMode(WAKEUP_PIN ,INPUT);
  gpio_wakeup_enable(WAKEUP_PIN ,GPIO_INTR_HIGH_LEVEL);
  esp_sleep_enable_gpio_wakeup();
}

void loop() {
  // 起動PINがLOWになるまでウエイト
  while (digitalRead(WAKEUP_PIN) == HIGH){
    delay(100);
  }
  
  // 起動PINがLOWになったら再度LightSleepへ移行
  esp_light_sleep_start();
}
