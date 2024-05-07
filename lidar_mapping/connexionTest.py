from flask import Flask, Response
import cv2
import numpy as np
from rplidar import RPLidar

app = Flask(__name__)
PORT_NAME = '/dev/ttyUSB0'
DMAX = 4000
IMIN = 0
IMAX = 50

def generate_frames(lidar):
    """Génère des images frame par frame à partir des données du LiDAR."""
    iterator = lidar.iter_scans()
    while True:
        scan = next(iterator)
        image = np.zeros((500, 500, 3), dtype=np.uint8)
        for _, quality, angle, distance in scan:
            if quality == 0:
                continue
            angle_rad = np.radians(angle)
            x = int((distance * np.cos(angle_rad)) / 10)
            y = int((distance * np.sin(angle_rad)) / 10)
            cv2.circle(image, (250 + x, 250 + y), 2, (255, 255, 255), -1)
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Route vidéo qui renvoie le flux vidéo."""
    lidar = RPLidar(PORT_NAME)
    return Response(generate_frames(lidar),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

