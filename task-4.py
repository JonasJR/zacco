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
#modified to only return unique words
def countAndSortDuplicateWords(words):
    counted = Counter(words)
    order = sorted(counted.items(), key=itemgetter(1))
    for o in order:
        if o[1] is 1:
            print o[0]

#Method that loops through the list of words and then removes all special chars
#and removes the whole entry if there is nothing left
def removeSpecialChars(words):
    newList = []
    for word in words:
        newWord = ''.join(e for e in word if e.isalnum())
        if newWord:
            newList.append(newWord.lower())
    return newList

words = removeSpecialChars(words)
countAndSortDuplicateWords(words)
