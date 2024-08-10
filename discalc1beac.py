import asyncio
from bleak import BleakScanner
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading

TARGET_MAC = "E8:DB:84:04:3F:4A" 

def calculate_distance(rssi, tx_power=-59, decimals=2):
    n = 2.0
    try:
        distance = 10 ** ((tx_power - rssi) / (10 * n))
        distance = round(distance, decimals)
    except ZeroDivisionError:
        distance = float('inf')
    return distance

async def scan_ble_device(target_mac):
    try:
        devices = await BleakScanner.discover(timeout=10)
        for dev in devices:
            if dev.address.lower() == target_mac.lower():
                return dev.rssi
    except Exception as e:
        print(f"Error during BLE scan: {e}")
    return None

def run_event_loop(loop, target_mac, rssi_container):
    asyncio.set_event_loop(loop)
    rssi = loop.run_until_complete(scan_ble_device(target_mac))
    rssi_container[0] = rssi
    print(f"Debug: RSSI value fetched: {rssi}")

def update_plot(frame, ax, target_mac, loop, rssi_container):

    thread = threading.Thread(target=run_event_loop, args=(loop, target_mac, rssi_container))
    thread.start()
    thread.join()

    # Get the latest RSSI value
    rssi = rssi_container[0]
    print(f"Debug: RSSI value used for calculation: {rssi}")
    
    if rssi is not None:
        distance = calculate_distance(rssi)
    else:
        distance = np.nan 
    
    print(f"Debug: Calculated distance: {distance}")

  
    ax.clear()
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    
    beacon_position = (0, 0)
    device_position = (distance, 0) if not np.isnan(distance) else (np.nan, np.nan)
    
    ax.plot(beacon_position[0], beacon_position[1], 'bo', label="Beacon")
    ax.plot(device_position[0], device_position[1], 'ro', label="Estimated Device")
    
    ax.legend()
    ax.grid(True)
    ax.set_xlabel('X-axis (meters)')
    ax.set_ylabel('Y-axis (meters)')
    ax.set_title('BLE Device Location Estimation')

def main():
    fig, ax = plt.subplots()
    target_mac = TARGET_MAC
    loop = asyncio.new_event_loop()
    rssi_container = [None] 

    ani = animation.FuncAnimation(
        fig,
        update_plot,
        fargs=(ax, target_mac, loop, rssi_container),
        interval=5000, 
        blit=False
    )

    plt.show()

if __name__ == "__main__":
    main()
