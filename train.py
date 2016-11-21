import pickle
import nltk
from random import randint
import naive

#Open the dataset pickle file
with open("train_set.pkl",'r') as file:
	train_set = pickle.load(file)

test_set_size = len(train_set)/10	#10% of train set
test_set = []

#Seperate the dataset into testing and training
for i in xrange(test_set_size):
	index = randint(0,len(train_set)-1)
	test_set.append(train_set[index])
	try:
		train_set.pop(index)
	except:
		print index

#Extract all words from the dataset into one list
all_words = []
for item in train_set:
	ques = item['ques']
	item['ques'] = [ w for w in ques.lower().split() if len(w) >= 2] #ignore words with less than 2 characters
	all_words.extend(item['ques'])

freq_dist = nltk.FreqDist(all_words)
freq_dist = freq_dist.most_common(2000)
word_features = [n[0] for n in freq_dist]

junk_features = ["'s","''","``"] #remove those features we do not want
for j in junk_features:
	try:
		word_features.remove(j)
	except:
		print "remove err"

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = [(extract_features(item['ques']),item['label']) for item in train_set]
classifier = nltk.NaiveBayesClassifier.train(training_set)
test_set = [(extract_features(item['ques']),item['label']) for item in test_set]
print nltk.classify.accuracy(classifier, test_set)

#interactive shell to classify user questions. Press ctrl+C to exit 
while True:
	ques = raw_input("Enter the question: ")
	ques = ques.rstrip().replace("?","")  #remove trailing whitespace and question mark
	print classifier.classify(extract_features(ques.split()))

