import pickle

TRAIN_FILE = 'train_1000.label'
MAPPINGS_FILE = 'mappings'

#Load the training set from file
train_set = []
with open(TRAIN_FILE,'r') as file:
	for line in file:
		label, ques = line.rstrip().split(" ",1)
		train_set.append({'label':label,'ques':ques})

#Load the mappings from the file
mappings = []
with open(MAPPINGS_FILE,'r') as file:
	for line in file:
		label,new_label = line.rstrip().split("\t")
		mappings.append([label,new_label])

#Map the custom labels to the old ones
for item in train_set:
	for m in mappings:
		if item['label'] == m[0]:
			item['label'] = m[1]

#Choice ques load
with open("choice_ques.txt",'r') as file:
	for line in file:
		train_set.append({'label':'Affirmation','ques':line.rstrip()})

#Save the dataset as pickle file
with open("train_set.pkl",'w') as file:
	pickle.dump(train_set,file)