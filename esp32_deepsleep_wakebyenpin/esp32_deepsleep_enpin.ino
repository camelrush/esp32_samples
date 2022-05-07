void setup() {
  // シリアル出力初期化
  Serial.begin(115200);

  // シリアル出力初期化
  Serial.println("Sleep!!");
  esp_deep_sleep_start();
  Serial.println("Wake?(on setup)"); // ← 出力されない
}

void loop(){
  // ダミー出力
  Serial.println("Wake?(on loop)"); // ← 出力されない
}
