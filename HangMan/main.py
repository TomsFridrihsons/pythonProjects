#TODO  1)Find a database with words
#TODO  2)Create functions for
#           input
#           randomly choosing the guessing word from dictionary
#           checking each letter (if in correct place or if it is in the word)
#           Displaying the game
#           Statistics
#           Check if input word exists in database. If it does not then the word does not exists and
#               let the player try again
#           Create "Next word" function
import random
import csv

def wordInput(wordLenght, allowedGuesses):
    guessedWord = ""
    print(f"Tev ir jāuzmin vārds ar {wordLenght} burtiem")
    inputWord = input(f"Tev ir palikuši {allowedGuesses} mēģinājumi: ")
    for letter in inputWord:
        if (letter.isalpha()) == True:
            guessedWord += letter

    guessedWord = guessedWord.lower()

    if wordLenght != len(guessedWord):
        print("Ievadītais vārds neatbilst mināmā vārda garumam.")
        print("Mēģini vēlreiz!")
        wordInput(wordLenght, allowedGuesses)
    else:
        return guessedWord

def getWordMain():
    rowCount = 0
    gameInfo = []
    DictionaryPath = "./latvianNounDict.csv"
    openReader = open(DictionaryPath, 'r', encoding="utf8")
    reader = csv.reader(openReader)
    allWords = list(reader)
    for row in allWords:
        rowCount+=1
    rowNumber = random.randint(0, rowCount-1)
    chosenWord = allWords[rowNumber][0]
    if len(chosenWord) >= 6:
        print("Pa garu")
        getWord()
    openReader.close()

    return chosenWord


def game():
    print()
    print("KARĀTAVAS")
    print("Izvēlne:")
    print("1 --> Sākt jaunu spēli")
    print("2 --> Apskatīt statistiku")
    print("3 --> Apskatīt noteikumus")
    print("4 --> Beigt spēli")
    choise = input()
    choise = int(choise)
    if choise >= 1 and choise <= 3:
        if choise == 1:
            while choise != 3:
                print("Sākam spēli!")
                full()
                game()
    else:
        print("Try again!")
        game()


def inputCheck(chosenWord, inputWord, guessCount):
    if guessCount == 6:
        correctLetters = 0
        correctGuess = []
    if chosenWord == inputWord:
        return "Guessed!"
    else:
        for letter in range(len(inputWord)):
            correctGuess.append("_")
            if chosenWord[letter] == inputWord[letter]:
                correctLetters += 1
                correctGuess[letter] = chosenWord[letter]
        print(f"Tu pareizi uzminēji {correctLetters} burtus")
        return correctGuess


def full():
    print()
    print()
    guessCount = 6
    gameCount = 0
    result = ""
    chosenWord = getWord()
    wordLenght = len(chosenWord)
    print(f"Vārda garums {wordLenght}")
    print(f"Mēģinājumu skaits {guessCount}")
    print()
    for game in range(guessCount):
        inputWord = wordInput(wordLenght, guessCount-game)
        print(inputWord)
        if inputWord is None:
            print("Notika kļūda. Mēģini vēlreiz!")
            inputWord = wordInput(wordLenght, guessCount - game)
        result = inputCheck(chosenWord, inputWord, guessCount)
        if type(result) is not list:
            print("Congrats you won!")
            break
        else:
            print(result)

    if type(result) is list:
        print("Tu neuzminēji doto vārdu!")
        print(f"Vārds, kas Tev bija jāuzmin: {chosenWord}")


def getWord():
    allWords = []
    rowCount = 0
    DictionaryPath = "./latvianNounDict.csv"
    openReader = open(DictionaryPath, 'r', encoding="utf8")
    reader = csv.reader(openReader)
    # rowCount = sum(1 for row in reader)
    for row in reader:
        # print(1)
        rowCount += 1
        word, definition = row
        allWords.append(word)
    # allWords = list(reader)
    wordNumber = random.randint(0, rowCount-1)
    chosenWord = allWords[wordNumber]
    print(chosenWord)
    openReader.close()
    return chosenWord


game()


