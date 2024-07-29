import random

# Creating a dictionary with words and phrases
dict = {
    "words": {
        "strawberry": "a fruit",
        "butterfly": "an insect",
        "milkshake": "a beverage",
        "leopard": "an animal",
        "jacket": "a piece of clothing",
    },
    "phrases": {
        "break a leg": "good luck",
        "spill the beans": "disclose information",
        "piece of cake": "something very easy",
        "under the weather": "feeling ill",
        "call it a day": "stop working",    
    }
}

#Get a category(words/phrases) as input from user
category= input("Enter a category(words/phrases) :").strip().lower()
if category in dict:
   print(f"Category selected: {category}") 
else:
   print("Invalid category. Please enter 'words' or 'phrases'.")

def choose_word_or_phrase(category)
"""The function will choose a random element from the selected category"""
elements=list(dict[category].keys())
# The key() shows all the elements in a specific category
# To access an element of dict we use square brackets
random_element=random.choice(elements)
return random_element

def shuffle(random_element)
letters=list(random_element)
random.shuffle(letters)
shuffled=''.join(letters)
#join() converts list back to string
return shuffled






  
