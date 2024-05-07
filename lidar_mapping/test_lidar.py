from rplidar import RPLidar

lidar = RPLidar('/dev/ttyUSB0')
lidar.clear_input()  # Attempt to clear any residual data in buffer

try:
    print("Lidar Info:", lidar.get_info())
    health = lidar.get_health()
    print("Lidar Health:", health)

    if health[0] == 'Good':
        lidar.start_motor()
        for i, scan in enumerate(lidar.iter_scans(max_buf_meas=200)):
            print(f'{i}: Got {len(scan)} measurements')
            if i > 10:
                break
finally:
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
