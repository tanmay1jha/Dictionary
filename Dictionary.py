import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def dict(w):
    if w in data:
        return data[w]
    elif w.lower() in data:
        return data[w.lower()]
    elif w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w,data.keys(),cutoff = 0.8)) > 0:
        print(f"Did you mean {get_close_matches(w,data.keys(),cutoff = 0.8)[0]}")
        yn = input("Y for Yes and N for No ")
        if yn.lower() == "y":
            return data[get_close_matches(w,data.keys(),cutoff = 0.8)[0]]
        elif yn.lower() == "n":
            return "Word not found in dictionary"
        else: 
            return "We didn't understand your query"
    else:
        return "Word not found in dictionary"


while True:
    print('To exit type "exit"')
    word = input("Enter word to search: ")
    if word == "exit":
        ex = input(("Do you want to exit (y) or want to search the word (press any key)  "))
        if ex.lower() == "y":
            break
        else:
            output = dict(word)
            if type(output) == list:
                for item in output:
                    print(f"   {item}")
            else:
                print(output)
    else:
        output = dict(word)
        if type(output) == list:
            for item in output:
                print(f"   {item}")
        else:
            print(output)