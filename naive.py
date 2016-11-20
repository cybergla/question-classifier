def classify(ques):
	ques = ques.lower()
	labels = ["Who","What","When"]
	for l in labels:
		if ques.find(l.lower()) >= 0:
			return l
	choice = ["are","is","do","can","does"]
	for c in choice:
		if ques.find(c) >= 0:
			return "Affirmation"
	return "Unknown"

def find_accuracy(test_set):
	count = 0
	for sample in test_set:
		print sample['ques'], classify(sample['ques']), sample['label']
		if classify(sample['ques']) == sample['label']:
			count = count+1
	return float(count)/len(test_set)