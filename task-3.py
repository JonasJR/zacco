from collections import Counter
from operator import itemgetter

#Starts with reading the file and deviding it up into a list of sorted words
words = []
with open("words-test-UTF8.txt") as f:
    for line in f:
        for word in line.split():
            words.append(word)
words.sort()

#Method that counts the occurances of a word, places it in a dictionary and
#then prints out the words in the list in the correct order
def countAndSortDuplicateWords(words):
    counted = Counter(words)
    order = sorted(counted.items(), key=itemgetter(1))
    for o in order:
        current = o[0]
        for word in words:
            if word == current:
                print word

countAndSortDuplicateWords(words)
