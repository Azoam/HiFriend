#import numpy
import time
import sys
#import pandas
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.wrappers.scikit_learn import KerasClassifier
#from keras.utils import np_utils
#from sklearn.model_selection import cross_cal_scare
#from sklearn.model_selection import KFold
#from sklearn.preprocessing import LabelEncoder
#from sklearn.pipline import Pipeline
from PyoConnect import *
myo1 = Myo(None, tty=sys.argv[1] if len (sys.argv) >= 2 else None)
myo2 = Myo(None, tty=sys.argv[2] if len (sys.argv) >= 2 else None)
featureVector = np.array([])
classifySam = np.array([])
classifyEzra = []
sam = ""
ezra = ""
MAX = 2000
ITERATION = 0
SAMPLES = 100

def something(quat, acc, gyro, tty):
    global featureVector
    global ITERATION
    global SAMPLES
    for x in quat:
        featureVector.append(x)
    for x in acc:
        featureVector.append(x)
    for x in gyro:
        featureVector.append(x)
    if len(featureVector) >= MAX:
        print("ITERATION: "+str(ITERATION))
        ITERATION+=1
        for x in range(0,1500):
            with open('data_sam.csv','a') as file:
                file.write(str(featureVector[x])+",")
        with open('data_sam.csv','a') as file:
            file.write("2\n")
            SAMPLES -= 1
            if SAMPLES < 0:
                print("Done")
                sys.exit(0)
        featureVector = []


def test(quat, acc, gyro, tty):
   global classifySam
   global classifyEzra
   global sam
   global ezra
   for x in quat:
       if tty == "/dev/ttyACM0":
           classifySam.append(x)
        else:
            classifyEzra.append(x)
    for x in acc:
        if str(tty) == "/dev/ttyACM1":
            classifySam.append(x)
        else:
            classifyEzra.append(x)
    for x in gyro:
        if str(tty) == "/dev/ttyACM1":
            classifySam.append(x)
        else:
            ezra += str(x)+","
    if len(classifySam) >= 1000 and len(classifyEzra) >= 1000:
        samArr = model.predict((classifySam[:500]+classifySam[500:])/2)
        #ezraArr = model.predict((classifyEzra[:500]+classifyEzra[500:])/2)
        print(samArr)
        #print(ezraArr)
        classifySam = np.array([])
        classifyEzra = np.array([])


myo1.add_imu_handler(test)
myo2.add_imu_handler(test)
print("STARING IN 5 SECONDS!")#time.sleep(5)
time.sleep(5)
myo1.connect()
myo2.connect()
try:
    while True:
        myo1.run(1)
        myo2.run(1)
except KeyboardInterrupt:
    pass
finally:
    myo1.disconnect()
    myo2.disconnect()
