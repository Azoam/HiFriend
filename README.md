# HiFriend | HackNY - 2019
    0. The Plan
    1. Reading in data from Myo Armbands
    2. Classifying and Training
    3. Averaging over a time period
    4. API's
    5. Problems and Potential Solutions


## The Plan
The idea for this application was to train a machine learning model different gestures, with the help of the Myo Armband, by using the large amounts of data that the Armband spit out across some time period. Each gesture we taught the armband we wanted to do something with it - Venmo transactions on hand shake, social medial communication on high five, calling your friend with a calling gesture, and much more.


## Reading in data from Myo Armbands
Because we were using a dragon board in order to read in bluetooth information and the Myo SDK is not compatible with Linux machines, we had to find a specific library that was a wrapper around the Myo SDK that allowed for linux development. We found a great library called PyoConnect by Fernando Cosentino which gave us these capabilities. The only thing was, this library didn't seem to allow for multiple armbands to be connected to the same application at once and this is very necessary
if want a specific action happening when both people do a certain action. It would be possible using a file for communication but we all know how slow I/O communication can be, therefore we wanted the library to connect multiple without the need to run up a new application.

What we did was made some edits to the library code so that it could notice two armbands at a time. After this we wrote up our own function that collected data from the armband (acceleration, gyroscope information, muscle contraction information) and comma separated each element (the last element being the class or gesture). Because the armband is spitting out a lot of information at once, we decided to make our feature vectors 500 * 9 data points. 9 datapoints corresponding to the 9
points it can measure in less than second and 500 of these 9 data points in one vector. We got around 300 feature vectors for each class. Once we had our data comma separated we went to the next stage of neural networks -> training our model.
## Classifying and Training

## Averaging over a time period
Once we got our model we were able to do averaging over a time period, (so about 1000 points were measured before it stopped and averaging downt to 500 points) we were able to define a gesture every 5 seconds (5 seconds is sufficient enough to change state without too much overlap from other states and noise). So when we predicted the average on both armbands we defined states where an example is -> state 1: Both people are shaking their hands -> logic.

##API's

##Problems and Potential Solutions
Unfortunately we were not able to demo and the reason was hardware. The Dragon board did not supply use with the hardware we needed. We spent most of our time downloading dependencies, fixing network errors, and downloading tensorflow. Tensorflow is not an easy library to download to begin with and putting it on such a small machine with its own Debian distribution of Linux spilled disaster every where.

Of course we could have dealt with this issue by using another device that could maintain communication with the bluetooth armbands, but most of these were taken and we were determined to make it work. If we ever get a chance to work with those armbands again, we would defintely use a different mini computer (probably a respberry pi).


