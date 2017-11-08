#! /usr/bin/python3
from weatherInput import *
from classInput import *

# each entry in noramlized array is an array of the input 
# values to be passed through the array.
# the last value in each entry is the expected or correct outcome
normalized_weather = weather_array()
normalized_class = class_array()


# start the process of training 
# each layer represented by an array holding weights
# to be applied to the data
# in for loop call function to perform calculation and
# store data in Transition array.
# evaluate the accuracy of the training
