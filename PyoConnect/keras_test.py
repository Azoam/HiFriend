import numpy
import pandas
from keras.models import load_model


savename = ('gesture_model_sam.h5') 
model = load_model(savename)

dataset = numpy.loadtxt('dataset.txt')

numpy.random.shuffle(dataset)

X = dataset[:, 0:500].astype(float)
Y = dataset[:, 500].astype(int)


pred = model.predict(X[15:30, 0:500], verbose = 0)

for arr in pred:
	m = max(arr)
	print(numpy.argmax(arr))
print(Y[15:30])



