import random

# Creating a dictionary with words and phrases
dict = {
    "words": {
        "strawberry": "a fruit",
        "butterfly": "an insect",
        "coffee": "a beverage",
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

def main():
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

    def shuffle(random_element):
        letters=list(random_element)
        random.shuffle(letters)
        shuffled=''.join(letters)
        #join() converts list back to string
        return shuffled


    #storing return value into variable
    random_element=choose_word_or_phrase(category)
    shuffled=shuffle(random_element)

    print(f"\nSolve: {shuffled}")
    hint=dict[category][random_element]
    print(f"Hint: {hint}")
    print("\nYou will get 3 attempts")

    #to check if guess is correct or incorrect
    for attempt in range(1,4):
        guess=input("\nEnter your guess: ").strip().lower()   
        if guess==random_element:
            print("Welldone!You guessed correct.")
            restart_()
            break
        else:
            print ("You guessed wrong!")
            attempt_left= 3-attempt

    #to check the number of attempts left
        if attempt_left>0:
            print (f"You have {attempt_left} attempts left")
        else:
            print (f"Out of attempts! The correct answer was {random_element}.")
            restart_()

#restart the solver
def restart_():
    restart= input("Do you want to play (yes/no): ").strip().lower()
    if restart=="no":
        print("Thanks for playing")
    elif restart=="yes":
        main()
    else:
        print("Invalid answer")
        print(restart)
restart_()        



    



  





  
