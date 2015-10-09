import os
from os import listdir
import subprocess
import sys

perceptronPath = '/Users/priyakotwal/Documents/sharedUbuntu/544/csci544-hw2-WORKING/'

def generateModel(trainingfile, modelfile):
    f = open(modelfile, 'w',errors='ignore')
    #p = subprocess.call([megamPath, '-maxi', '3', '-nc', 'multitron', trainingfile],stdout=f, stderr=subprocess.PIPE) """
    p = subprocess.call(['python3',perceptronPath+"perceplearn.py", trainingfile,modelfile],
                         stdout=f, stderr=subprocess.PIPE)
    #./megam -fvals -nc multiclass spam.megam.training.txt
    f.close()
    print('')

def generatePOS(trainingfile, modelfile):
    
    input = ''
    trainData = ''
    lineInput = []

    if os.path.isfile(trainingfile):
        with open(trainingfile, 'r',encoding='ISO-8859-15') as currentfile:
            for line in currentfile:
                input += line.strip() + ' '

    lineInput = input.split()

    for i in range(len(lineInput)):
        if len(lineInput[i]) > 0:
            data = lineInput[i].split('/')

            prePreWord = 'pp_word:'
            preWord = 'p_word:'
            currentWord = 'curr_word:' + data[0]
            nextWord = 'n_word:'
            nextNextWord = 'nn_word:'
            pfxWord = "pfx:"
            sfxWord = "sfx:"

            if len(data[0]) < 2:
                pfxWord += data[0][:len(data[0])]
            else:
                pfxWord += data[0][:2]

            if len(data[0]) < 2:
                sfxWord += data[0][:len(data[0])]
            else:
                sfxWord += data[0][-2:]

            if i >= 2:
                prePreWord += lineInput[i-2].split('/')[0]
            if i >= 1:
                preWord += lineInput[i-1].split('/')[0]
            if i+1 < len(lineInput):
                nextWord += lineInput[i+1].split('/')[0]
            if i+2 < len(lineInput):
                nextNextWord += lineInput[i+2].split('/')[0]

            if data[1] == '#':
                data[1] = 'HASH'

            trainData += data[1] + ' ' + prePreWord + ' ' + preWord + ' ' + pfxWord + ' ' + \
                                currentWord + ' ' + sfxWord + ' ' + nextWord + ' ' + nextNextWord + '\n'

    f = open(perceptronPath+"pos_model.txt", 'w')
    f.write(trainData)
    f.close()

    generateModel(perceptronPath+"pos_model.txt", modelfile)


def main():
    trainingfile = ''
    modelfile = ''

    argsLength = len(sys.argv)
    if 1 <= argsLength <= 2:
        print('python3 postrain.py <Training File> <Model File>')
        exit()
    if argsLength == 3:
        trainingfile = str(sys.argv[1])
        modelfile = str(sys.argv[2])
    if argsLength > 3:
        print('Please enter exactly two arguments')
        exit()

    generatePOS(trainingfile, modelfile)

if __name__ == '__main__':
    main()