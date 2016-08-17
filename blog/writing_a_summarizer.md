---
title: Writing a Summarizer
subtitle: An exercise with weights.
date: Wednesday August 17, 2016
---

Writing a summarizer is a task that can have varying levels of difficulty,
depending on what technique is employed and how compressed the desired text should be.

For the summarizer proof of concept notebook I posted on GitHub, the technique
used to determine the importance of a sentence is very simple. Sentences have
scores calculated based on their apparent importance though using a metric
called TFIDF and then scores of sentences are tabulated by summing and
normalizing the scores of words in a sentence.

## Problem

One of the main issues one can encounter when trying to write an automatic
summarizer is the bias of subjectivity in summarization. Each person may consider
different parts of a text more or less important and thus worthy of including in
a summarized text. This subjectivity is increased even more so when an
algorithm is devised to attempt to determine the importance of a sentence. The
only way to reduce bias in an algorithm would be to take an extremely large
data set and train/test the algorithm on this large corpus to ensure that
results perform well for ALL sorts of documents, rather than documents of
a certain type. Through having a large enough cross-validation set, bias can be
reduced significantly, though maybe not a point where the summarizer can be
considered completely generalized.

## Learning

Since this was just a proof of concept, the standard TFIDF implementation was
taken from scikit-learn. If you do not know what this is, it is one of, if not
the most popular library with a collection of machine learning algorithms coded
in Python. It is an industry standard. Back to the process, I used a training
data set from 20 newsgroups as this is a very diverse set of documents (rather
emnail chains) that would surely provide a good spread of words to calculate
appropriate weightings for words. Scikit-learn took care of handling
tokenization and calcuating the weightings with the `TfidfTransformer` module.

##TFIDF

TFIDF stands for term frequency inverse document frequency. A words "score" is
calculated by looking at it's relative frequency in a corpus (a set of
documents) and the number of times it occurs in a document. The gist of the
algorithm is that words that are common in a corpus have lower weightings than
words which are frequent in a document. For example, the word "the" appears
a lot in any set of documents you may pick. On the other hand, words such as
"backpropagation"  might not be very common if a random set of documents were
chosen, though if we look at a particular document talking about neural
networks, this term might be mentioned relatively frequently.


## Testing

Once scores were calculated, the test data (some excerpt from an astronomy
textbook) was placed in an external file  and read into the program. From here,
sentences were separated on punctuation and each sentence was scored by taking
the normalized sum of the scores for the words in the sentence. Finally,
sentences with scores above a threshold were extracted and this was taken to be
the summarized text.

## Future Improvements

The summarizer created produced relatively compressed results, with a ratio
hovering around 30% of the original text size. Although this seems like a lot
of compression, it is most likely not enough and many improvements can be had
by changing the methodology from just simply summing and normalizing scores.
One potential path one can take to build a better summarizer would be to
implement a large CNN and attempt to have the neural network learn about what
terms may be important. The issue with this is obviously that the neural
network will only be looking at individual words rather than sequences of
words. Another issue that this solution would impose would be the fact that
some sort of text would have to already be summarized in order to provide the
training data.
