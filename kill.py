
from djitellopy import Tello

if __name__ == '__main__':
    drone = Tello()
    drone.connect()
    drone.land()
    drone.end()
