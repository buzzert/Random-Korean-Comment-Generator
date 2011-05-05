#!/usr/bin/python

import random

# Returns a random syllable by mashing up some Hangul
# unicode characters!
def getRandomSyllable():
    # These are ranges of Jamo characters called Hangul
    # compatibility Jamo
    # Source: http://bit.ly/dzMEIY
    leadConsonantRange = (0x1100, 0x1112)
    vowelRange = (0x1161, 0x1175)
    tailConsonantRange = (0x11A8, 0x11C2)
    
    # Generate a random lead consonant, and a vowel
    leadConsonant = unichr(random.randrange(leadConsonantRange[0], leadConsonantRange[1]))
    vowel = unichr(random.randrange(vowelRange[0], vowelRange[1]))
    
    # ... and sometimes a tail character
    tailExcl = random.randrange(0, 2)
    if (tailExcl == 0):
        tailConsonant = unichr(random.randrange(tailConsonantRange[0], tailConsonantRange[1]))
    else:
        tailConsonant = ''
    
    return leadConsonant + vowel + tailConsonant
    
# Returns a random puncuation mark
def getRandomPunctuation():
    punct = ['.', '!']
    
    return punct[random.randrange(0, len(punct))]

# Returns a random korean sentence of specified word length
def getRandomSentence(wordLength):
    sentence = ""
    
    for i in range(0, wordLength):
        randWordLen = random.randrange(1, 6)
        for w in range(0, randWordLen):
            sentence += getRandomSyllable()
        sentence += " "
        
    return sentence[:-1] + getRandomPunctuation()

# English equivalent of "LOL!"
def kekekeke():
    return "" + unichr(0x110F) * random.randrange(3,10)

# Get a random series of sentences of specified sentence count
def getRandomComment(numSentences):
    comment = ""
    
    for i in range(0, numSentences):
        randSentenceLen = random.randrange(2,7)
        comment += getRandomSentence(randSentenceLen) + " "
    
    return comment + kekekeke()
    
    
if __name__ == "__main__":
    print getRandomComment(2)