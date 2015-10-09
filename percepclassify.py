from collections import Counter, defaultdict
import re
import sys
import random
import math
import os
import operator
import pickle

# Author: Priya Kotwal
# Command : python3 percepclassify.py model_file testing_file

wavg = defaultdict(Counter)

def tokenize(text):
    return re.findall('[a-z0-9]+', text)

def tokenize1(text):
    return text.split(' ')
    
def classify(wavg, features):
    max_wt = -99999999
    resultClass = random.choice(list(wavg.keys()))
    for eachClass, val in wavg.items():
        if eachClass != "Default":
            sum = 0
            for feature in features:
                sum += wavg[eachClass][feature]
            if sum > max_wt:
                resultClass = eachClass
                max_wt = sum
    return resultClass
 
    
def readTestingFile(fileName):
    return [line.strip().split('\n') for line in open(fileName,errors='ignore').readlines()]

def main():
    count = 0
    argsLength = len(sys.argv)
    modelFile = sys.argv[1]
    if argsLength > 2:
    	testingFile = sys.argv[2]
    total = 1
    correct = 0
    
    with open(modelFile, 'rb') as handle:
        wavg = pickle.load(handle)
    
    if argsLength == 2:
    	print('Enter the data: ')
    	data = input()
    	actualClass = data.split(' ',1)[0]
    	featuresC = data.split(' ',1)[1]
    	features = tokenize1(featuresC)    
    	resultClass = classify(wavg, features)
    	print(resultClass)
    else:    
    	with open(testingFile,errors='ignore') as file:
        	for doc in file:
        		actualClass = doc.split(' ',1)[0]
        		featuresC = doc.split(' ',1)[1]
        		features = tokenize1(featuresC)    
        		resultClass = classify(wavg, features)
        		total += 1
        		print(resultClass)
        		"""print('Actual class | Predicted class: ',actualClass,'|',resultClass)
            	if actualClass == resultClass:
                	correct += 1
    	print('Accuracy: ',float(correct/total), ' total: ',total, ' correct: ',correct)"""
    
   
if __name__ == '__main__':
    main()