import sys

#takes a word "word" and returns that word with the letter at
#the integer "index" capitalized
def capitalizeOneLetter(word, index):
    #all characters before the letter to be capitalized
    beforeCaps = word[0:index]
    #the letter to be capitalized, already capitalized using .upper()
    charToBeCapitalized = word[index].upper()
    #all characters after the letter to be capitalized
    afterCaps = word[(index+1):len(word)]
    return(beforeCaps + charToBeCapitalized + afterCaps)

#checks the word for four letters, and prints that word with
#eacj of those letters converted to numbers one at a time
def numberWordConversion(word):
    for i in range(len(word)):
        beforeCheck = word[0:i]
        charToCheck = word[i]
        afterCheck = word[(i+1):len(word)].strip()
        #converts each character to the number
        if charToCheck == "o":
            print(beforeCheck + "0" + afterCheck)
        elif charToCheck == "e":
            print(beforeCheck + "3" + afterCheck)
        elif charToCheck == "i":
            print(beforeCheck + "1" + afterCheck)
        elif charToCheck == "a":
            print(beforeCheck + "4" + afterCheck)

#gets each word in the input, and for each possible combination
#of one-letter-capitalized-all-others-lowercase, converts all
#possible number-characters to number one at a time
for word in sys.stdin:
    for i in range(len(word)):
        capsWord = capitalizeOneLetter(word, i)
        numberWordConversion(capsWord)
