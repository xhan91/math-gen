import re
from collections import defaultdict
from functools import cmp_to_key
from random import random

text = "Alice was beginning to get very tired of sitting by her sister on the\n" \
    + "bank, and of having nothing to do: once or twice she had peeped into the\n" \
    + "book her sister was reading, but it had no pictures or conversations in\n" \
    + "it, 'and what is the use of a book,' thought Alice 'without pictures or\n" \
    + "conversations?'\n" \
    + "\n" \
    + "So she was considering in her own mind (as well as she could, for the\n" \
    + "hot day made her feel very sleepy and stupid), whether the pleasure\n" \
    + "of making a daisy-chain would be worth the trouble of getting up and\n" \
    + "picking the daisies, when suddenly a White Rabbit with pink eyes ran\n" \
    + "close by her.\n" \
    + "\n" \
    + "There was nothing so VERY remarkable in that; nor did Alice think it so\n" \
    + "VERY much out of the way to hear the Rabbit say to itself, 'Oh dear!\n" \
    + "Oh dear! I shall be late!' (when she thought it over afterwards, it\n" \
    + "occurred to her that she ought to have wondered at this, but at the time\n" \
    + "it all seemed quite natural); but when the Rabbit actually TOOK A WATCH\n" \
    + "OUT OF ITS WAISTCOAT-POCKET, and looked at it, and then hurried on,\n" \
    + "Alice started to her feet, for it flashed across her mind that she had\n" \
    + "never before seen a rabbit with either a waistcoat-pocket, or a watch\n" \
    + "to take out of it, and burning with curiosity, she ran across the field\n" \
    + "after it, and fortunately was just in time to see it pop down a large\n" \
    + "rabbit-hole under the hedge.\n"

def getWords(s):
    delimiter = r'\W'
    return list(filter(lambda x : x != '' , re.split(delimiter, s.lower())))

# print(getWords(text))

def analyze(words):
    def int_default():
        return defaultdict(int)
    d = defaultdict(int_default)
    for w1, w2 in zip(words, words[1:]):
        d[w1][w2] += 1
    if words[-1] not in d:
        d[words[-1]] = int_default()
    return d

# print(analyze(getWords("the dog ate the cat")))

# d { word : { word : count } }
def processD(d):
    def compare(a, b):
        if a[1] != b[1]:
            return a[1] - b[1]
        else:
            return 1 if b[0] > a[0] else -1

    newD = {}
    for k, v in d.items():
        l = [[w, c] for w, c in v.items()]
        l.sort(key=cmp_to_key(compare), reverse=True)
        t = 0
        for i in range(len(l)):
            t += l[i][1]
            l[i][1] = t
        newD[k] = l
    return newD

# d { word : [(word, count), ... ]} large > 
def getNextWord(word, num, d):
    if word not in d or not d[word]:
        return None
    num = num * d[word][-1][1]
    for w, c in d[word]:
        if num < c:
            return w


def writeASentence(word, d):
    result = []
    while word:
        result.append(word)
        word = getNextWord(word, random(), d)
    return ' '.join(result)

d = analyze(getWords(text))
# print(d)
newD = processD(d)
# print(newD)
print(writeASentence('alice', newD))