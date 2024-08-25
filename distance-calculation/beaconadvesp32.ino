#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

// Define the beacon name
#define BEACON_NAME "Anchor_1"  // Change this to "Anchor_2" and "Anchor_3" for the other anchors

void setup() {
  Serial.begin(115200);
  
  // Initialize BLE
  BLEDevice::init(BEACON_NAME);
  BLEServer *pServer = BLEDevice::createServer();

  // Set advertisement data
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(BLEUUID((uint16_t)0x181A));  // Random service UUID
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinPreferred(0x06);  // Functions that help with iPhone connections issues
  pAdvertising->setMinPreferred(0x12);
  BLEDevice::startAdvertising();

  Serial.printf("Beacon %s is advertising...\n", BEACON_NAME);
}

void loop() {
  // Keep the loop empty as we're just advertising
  delay(1000);
}
