#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
#include <esp_system.h>

void setup() {
  uint8_t chipid[6];
  char name[256];
  /* Read ESP's MAC address */
  esp_efuse_read_mac(chipid);
  /* Take last 3 octects and discard organisation's identifier */
  snprintf(name, 256, "BEACON_ASL-%02X%02X%02X", chipid[3], chipid[4], chipid[5]);

  BLEDevice::init(name);
  BLEDevice::setPower(ESP_PWR_LVL_P9); /* Maximum power level */
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  /* Minimum interval for BLE is 20ms:
   * (0x20 = 32d --> interval = 0.625*32 = 20ms --> 50Hz) */
  pAdvertising->setMinInterval(0x20);
  pAdvertising->setMaxInterval(0x20); 
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinPreferred(0x0);
  BLEDevice::startAdvertising();
}

void loop() { /* Empty loop */ }
