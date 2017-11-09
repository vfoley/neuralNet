#! /usr/bin/python3
from weatherInput import *
from classInput import *
import random
# each entry in noramlized array is an array of the input 
# values to be passed through the array.
# the last value in each entry is the expected or correct outcome
normalized_weather = weather_array()
normalized_class = class_array()
BIAS_VALUE = 1

#returns layer of weights ranomized -.5 <= w <= .5
def randomize_node_weights(num):
    node = []
    for i in range(0,num):
        node.append(random.uniform(-.5,.5))
    
    return node

#returns entry passed through node
def return_weighted_input(node=[],input=[]):
    weighted_value = 0
    weighted_input = []
    for i in range(0,len(node)):
        weighted_value += BIAS_VALUE
        for j in range(0,len(node)):
            #summation of weights to each node.
            weighted_value += (node[i]*input[j])
        weighted_input.append(weighted_value)
    return weighted_input
# start the process of training 
# each layer represented by an array holding weights
# to be applied to the data
# in for loop call function to perform calculation and
# store data in Transition array.
# evaluate the accuracy of the training

layers = []
transition_array = []
layers.append(randomize_node_weights(4))

for line in normalized_weather:
    for node in layers:
        transition_array.append(return_weighted_input(node, line))

for line in transition_array:
    print(line)
            


#end
