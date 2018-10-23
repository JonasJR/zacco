from collections import Counter

sentence = raw_input("Please enter a sentence: ").split()
sentence = Counter(sentence)
sentence = sorted(sentence.items())
for item in sentence:
    print item
