import os
import subprocess
import sys

perceptronPath = '/Users/priyakotwal/Documents/sharedUbuntu/544/csci544-hw2-WORKING/'

def getPredictedTags(modelfile, testFile, inputData):
    p = subprocess.call(['python3',perceptronPath+"percepclassify.py", modelfile,testFile],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (output, err) = p.communicate()
    getResult(inputData, output)


def getResult(input, output):
    linesOutput = output.split('\n')
    linesInput = input.split('\n')
    tags = []
    words = []
    resultStr = ''

    for i in range(len(linesOutput)):
        if len(linesOutput[i]) > 0:
            item = linesOutput[i].split('\t')
            tags.append(item[0])

    for j in range(len(linesInput)):
        if len(linesInput[j]) > 0:
            words.extend(linesInput[j].split(' '))

    count = 0
    inputRowsIndex = 0;
    for j in range(len(words)):
        resultStr += words[j] + '/' + tags[j] + ' '
        count += 1

        if count == len(linesInput[inputRowsIndex].split(' ')):
            count = 0
            inputRowsIndex += 1
            resultStr = resultStr.strip() + '\n'

    print(resultStr)



def generatePOS(inputData, modelfile):
    trainData = ''
    inputLine = []
    line = []

    line = inputData.split('\n')

    for j in range(len(line)):
        inputLine.extend(line[j].split(' '))

    for i in range(len(inputLine)):
        if len(inputLine[i]) > 0:
            data = inputLine[i]

            prePreWord = 'pp_word:'
            preWord = 'p_word:'
            currentWord = 'curr_word:' + data
            nextWord = 'n_word:'
            nextNextWord = 'nn_word:'
            pfxWord = "pfx:"
            sfxWord = "sfx:"

            if len(data) < 2:
                pfxWord += data[:len(data)]
            else:
                pfxWord += data[:2]

            if len(data) < 2:
                sfxWord += data[:len(data)]
            else:
                sfxWord += data[-2:]

            if i >= 2:
                prePreWord += inputLine[i-2]
            if i >= 1:
                preWord += inputLine[i-1]
            if i+1 < len(inputLine):
                nextWord += inputLine[i+1]
            if i+2 < len(inputLine):
                nextNextWord += inputLine[i+2]

            trainData += 'TEST ' + prePreWord + ' ' + preWord + ' ' + pfxWord + ' ' + \
                                currentWord + ' ' + sfxWord + ' ' + nextWord + ' ' + nextNextWord + '\n'

    f = open(perceptronPath+"pos_tag.txt", 'w')
    f.write(trainData)
    f.close()

    getPredictedTags(modelfile,perceptronPath+"pos_tag.txt", inputData)


def main():
    modelfile = ''

    modelfile = str(sys.argv[1])
    inputData = ''
    print('Enter the input:')
    while True:
        line = input().strip()

        if not line:
            break
        else:
            inputData += line + '\n'

    generatePOS(inputData, modelfile)


if __name__ == '__main__':
    main()