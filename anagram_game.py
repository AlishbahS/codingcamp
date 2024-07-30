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

def choose_word_or_phrase(category):
    """The function will choose a random element from the selected category"""
    elements=list(dict[category].keys())
    # The key() shows all the elements in a specific category
    # To access an element of dict we use square brackets
    random_element=random.choice(elements)
    return random_element

random_element=choose_word_or_phrase(category)
shuffled = shuffle(random_element)

attempts=3
while attempts!=0:
      print("the word is",shuffled)

guess="enter your guess:  ".lower().strip()
    
    if guess == random_element:
        print("Congratulations! You guessed it right.")
        break

    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong guess. You have {attempts} attempts left.")
        else:
            print(f"Sorry, you're out of attempts. The correct answer was '{random_element}'.")






  
