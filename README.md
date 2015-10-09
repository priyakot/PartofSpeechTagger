<<<<<<< HEAD
ASSIGNMENT 2
PRIYA KOTWAL

IMPORTANT : Please change the path of the perceptronPATH to the path of the directory containing perceplearn.py and
percepclassify.py in the files: postrain.py, postag.py, nelearn.py, netag.py

PART 1: Averaged Perceptron classifier

	The averaged perceptron classifier is set to 26 iterations and gives good accuracy at this limit
	While training the pecerptron, each iteration takes about 2 mins on the pos.train model file and overall 52 mins. 
	This perceptron is almost at par with the Megam
	The format of the training file to the perceptron should be TAG FEATURE FEATURE FEATURE....
	The model file is to be a *.nb file for faster processing.
	The perceptron classifier takes a model file as input and outputs the right tag 
	
	Commands:
	1. perceplearn.py
	   python3 perceplearn.py training_file model_file
	
	2. percepclassify.py
	   python3 percepclassify.py model_file
	   STDIN -> input
	   output-> STDOUT

PART 2: Part-of-speech tagger

	The postrain.py is used for generating an intermidiate model file in the form TAG FEATURE FEATURE FEATURE.. 
	This file will be the input/ training file to the perceptron which is called with a subprocess call
	MegaM can also be alternately used instead of the perceptron in the subprocess call.
	The postag takes the test file(words with no tags) and produces a file in the same format as above which will be the input/ testing file to the percepclassify which is called with a subprocess call
	MegaM can also be alternately used instead of the perceptron in the subprocess call.
	The following is used while converting the input file to the intermidiate file:
			prePreWord = 'pp_word:'
            preWord = 'p_word:'
            currentWord = 'curr_word:' + data[0]
            nextWord = 'n_word:'
            nextNextWord = 'nn_word:'
            pfxWord = "pfx:"
            sfxWord = "sfx:"

In the postrain.py : 
-Please specify the path of the perceptron in the peceptronPATH variable
-For example: perceptronPATH = /Users/priyakotwal/Documents/sharedUbuntu/544/csci544-hw2-WORKING/
-The intermidiate file will be created at perceptronPATH+'post_model.txt'
-The subprocess call will be as follows:
 subprocess.call(['python3',perceptronPath+"perceplearn.py", trainingfile,modelfile],
                         stdout=f, stderr=subprocess.PIPE)

	Commands:
   1. postrain.py
   	  python3 postrain.py TRAININGFILE MODEL
   
   2. postag.py
      python3 postag.py MODEL
      STDIN -> input
	  output-> STDOUT
 
 PART 3: Named Entity Recognition  
    1. nelearn.py  
       python3 nelearn.py TRAININGFILE MODEL
    2. netag.py
      python3 netag.py MODEL
      STDIN -> input
	  output-> STDOUT 


1. Part-of-speech tagger
   part-of-speech tagger using averaged perceptron :
   
   a. dev.pos accuracy   : 0.9500224338202303 
   b. train.pos accuracy : 0.9949575298850114 
   
   part-of-speech tagger using MegaM
   
   a. dev.pos accuracy   : 0.959319
   b. train.pos accuracy : 99.859319
   
2. Named Entity Recognizer

   a. 
Entity      		Precision		Recall			F - Score
PER					0.852113128211	0.826405864785	0.83906263742294
ORG					0.841145223764	0.715671716532	0.77335212710291
LOC					0.661752343126	0.801463155134	0.72493781192145
MISC				0.696124031008	0.421459861535	0.52504038341539
Overall without 'O'	0.780213283784	0.682536348309	0.72811356630339
Overall with 'O'	0.951078965697	0.951076455697	0.95107771069534

   b. Overall F-score : 0.67831684737228
   
   
3. What happens if you use your Naive Bayes classifier instead of your perceptron classifier (report performance metrics)? 
   Why do you think that is?  
   
   
    
   
   
   
   
   
   
=======
ASSIGNMENT 2

PRIYA KOTWAL



PART 1: Averaged Perceptron classifier



	The averaged perceptron classifier is set to 26 iterations and gives good accuracy at this limit

	While training the pecerptron, each iteration takes about 2 mins on the pos.train model file and overall 52 mins. 

	This perceptron is almost at par with the Megam

	The format of the training file to the perceptron should be TAG FEATURE FEATURE FEATURE....

	The model file is to be a *.nb file for faster processing.

	The perceptron classifier takes a model file as input and outputs the right tag 

	

	Commands:

	1. perceplearn.py

	   python3 perceplearn.py training_file model_file

	

	2. percepclassify.py

	   python3 percepclassify.py model_file

	   STDIN -> input

	   output-> STDOUT



PART 2: Part-of-speech tagger



	The postrain.py is used for generating an intermidiate model file in the form TAG FEATURE FEATURE FEATURE.. 

	This file will be the input/ training file to the perceptron which is called with a subprocess call

	MegaM can also be alternately used instead of the perceptron in the subprocess call.

	The postag takes the test file(words with no tags) and produces a file in the same format as above which will be the input/ testing file to the percepclassify which is called with a subprocess call

	MegaM can also be alternately used instead of the perceptron in the subprocess call.

	The following is used while converting the input file to the intermidiate file:

			prePreWord = 'pp_word:'

            preWord = 'p_word:'

            currentWord = 'curr_word:' + data[0]

            nextWord = 'n_word:'

            nextNextWord = 'nn_word:'

            pfxWord = "pfx:"

            sfxWord = "sfx:"



	Commands:

   1. postrain.py

   	  python3 postrain.py TRAININGFILE MODEL

   

   2. postag.py

      python3 postag.py MODEL

      STDIN -> input

	  output-> STDOUT

 

 PART 3: Named Entity Recognition  

    1. nelearn.py  

       python3 nelearn.py TRAININGFILE MODEL

    2. netag.py

      python3 netag.py MODEL

      STDIN -> input

	  output-> STDOUT 





1. Part-of-speech tagger

   part-of-speech tagger using averaged perceptron :
   a. dev.pos accuracy   : 0.9500224338202303 

   b. train.pos accuracy : 0.9949575298850114 

   

   part-of-speech tagger using MegaM
   a. dev.pos accuracy   : 0.959319

   b. train.pos accuracy : 99.859319

   

2. Named Entity Recognizer



   a. 

Entity      		Precision		Recall			FScore

PER					0.849553128103	0.822200864969	0.8356532356532357

ORG					0.830288266342	0.666992824527	0.7397359377826008

LOC					0.653990024938	0.794095382286	0.7172649572649573

MISC				0.696124031008	0.408553230209	0.5149082568807339

Overall without 'O'	0.781147784716	0.694330646227	0.735185055622

Overall with 'O'	0.953800804943	0.953800804943	0.953800804943


   b. Overall F-score : 0.652569856702

    

3. What happens if you use your Naive Bayes classifier instead of your perceptron classifier (report performance metrics)? 

   Why do you think that is?
   What happens if you use your Naive Bayes classifier instead of your perceptron classifier (report performance metrics)? 
   Why do you think that is?  
   Accuracy Perceptron :0.9949575298850114 
   Accuracy Naive Bayes: 0.9033167485974351
   
   The performance reduces due to the Naive Bayes Classifier since the perceptron is used for establishing linear relationships such as whether the document belongs to the class or not.
   If this is not true then it averages multiple times. This average helps in achieving a better accuracy whereas the Naive Bayes Classifier iterates only once over the data and chooses the most probable one
   It does not give a finite answer like the perceptron but a close one which maybe wrong whereas in the perceptron a finite answer is obtained and if it is wrong and not the predicted one it is averaged over till some convergence is obtained.
    
   
   
   
   
>>>>>>> 84cb58cd1500c17633908ef1478f6b0bc8bb9974
