import csv

reader = csv.reader(open("morseCode.csv", 'r'))
morseDict = {}
for row in reader:
    letter, morse = row
    morseDict[letter] = morse

def translate(text):
    text = text.upper()
    morseText = ""
    for i in range(len(text)):
        if text[i] != ' ':
            morseText += morseDict[text[i]]
            morseText += '/'
        else:
            # morseText += text[i]
            morseText += '/'
    return morseText

def decode(morse):
    letter = ""
    result = ""
    for i in range(len(morse)):
        if morse[i] != '/':
            letter += morse[i]
        else:
            for key, value in morseDict.items():
                if letter == value:
                    result += key
                    letter = ""
            if morse[i] + morse[i-1] == "//":
                result += ' '
    return result


inputLine = input("Input a text to translate it to Morse: ")
morseTranslation = translate(inputLine)
textTranslaton = decode(morseTranslation)

print(morseTranslation)
print(textTranslaton)






