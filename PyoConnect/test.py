from PyoConnectLib import *
myo = Myo(sys.argv[1] if len (sys.argv) >= 2 else None)


def something(pose):
    print("AAAAH"+str(pose))





myo.add_pose_handler(something)
myo.connect()
try:
    while True:
        myo.run(1)
except KeyboardInterrupt:
    pass
finally:
    myo.disconnect()
