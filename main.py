import json
import difflib


data = json.load(open("data.json"))

def translate(w):
  w = w.lower()
  if w in data:
    return data[w]
  elif w.upper() in data: # for capitalized words like USA and Nato
    return data[w.upper()]
  elif w.title() in data: # for words that start with a capital letter
    return data[w.title()]

  close_words = difflib.get_close_matches(w, data, cutoff=0.7) # A list of a word's close matches, if any

  if len(close_words) > 0:
    yn = input("Did you mean: {}? Y/N: ".format(close_words[0]))

    if yn.lower() == "y":
      return data[close_words[0]]
    
  return "Word not found. Please check your spelling and try again."

word = ""
while word.lower() != "q":
  word = input("Please enter a word (or q to quit): ")
  
  if word != "q":
    meanings = translate(word)
    if type(meanings) == str:
      print(meanings)
    else:
      for meaning in meanings:
        print("\n" + meaning)