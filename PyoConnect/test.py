from PyoConnectLib import *
myo = Myo(sys.argv[1] if len (sys.argv) >= 2 else None)


def something(quat, acc, gyro):
    featureVector = []
    for x in quat:
        featureVector.append(x)
    for x in acc:
        featureVector.append(x)
    for x in gyro:
        featureVector.append(x)
    





myo.add_imu_handler(something)
myo.connect()
try:
    while True:
        myo.run(1)
except KeyboardInterrupt:
    pass
finally:
    myo.disconnect()
