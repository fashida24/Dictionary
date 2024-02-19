import json
from difflib import get_close_matches

data = json.load(open("data.json")) #This opens the data.json file

def definition(word):
    
    word = word.lower() #This makes the word case insensitive
    if word in data: 
      return data[word] #this gets the definition of the word from the data.json file
    elif len(get_close_matches(word, data.keys()))>0:
       question= input("Did you mean %s instead  y or n " % get_close_matches(word, data.keys())[0])    #This returns a similar word. A .format method can work for this
       question= question.lower() #This makes the question to be case insensitive
       if question == "y" :
          return data[get_close_matches(word, data.keys())[0]]
       elif question == "n" :
          print("please check yor word agin!!")
       else:
          print("pick y or n")
    elif word.title(): #This makes nouns to be accessible
       return data[word.title()]
    elif word.upper: #This is for words that have acronyms
       return data[word.upper()]
    
          
    else:
       print("This word doesn't exist! Crosscheck it!")
word=input("Please enter a word: ") #This asks the user for a word
# Originally the words will come out in form of a list.. so we have toshow the word without the [] list
output=definition(word) #This prints the definition of the word
if type(output) == list:
   for item in output:
      print (item)
else: #This is for when it is a string
   print (output)

