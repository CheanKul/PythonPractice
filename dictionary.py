import json
from difflib import get_close_matches


def loadJsonData(filename):
    return json.load(open(filename))


def acceptInput(file):
    inputWord = input("\nEnter Your Word For Searching : - ")
    jsonData = loadJsonData(file)
    if inputWord.lower() in jsonData:
        return jsonData[inputWord.lower()]
    else:
        matched = get_close_matches(inputWord.lower(), jsonData.keys())[0]
        newInput = input("\nDid You Mean \'" + matched
                         + "\' ... Enter Y To Search For That Or Press N For NO?   :-|  ")
        return jsonData[matched] if newInput.lower() == 'y' else "Cannot Find Translation Of Your Word ...:-("


def displayResult(file):
    [print("\nOutput : - " + i) for i in acceptInput(file)]


displayResult("076 data.json")
