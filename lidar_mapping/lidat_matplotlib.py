import os
from math import floor, radians
import matplotlib.pyplot as plt
from adafruit_rplidar import RPLidar

# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3)
lidar.connect()
lidar.start_motor()
lidar.start()
# Initialize the plot
plt.ion()  # Turn on interactive plotting
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
line, = ax.plot([], [], 'b.')  # Initial empty plot
ax.set_theta_zero_location('N')  # Set the direction of the 0 degree
ax.set_theta_direction(-1)  # Set the rotation direction (clockwise)
ax.set_ylim(0, 4000)  # Set the radius limit

fig.canvas.draw()  # Perform an initial draw to cache the renderer

def update_plot(scan_data):
    angles = [radians(angle) for angle in range(360)]
    line.set_xdata(angles)  # Set angles
    line.set_ydata(scan_data)  # Set distances
    ax.draw_artist(ax.patch)
    ax.draw_artist(line)
    fig.canvas.draw()  # Update the full figure
    fig.canvas.flush_events()  # Handle GUI events

scan_data = [0]*360

try:
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
        update_plot(scan_data)

except KeyboardInterrupt:
    print('Stopping.')
finally:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    plt.close(fig)

