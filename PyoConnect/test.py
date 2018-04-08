import numpy
import sys
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_cal_scare
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipline import Pipeline
from PyoConnectLib import *
myo = Myo(sys.argv[1] if len (sys.argv) >= 2 else None)
featureVector = []
MAX = 1500


def something(quat, acc, gyro):
    for x in quat:
        featureVector.append(x)
    for x in acc:
        featureVector.append(x)
    for x in gyro:
        featureVector.append(x)
    if len(featureVector) >= 2000:
        for x in range(0,1500):
            with open('data.csv','a') as file:
                file.write(str(featureVector[x])+",")
        with open('data.csv','a') as file:
            file.write("2\n")
        featureVector = []





myo.add_imu_handler(something)
myo.connect()
try:
    while True:
        myo.run(1)
except KeyboardInterrupt:
    pass
finally:
    myo.disconnect()
