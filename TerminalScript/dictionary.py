import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def get_word(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        answer = input("Did you mean %s ? Yes or No ?: " % get_close_matches(word, data.keys())[0]).lower()
        if answer == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif answer == "no":
            return "Please try another word"
        else:
            return "Wrong entry"
    else:
        return "Cannot find word"


word = input("Type a word: ")
output = get_word(word)
if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)
