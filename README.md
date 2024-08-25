# Smart Walking Stick for Visually Impaired Navigation

![Project Image](path_to_your_image.jpg)

## Overview

The Smart Walking Stick is designed to assist visually impaired individuals in navigating indoor environments, such as an IKEA store. The system utilizes Bluetooth Low Energy (BLE) technology to detect proximity to various store sections, making navigation easier and safer. The walking stick leverages BLE beacons placed throughout the environment, which communicate with an ESP32 microcontroller to determine the user's location and guide them to their desired destination.

### Key Features
- **BLE Beacons**: Strategically placed throughout the environment to detect proximity and provide location-based information.

## Components

- **ESP32 Microcontroller**: The core of the system, handling BLE communication and processing data.
- **BLE Beacons**: Small, battery-powered devices that broadcast BLE signals to indicate different store sections or points of interest.
- **Power Supply**: Battery or rechargeable power source to power the ESP32 and other components.

## How It Works

1. **BLE Proximity Detection**: 
   - The BLE beacons are placed at key locations throughout the indoor environment (e.g., entrance, exit, different sections of the store).
   - These beacons continuously broadcast BLE signals that the ESP32 on the walking stick detects.
   - Based on the strength of the BLE signals (RSSI - Received Signal Strength Indicator), the system estimates the proximity to each beacon and determines the user's current location.

2. **RSSI to Distance Calculation**:  
   - The RSSI (Received Signal Strength Indicator) is used to estimate the distance between the walking stick and the BLE beacons. The relationship between RSSI and distance can be approximated using the following formula:

   \[
   \text{Distance} = 10^{\left(\frac{\text{Measured RSSI} - \text{RSSI at 1 meter}}{10 \times n}\right)}
   \]

   Where:
   - **Measured RSSI**: The RSSI value read by the ESP32.
   - **RSSI at 1 meter**: The RSSI value expected at a distance of 1 meter from the beacon (this is usually a negative value and can be obtained through calibration).
   - **n**: The environmental factor (path-loss exponent), which typically ranges from 2 to 4 depending on the indoor environment. A value of 2 is used for free space, while higher values are used for more obstructed environments.


## Future Improvements

- **Integrate GPS for Outdoor Navigation Capabilities**: Enhance the system for both indoor and outdoor environments.
- **Add More Advanced Obstacle Detection**: Use ultrasonic sensors or LIDAR for improved obstacle avoidance.
- **Develop a Mobile App**: Provide an app for easier destination input and system configuration.
- **Implement Machine Learning Algorithms**: Use AI for more accurate and adaptive navigation guidance.
- **Incorporate Ultra-Wideband (UWB) Technology**: Improve indoor positioning accuracy with UWB for more precise location tracking.
- **Enhance Voice Guidance Capabilities**: Integrate dynamic voice feedback to provide real-time navigation instructions and alerts.
- **Add Haptic Feedback**: Implement vibrations or tactile responses to provide directional cues and alerts, enhancing the user experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the open-source community for providing resources and libraries that made this project possible.
