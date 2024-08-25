import serial
import matplotlib.pyplot as plt
import time

# Set up the serial connection (replace 'COM3' with the appropriate port)
ser = serial.Serial('COM3', 115200)
time.sleep(2)  # Give time for the connection to establish

x_vals = []
y_vals = []

plt.ion()
fig, ax = plt.subplots()

def plot_location(x, y):
    x_vals.append(x)
    y_vals.append(y)
    ax.clear()
    ax.scatter(x_vals, y_vals)
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    plt.title('Estimated Location')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.draw()
    plt.pause(0.01)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        if "Estimated Location" in line:
            print(line)
            parts = line.split(",")
            x = float(parts[0].split('=')[1].strip())
            y = float(parts[1].split('=')[1].strip())
            plot_location(x, y)
