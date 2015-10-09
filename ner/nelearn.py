import os
from os import listdir
import subprocess
import sys

perceptronPath = '/Users/priyakotwal/Documents/sharedUbuntu/544/csci544-hw2-WORKING/'


def generatePOS(trainingfile, modelfile):
    trainingFileData = ''

    inputData = ''
    lineData = []

    if os.path.isfile(trainingfile):
        with open(trainingfile, 'r',encoding='ISO-8859-15') as file:
            for line in file:
                inputData += line.strip() + ' '

    lineData = inputData.split()

    for i in range(len(lineData)):
        if len(lineData[i]) > 0:
            data = lineData[i].rsplit('/', 2)

            if len(data) != 3:
                print('Incorrect format Word/POSTag/NETag. ')
                break

            tag = ''
            posTag = 'postag:'
            prePreWord = 'pp_word:'
            preWord = 'p_word:'
            pfxWord = "pfx:"
            currentWord = 'curr_word:'
            sfxWord = "sfx:"
            nextWord = 'n_word:'
            nextNextWord = 'nn_word:'

            if len(data[0]) < 2:
                pfxWord += data[0][:len(data[0])]
            else:
                pfxWord += data[0][:2]

            if len(data[0]) < 2:
                sfxWord += data[0][:len(data[0])]
            else:
                sfxWord += data[0][-2:]

            if i >= 2:
                prePreWord += lineData[i-2].split('/')[0]
            if i >= 1:
                preWord += lineData[i-1].split('/')[0]
            if i+1 < len(lineData):
                nextWord += lineData[i+1].split('/')[0]
            if i+2 < len(lineData):
                nextNextWord += lineData[i+2].split('/')[0]

            currentWord += data[0]
            posTag += data[1]
            tag = data[2]

            if tag == '#':
                tag = 'HASH'

            trainingFileData += tag + ' ' + posTag + ' ' + prePreWord + ' ' + preWord + ' ' + pfxWord + ' ' + \
                                currentWord + ' ' + sfxWord + ' ' + nextWord + ' ' + nextNextWord + '\n'

    f = open(perceptronPath+"ner_model.txt", 'w')
    f.write(trainingFileData)
    f.close()
    generateModel(perceptronPath+"ner_model.txt", modelfile)


def generateModel(trainingfile, modelfile):
    f = open(modelfile, 'w',errors='ignore')
    p = subprocess.call(['python3',perceptronPath+"perceplearn.py", trainingfile,modelfile],
                         stdout=f, stderr=subprocess.PIPE)
    f.close()
    print('')
    

def main():
    trainingfile = ''
    modelfile = ''

    argsLength = len(sys.argv)
    if 1 <= argsLength <= 2:
        print('python3 nelearn.py <Training File> <Model File>')
        exit()
    if argsLength == 3:
        trainingfile = str(sys.argv[1])
        modelfile = str(sys.argv[2])
    if argsLength > 3:
        print('Please enter exactly two arguments!')
        exit()

    generatePOS(trainingfile, modelfile)

if __name__ == '__main__':
    main()