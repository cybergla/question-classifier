# Question Classifier

The task was to classify a question into four possible types

1. Who
2. What 
3. When
4. Affirmative

Any other type of question would be labelled "Unknown". 

I decided to approach the problem as that of classification, with the question types as labels. I decided to use a Naïve Bayes Classifier to build the model because of its popularity in text mining.

# How to run
Execute `python train.py`

## Dependencies
1. Python >= 2.7
2. nltk

# The Dataset

The first challenge was to find a suitable dataset. The dataset linked to in the assignment instructions was that of the Cognitive Computation Group at UIUC. It was an excellent dataset with over 1000 labelled questions. However the class labels were different from the ones I needed. They were more detailed and were divided into multiple subcategories. Also the final category of questions `Affirmative` was not present at all.

So my first task was to map these labels to the 4 categories I needed. I manually decided on a mapping based on my intuition and understanding. 

For the `Affirmative` type of questions, I looked elsewhere on the internet and found a set of 155 ["choice questions"](http://www.home-speech-home.com/yes-or-no-questions.html). I interpreted the `Affirmative` type as a type of question with either a yes or no answer. I loaded those questions into the dataset with the others.

# Preprocessing

`process.py` is the preprocessing module where I mapped my own class labels over the CogComp ones and merged the choice question dataset. I saved the dataset as a pickle to disk.

# Training

The `train.py` module performs the actual training of the model. I chose 10% of the training dataset as the test dataset. 

The first task was to determine which features would be relevant to the model. I decided to extract the features from the question based on whether certain words were present or not. I created a list of all the words in the training dataset and made a frequency distribution of words from it, using nltk's `FreqDist()`. I chose the top 2000 common words as the list of features. I was careful to remove words less than 2 characters longs and also words which did not have much relevance such as `` ` ` `` or  ` " ` but weren't very common. After this I had a list of words which would serve as the feature list.


I then wrote an `extract_features()` function which would return a list of which features the question contained in the format of `contains(<word>): True/False`. I created a list of tuples containing the extracted features and their labels. I fed this as the training set into the `nltk.NaiveBayesClassifier`. The test set was also created similarly and I used `nltk.classify.accuracy()` function to find out the accuracy of the model.

# Testing

To properly test whether the model was useful or not I had to create a benchmark. In `naive.py` I developed a naive method of classifying such questions. 

1. A question containing `who`, `what`, `when` would be classified accordingly.
2. A question containing `"are","is","do","can","does"` were classified as `Affirmation`
3. Rest were classified as `Unknown`.

This is obviously not a very good method  of classifying, but it at least gave me a good way to measure how effective my model was against a naive method. 

# Results

When I ran the testing set using the naive model, I got an accuracy of around 50%. When I used the Bayes Classified Model, I got an accuracy of around 60-65%, depending on the training set.

It was a very modest improvement, but I'm confident that given more time to analyse the dataset and extract more relevant features, I can achieve better results. 

One problem I encountered was that "What" type of questions overpopulated the training dataset. They skewed the training considerably.

I could also have tried another type of classifier, such as a Decision Tree or a Multinomial Bayes Classifier which takes into account the number of occurences of a word.

