#include <WiFi.h>
#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>

#define SCAN_TIME 5 // seconds

// Wi-Fi credentials
const char* ssid = "your_SSID";        // Replace with your network SSID
const char* password = "your_PASSWORD"; // Replace with your network password

// Server settings
WiFiServer wifiServer(80);
WiFiClient client;

BLEScan* pBLEScan;
int rssiValues[3] = {0}; // RSSI values for Anchor_1, Anchor_2, Anchor_3
String anchorNames[3] = {"Anchor_1", "Anchor_2", "Anchor_3"};

void setup() {
  Serial.begin(115200);
  BLEDevice::init("");
  pBLEScan = BLEDevice::getScan(); // Create a BLE scan object
  pBLEScan->setActiveScan(true); // Active scan for more results
  pBLEScan->setInterval(100);
  pBLEScan->setWindow(99);  // Less than or equal to setInterval value
  
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi!");
  Serial.println(WiFi.localIP());
  
  wifiServer.begin();
}

void loop() {
  BLEScanResults foundDevices = pBLEScan->start(SCAN_TIME, false);
  for (int i = 0; i < 3; i++) {
    rssiValues[i] = -100; // Default low RSSI value
  }

  for (int i = 0; i < foundDevices.getCount(); i++) {
    BLEAdvertisedDevice device = foundDevices.getDevice(i);
    String deviceName = device.getName().c_str();

    for (int j = 0; j < 3; j++) {
      if (deviceName == anchorNames[j]) {
        rssiValues[j] = device.getRSSI();
        Serial.printf("Anchor: %s, RSSI: %d\n", anchorNames[j].c_str(), rssiValues[j]);
      }
    }
  }

  // Calculate estimated location
  float x, y;
  estimateLocation(rssiValues, x, y);
  
  if (client && client.connected()) {
    client.printf("Estimated Location: x = %.2f, y = %.2f\n", x, y);
  } else {
    client = wifiServer.available();  // Listen for incoming clients
  }

  delay(3000);
}

void estimateLocation(int rssiValues[], float &x, float &y) {
  // Placeholder simple average-based estimation for demonstration
  // Replace this with actual trilateration algorithm
  x = (rssiValues[0] + rssiValues[1] + rssiValues[2]) / 3.0;
  y = (rssiValues[0] + rssiValues[1] + rssiValues[2]) / 3.0;
}
