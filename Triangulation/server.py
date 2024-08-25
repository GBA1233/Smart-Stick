import socket
import matplotlib.pyplot as plt

# ESP32 IP and port
esp32_ip = "192.168.1.100"  # Replace with your ESP32's IP address
esp32_port = 80

# Set up the socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((esp32_ip, esp32_port))

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

try:
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if "Estimated Location" in data:
            print(data)
            parts = data.split(",")
            x = float(parts[0].split('=')[1].strip())
            y = float(parts[1].split('=')[1].strip())
            plot_location(x, y)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client_socket.close()
