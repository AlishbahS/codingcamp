import random

# Define the dictionary with words and phrases
data = {
    "words": {
        "apple": "a fruit",
        "banana": "another fruit",
        "car": "a vehicle",
        "dog": "an animal"
    },
    "phrases": {
        "break a leg": "good luck",
        "hit the sack": "go to sleep",
        "piece of cake": "something very easy"
    }
}


# Get the category from the user
category = input("Select a category (words/phrases): ").strip().lower()
print(f"Category selected: {category}")  # Debug print

if category in data:
    print(f"Playing with category: {category}")

    while True:
        items = list(data[category].keys())
        original = random.choice(items)
        shuffled = ''.join(random.sample(original, len(original)))
        hint = data[category][original]

        print(f"\nSolve: {shuffled}")
        print(f"Hint: {hint}")

        correct = False
        for attempt in range(3):
            guess = input(f"Attempt {attempt + 1}/3: ").strip().lower()
            print(f"User guessed: {guess}")  # Debug print
            if guess == original:
                print("Correct!")
                correct = True
                break
            else:
                print("Incorrect.")
        
        if not correct:
            print(f"Out of attempts! The correct answer was: {original}")

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        print(f"Play again: {play_again}")  # Debug print
        if play_again != 'y':
            print("Thank you for playing!")
            break
else:
    print("Invalid category.")
