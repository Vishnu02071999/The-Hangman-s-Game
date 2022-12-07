import hangmanlogo
import hangmanlist
import random

# print(hangmanlogo.logo)
lives = 7
chosenword = random.choice(hangmanlist.words)
end_of_game = False
lives = 6
length=len(chosenword)
display = []
for _ in range(length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You've already guessed {guess}")
    for position in range(length):
        letter = chosenword[position]
        if letter == guess:
          display[position] = letter
    if guess not in display:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")
        
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("Congrats!! You won.")
    

    print(hangmanlogo.stages[lives])
print(f"The word was {chosenword}")