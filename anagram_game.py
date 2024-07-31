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

def choose_word_or_phrase(category):
    """The function will choose a random element from the selected category"""
    elements=list(dict[category].keys())# The key() shows all the elements in a specific category
    # If the category is words it will store all the keys of words in a list
    # To access an element of dict we use square brackets
    random_element=random.choice(elements)# random.choice will choose a random key from the list elements 
    return random_element #This function gives the value for random_element

def shuffle(random_element):
    shuffled_list=[]#Creating an empty list
    words=random_element.split()#the split function converts string to list and this list is called words
    # Here it seperates all the words of random_element
    for word in words:  #variable word iterates over each element in list words  
        letters=list(word) #Each of these element is converted into list.
        # Here the letters of each word is converted to list
        random.shuffle(letters)#random.shuffle shuffles the letters of the word
        shuffled_word=''.join(letters)#join converts list to string
        #Here join converts the list of shuffled letters to a single shuffled word
        shuffled_list.append(shuffled_word)#append adds elements to a list, keeping them seperate
        # Here append adds all the shuffled words to the empty list.
    shuffled=' '.join(shuffled_list)
        #After the loop ends join function converts shuffled list back to string
        #join places a space between each element of list
    return shuffled #This function gives the value for shuffled(phrase/word)

def main():
    """This is the main game loop"""
    while True:#This loop executes infinitely, unless we exit the function

    
#Get a category(words/phrases) as input from user
        category= input("Enter a category(words/phrases) :").strip().lower()
        if category in dict: #category refers to the two outer keys in dict
            print(f"Category selected: {category}") #if the category is in the dict it will print this
            
            #Calling the functions defined above
            random_element=choose_word_or_phrase(category)
            shuffled=shuffle(random_element)

            print(f"\nSolve: {shuffled}")#\n starts from new line
            hint=dict[category][random_element]# the value of key is the hint
            print(f"Hint: {hint}")
            print("\nYou will get 3 attempts")


            #to check if guess is correct or incorrect
            for attempt in range(1,4): #executes 3 times
                guess=input("\nEnter your guess: ").strip().lower() #prompts the user to enter a guess  
                if guess==random_element:
                    print("Welldone!You guessed correct.")
                    restart_() #goes to restart function
                    return #exits this round and starts a fresh one
                else:
                    print ("You guessed wrong!")
                    attempt_left= 3-attempt #executes each time the user guesses wrong

            #to check the number of attempts left
                if attempt_left>0:
                    print (f"You have {attempt_left} attempts left")
                else:
                    print (f"Out of attempts! The correct answer was {random_element}.")
                    restart_() #when the attempts are 0 the program goes to restart function
                    return #exits the function
        else:
            print("Invalid category")
            #if the user types invalid category ,as while true executes infinitely,
            #the program will go back to the start and prompt the user to enter the category again.
            

#Restarts the solver
def restart_():
    restart= input("Do you want to play again? (yes/no): ").strip().lower()
    if restart=="no":
        print("Thanks for playing")
    elif restart=="yes":
        main() #starts a fresh round
    else:
        print("Invalid answer")
        restart_() #prompts the user to enter valid input again

#Starts the solver      
main()
   

    



  





  
