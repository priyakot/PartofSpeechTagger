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

def generateNER(inputData, modelfile):
    trainingFileData = ''
    lineData = []
    line = []

    line = inputData.split('\n')

    for j in range(len(line)):
        lineData.extend(line[j].split(' '))

    for i in range(len(lineData)):
        if len(lineData[i]) > 0:
            data = lineData[i].strip().rsplit('/', 1)

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
            tag = 'TEST'

            trainingFileData += tag + ' ' + posTag + ' ' + prePreWord + ' ' + preWord + ' ' + pfxWord + ' ' + \
                                currentWord + ' ' + sfxWord + ' ' + nextWord + ' ' + nextNextWord + '\n'

    f = open(perceptronPath+"ner_tag.txt", 'w')
    f.write(trainingFileData)
    f.close()

    getPredictedTags(modelfile,perceptronPath+"ner_tag.txt", inputData)


def main():
    modelfile = ''

    modelfile = str(sys.argv[1])
    inputData = ''

    print('Enter the input data:')
    while True:
        line = input().strip()

        if not line:
            break
        else:
            inputData += line + '\n'

    generateNER(inputData, modelfile)


if __name__ == '__main__':
    main()