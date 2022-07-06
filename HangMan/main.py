#TODO  1)Find a database with words
#TODO  2)Create functions for
#           input
#           randomly choosing the guessing word from dictionary
#           checking each letter (if in correct place or if it is in the word)
#           Displaying the game
#           Statistics
import random
import csv
import pandas as pd


def wordInput(wordLenght, allowedGuesses):
    guessedWord = ""
    inputWord = input(f"Tev ir palikuši {allowedGuesses} mēģinājumi: ")
    for letter in guessedWord:
        if (letter.isalpha()) == True:
            guessedWord += letter

    guessedWord = guessedWord.lower()

    if wordLenght != len(guessedWord):
        print("Ievadītais vārds neatbilst mināmā vārda garumam.")
        print("Mēģini vēlreiz!")
        return wordInput(wordLenght,allowedGuesses)
    else:
        return guessedWord

def getWord():
    nounDictionaryPath = "HangMan/latvianNounDict.csv"
    DictionaryPath = "HangMan/latvianDict.csv"
    openReader = open(DictionaryPath, 'r', encoding="utf8")
    openWriter = open(nounDictionaryPath, 'w', encoding="utf8")
    # openReader = open(nounDictionaryPath, 'r', encoding="utf8")
    reader = csv.reader(openReader)
    writer = csv.writer(openWriter)
    allWords = list(reader)
    for row in reader:
        word, definition = row
        if "lietv" in definition and definition[-1] != 'i':
            writer.writerow(row)
    rowCount = sum(1 for row in reader)
    rowNumber = random.randint(0, rowCount)
    # print(rowNumber)
    # chosenWord = allWords[rowNumber][0]
    openReader.close()
    # openWriter.close()
    return rowCount



# def getWord():
#     rowCount = 0
#     DictionaryPath = "HangMan/latvianNounDict.csv"
#     reader = csv.reader(open(DictionaryPath, 'r', encoding="utf8"))
#     allWords = list(reader)
#     for row in allWords:
#         rowCount+=1
#     # rowCount = sum(1 for row in reader)
#     rowNumber = random.randint(0, rowCount)
#     print(rowNumber)
#     # chosenWord = allWords[rowNumber-1][0]
#     chosenWord = allWords[2]
#     print(chosenWord)
#     return rowCount


# print(getWord())






