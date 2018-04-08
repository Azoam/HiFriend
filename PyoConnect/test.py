from PyoConnectLib import *
myo = Myo(sys.argv[1] if len (sys.argv) >= 2 else None)


def something(quat, acc, gyro):
    print("QUAT"+str(quat))
    print("ACC"+str(acc))
    print("GYRO"+str(gyro))





myo.add_imu_handler(something)
myo.connect()
try:
    while True:
        myo.run(1)
except KeyboardInterrupt:
    pass
finally:
    myo.disconnect()
