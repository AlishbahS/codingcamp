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
        "spill the tea": "disclose information",
        "piece of cake": "something very easy",
        "under the weather": "feeling ill",
        "call it a day": "stop working",    
    }
}

# Chooses random word or phrase from selected category
def choose_word_or_phrase(category):
    """The function will choose a random element from the selected category"""
    elements = list(dict[category].keys())
    random_element = random.choice(elements)
    return random_element

# Shuffles the random element
def shuffle(random_element):
    shuffled_list = []
    words = random_element.split()
    for word in words:
        letters = list(word)
        random.shuffle(letters)
        shuffled_word = ''.join(letters)
        shuffled_list.append(shuffled_word)
    shuffled = ' '.join(shuffled_list)
    return shuffled

# Asks the user for a hint
def hint_(hint):
    ask_hint = input("\nDo you want a hint? (yes/no): ").strip().lower()
    if ask_hint == "yes":
        print(f"Hint: {hint}")
        return True
    elif ask_hint == "no":
        return False
    else:
        return hint_(hint)

#  Restarts the solver
def restart_():
    restart = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if restart == "no":
        print("Thanks for playing")
    elif restart == "yes":
        main()
    else:
        print("Invalid answer")
        restart_()

# Starts a new round
def main():
    """This is the main game loop"""
    while True:
        category = input("Enter a category (words/phrases): ").strip().lower()

        # Checks if user has entered valid category
        if category in dict:
            print(f"Category selected: {category}")
            
            random_element = choose_word_or_phrase(category)
            shuffled = shuffle(random_element)
            hint = dict[category][random_element]
            
            print(f"\nSolve: {shuffled}")
            print("\nYou will get 3 attempts")
            
            hint_taken = False  # Initializing the hint_taken flag 
            
            for attempt in range(1, 4):
                guess = input("\nEnter your guess: ").strip().lower()
                
                # Checks if user has made correct guess
                if guess == random_element:
                    print("Well done! You guessed correctly.")
                    restart_()
                    return
                else:
                    print("You guessed wrong!")
                    attempt_left = 3 - attempt
                    
                    # Checks the number of attempts left
                    if attempt_left > 0:
                        print(f"You have {attempt_left} attempts left")
                        if not hint_taken:
                            hint_taken = hint_(hint)
                    else:
                        print(f"Out of attempts! The correct answer was {random_element}.")
                        restart_()
                        return
        else:
            print("Invalid category")

# Starts the solver      
main()


    

                    
    
    



  





  
