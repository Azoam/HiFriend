import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

#fix random seed
seed = 9
numpy.random.seed(seed)
filename = 'data_sam.csv'
#filename = 'data_ez.csv'
savename = 'gesture_model_sam.h5'
#savename = 'gesture_model_ez.h5'
matrixfile = 'dataset.txt'

#load 
df = pandas.read_csv(filename, header=None)
dataset = df.values
numpy.random.shuffle(dataset)
numpy.savetxt(matrixfile, dataset)
X = dataset[:, 0:500].astype(float)
Y = dataset[:, 500].astype(int)
def baseline_model():
	#create model
	model = Sequential()
	model.add(Dense(output_dim = 500, input_dim = 500, activation = 'tanh'))
	model.add(Dense(output_dim = 5, init = 'uniform', activation='softmax'))
	#compile
	model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
	model.save(savename)

 	return model


estimator = KerasClassifier(build_fn=baseline_model, epochs=100, batch_size=100, verbose=1)
kfold = KFold(n_splits = 5, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
mfile = open("metrics.txt", "a")
mfile.write("Baseline: %.2f%% (%.2f%%)\n" %  (results.mean()*100, results.std()*100))


mfile.close()
#print(encoder.inverse_transform(predictions))


