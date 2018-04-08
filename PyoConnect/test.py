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
from PyoConnectLib import *
myo = Myo(sys.argv[1] if len (sys.argv) >= 2 else None)
featureVector = []
MAX = 2000
ITERATION = 0
SAMPLES = 100

def something(quat, acc, gyro):
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





myo.add_imu_handler(something)
print("STARING IN 5 SECONDS!")
time.sleep(5)
myo.connect()
try:
    while True:
        myo.run(1)
except KeyboardInterrupt:
    pass
finally:
    myo.disconnect()
