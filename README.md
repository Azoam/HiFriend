# HiFriend | HackNY - Spring 2018
    0. The Plan
    1. Reading in data from Myo Armbands
    2. Classifying and Training
    3. Averaging over a time period
    4. API's
    5. Problems and Potential Solutions


## The Plan
The objective of this application was to train a program to recognize different Myo Armband gestures through machine learning. We aimed to do this with the help of the Myo Armband becasue of the large amounts of data that the Armband can spit out across a short time period. We wanted each recognized gesture to cue an action - e.g. Venmo transactions on a hand shake, social medial communication on a high five, calling a friend with a calling gesture, and much more.  The hack was called HiFriend because it was meant to feature social interactions that could be done between two Armband users at once.


## Reading in data from Myo Armbands
Because we were using a DragonBoard in order to read in Bluetooth information and the official Myo SDK was not compatible with Linux, we had to find a library that allowed for linux development. We found a great library called PyoConnect by Fernando Cosentino which gave us these capabilities. However, this library did not apparently allow for multiple Myo Armbands to be connected to the same application at once, and this was a very necessary feature for HiFriend. While it would be possible to do this by using a file for communication, we were aware of how slow communication can be through file read/write, therefore we insisted that the library be able to connect multiple peripherals without the need of running a new application instance.

What we did was make some edits to the library code so that it could support two armbands at a time. After this we wrote up our own function that collected data from the armband (acceleration, gyroscope information, muscle contraction information) and comma separated each element (the last element being the class or gesture). Because the armband was spitting out a lot of information at once, we decided to make our feature vectors 500 * 9 data points: 9 datapoints corresponding to the 9
points it can measure in less than a second by 500 sets of these 9 data points in one vector. During training, we collected around 300 feature vectors for each gesture. Once we had our data comma separated, we went to the next stage of neural networks: training our model.

## Classifying and Training
The neural network's chief objective was to properly classify a stream of EMG data into the 5-7 custom gestures we intended to train it on.  Once an appropriate model was acheived, the model could be deployed on-line.  This goal fell under the category of multi-class classification, so we decided to use Keras, a deep-learning framework which is capable of running on Theano and TensorFlow.  Keras was easy to adapt, and also allowed us to add as many or as little layers as we wished when creating our model.

The procedure for training the model went along the following:  For some amount of time, a team member would wear the Myo armband and practice a gesture several times while raw EMG data was stored and formatted a CSV.  The single digit appended to the end of each feature vector was used to form our output variable vector. An example of some of the data we worked with is available for view in 'dataset.txt', and the CSV format of the same is viewable in 'data_sam.csv'. The data was then fed into the compiled model so it could be evaluated for realtime use.

The Keras model itself was built with two densely connected layers.  The input layer used arctan as its activation function, while the output layer used softmax.  Once we got the Keras model to work on the training data, we evaluated its performance and results through K-fold cross evaluation.  For this part, we used the scikit-learn library.  After enough data was collected, and we had a better idea of how to tweak the parameters, we acheived some very promising results for our gesture classification model.  Some of our K-fold results are recorded below, in the format of mean accuracy%(std-dev%): 

+ Baseline: 98.96% (0.72%)
+ Baseline: 98.71% (0.83%)
+ Baseline: 98.52% (1.10%)
+ Baseline: 98.46% (0.72%)
+ Baseline: 91.64% (2.34%)
+ Baseline: 98.83% (0.88%)
+ Baseline: 98.22% (0.36%)

The data above is available in 'metrics.txt'.  We moved forward with saving the model and aimed to deploy it on the DragonBoard once the two separate connections to the armbands were established.  We hoped that with a high enough accuracy, the model could be used for the on-line predictions which would guide the logic for the rest of the application.  Each classified gesture would correspond to a unique API call, such as sending a text message via Twilio or a initiating a transaction via Stripe or Venmo.  Following a successful API call, the process would be put to sleep for a few seconds to allow the band users to reset to neutral positions.

## Averaging over a time period
Once we finalized our model, we were able to begin averaging over time periods such that about 1000 EMG data points were measured in an interval. In turn, the 1000 points averaged down to 500 points.  From this, we were able to define/identify a gesture every 5 seconds (5 seconds being sufficient enough to change state without too much overlap from other states and noise). Hence, when we predicted the average on both armbands, we could define discrete states, an example being -> state 1: Two people are shaking hands -> logic -> initiation of Stripe/Venmo charge -> successful notification -> sleep -> state neutral(0) : Both people with their hands in neutral position.

## API's

## Problems and Potential Solutions
Unfortunately we were not able to demo, due to a hardware selection error. The DragonBoard did not supply us with the hardware or processing power we needed, despite its reported specs. We spent most of our time downloading dependencies, fixing network errors, and downloading numpy and Tensorflow. Tensorflow is not an easy library to download to begin with, and putting it on such a small machine with its own Debian distribution of Linux resulted in disaster.  An estimated 4 hours minimum of development time was wasted due to this issue - downloading dependencies deadlocked the device, preventing any of us from testing or even pulling our code onto it.

Of course we could have dealt with this issue by using another device that could maintain communication with the bluetooth armbands, but most of these were taken and we were determined to make it work. If we ever get a chance to work with those armbands again, we would defintely use a different mini computer (probably a Raspberry Pi).


