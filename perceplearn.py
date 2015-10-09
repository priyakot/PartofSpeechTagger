from collections import Counter, defaultdict
import re
import sys
import random
import math
import os
import operator
import pickle

# Author: Priya Kotwal
# Command : python3 perceplearn.py training_file model_file

wv = defaultdict(Counter)
wavg = defaultdict(Counter)
wavgFinal = defaultdict(Counter)
wavgVector = defaultdict(Counter)

def tokenize(text):
    return re.findall('[a-z0-9]+', text)

def tokenize1(text):
    return text.split(' ')
    
def perceptrain(fileName): 
    features = defaultdict(int)
    error = 0
    correct = 0
    total = 0
    accuracy = 0.0
    iterCount = 26
    predClass = "Default"
    max_wt = -999999
    for i in range(0,iterCount):
        total = 0
        accuracy = 0.0
        correct = 0
        error = 0
        with open(fileName,errors='ignore') as file:
            data = [ (random.random(), line) for line in file ]
            data.sort()
            for _,doc in data:
                actualClass = doc.split(' ',1)[0]
                featuresC = doc.split(' ',1)[1]
                features = tokenize1(featuresC)    
                if actualClass:
                    predClass, max_wt = predictClass(actualClass,features, predClass, max_wt)
    
                    if predClass == "Default":
                        updateWeights(actualClass, features)
                        #updateAVGClass(wv.keys(), features)
            
                    elif predClass != actualClass and predClass != 'Default':
                        updateWeights(actualClass,features)
                        reduceWeights(predClass,features)
                        #updateAVGClass(wv.keys(), features)
                        error += 1
                    else:
                        #updateAVGClass(wv.keys(), features)
                        correct += 1
                total += 1
            
            print(i, ' Accuracy: ',correct,' ',total,' ',float(correct/total)*100)  

    return wv
                
def predictClass(actualClass,features, resultClass, max_wt):
    """resultClass = "Default"
    max_wt = -9999999"""
    getMaxClass = defaultdict(int)
    for classC in wv.keys():    
        sum = 0
        for feature in features:
            sum += wv[classC][feature]
        getMaxClass[classC] = sum
        resultClass = max(getMaxClass, key=getMaxClass.get)
        max_wt = getMaxClass.get(resultClass)

    return (resultClass,max_wt)

def updateWeights(actualClass, features):
    for feature in features:
        wv[actualClass][feature] += 1
        
def reduceWeights(predClass,features):
    for feature in features:
        wv[predClass][feature] -= 1

def updateAVg(anyClass, features):
    for feature in features:
        wavg[anyClass][feature] += wv[anyClass][feature]    
        
def updateAVGClass(allClasses, features):
    for anyClass in allClasses:
        for feature in features:
            wavg[anyClass][feature] += wv[anyClass][feature]  
        
def main():
    trainingFile = sys.argv[1]
    modelFile = sys.argv[2]
    wavgVector = perceptrain(trainingFile)
    
    
    with open(modelFile, 'wb') as handle:
        pickle.dump(wavgVector, handle)

    
if __name__ == '__main__':
    main()