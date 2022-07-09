#TODO  1)Find a database with words: DONE
#TODO  2)Create functions for
#           input: DONE
#           randomly choosing the guessing word from dictionary: DONE
#           checking each letter (if in correct place or if it is in the word and how many times): DONE
#           Displaying the game: DONE
#           Statistics
#           Check if input word exists in database. If it does not then the word does not exists and
#               let the player try again
#           Create "Next word" function
#           Make it object oriented
import random
import csv

def menu():
    print()
    print("KARĀTAVAS")
    print("Izvēlne:")
    print("1 --> Sākt jaunu spēli")
    print("2 --> Apskatīt statistiku")
    print("3 --> Apskatīt noteikumus")
    print("4 --> Beigt spēli")
    choice = input()
    try:
        choice = int(choice)
    except ValueError:
        choice = "n"

    if type(choice) == int:
        choice = int(choice)
        if choice >= 1 and choice <= 3:
            if choice == 1:
                print("Sākam spēli!")
                game()
            if choice == 3:
                print("Beigt sēli!")
                return 0
                # game()
        else:
            print("Try again!")
            menu()


def gameSetup():
    correctLetters = 0
    correctGuess = []
    guessCount = 6
    gameCount = 0
    chosenWord = getWord()
    wordLenght = len(chosenWord)

    for letter in range(len(chosenWord)):
        correctGuess.append("_")

    gameSetup = [correctLetters, correctGuess, chosenWord, guessCount, gameCount, wordLenght]
    return gameSetup


def letterInput():
    userInput = input(f"Ievadi burtu: ")
    inputLetter = userInput[0]
    if (inputLetter.isalpha()) == True:
        inputLetter = inputLetter.lower()
        return inputLetter
    else:
        print("Ievadītais simbols nav burts.")
        print("Mēģini vēlreiz!")
        return False


def gameCheck(gameSetup, inputLetter):
    currentTry = 0
    unguessedLetters = 0
    timesInWord = 0
    knownLetter = False
    if inputLetter in gameSetup[1]:
        knownLetter = True
    for letter in range(len(gameSetup[1])):
        if knownLetter == True:
            print("Šis burts jau ir atminēts!")
            break
        if gameSetup[1][letter] == "_":
            if gameSetup[2][letter] == inputLetter:
                currentTry = 1
                gameSetup[0] += 1
                gameSetup[1][letter] = gameSetup[2][letter]
                timesInWord += 1

    if currentTry == 0 and knownLetter == False:
        gameSetup[3] -= 1
        print(f"Šis burts nav vārdā, kas ir jāatmin.")
    else:
        print(f"Šis burts vārdā atrodas {timesInWord} reizes")

    print(f"Tu pareizi esi uzminējis {gameSetup[0]} no {gameSetup[5]} burtiem.")
    print(f"Uzminētie burti: {gameSetup[1]}.")
    print(f"Atlikušo mēģinājumu skaits: {gameSetup[3]}.")

    if '_' in gameSetup[1]:
        return False
    else:
        return True


def game():

    result = True
    gameInfo = gameSetup()
    print()
    print()
    print(f"Vārda garums: {gameInfo[5]}")
    print(f"Mēģinājumu skaits: {gameInfo[3]}")
    print()
    for tryNr in range(gameInfo[3]):
        inputLetter = False
        while type(inputLetter) == bool or inputLetter is None:
            if inputLetter is None:
                print("Notika kļūda. Mēģini vēlreiz!")
            inputLetter = letterInput()
        print(inputLetter)
        result = gameCheck(gameInfo, inputLetter)
        if result == True:
            print("Congrats you won!")
            break

    if result == False:
        print("Tu neuzminēji doto vārdu!")
        print(f"Vārds, kas Tev bija jāuzmin: {gameInfo[2]}")


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
    openReader.close()
    return chosenWord


menu()


