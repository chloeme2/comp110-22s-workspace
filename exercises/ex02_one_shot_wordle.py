"""Exercise 02"""

__author__ = "730403918"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
correct_guess: str = "knoll"
six_letter_guess: str = (input("What is your 6-letter guess? "))
i: int = 0
box: str = ""
green_boxes: str = GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX

while len(six_letter_guess) != len(correct_guess): 
    six_letter_guess: str = input("That was not six letters! Try again: ")

if six_letter_guess == correct_guess:
    print(f"{ green_boxes }\nWoo! You got it!")
else: 
    while i < len(six_letter_guess): 
        if six_letter_guess[i] == correct_guess[i]: 
            box = box + GREEN_BOX
            i += 1    
        else: 
            letter: bool = False
            s: int = 0
            while letter == False and s < len(six_letter_guess): 
                if six_letter_guess[i] == correct_guess[s]:
                    letter == True
                else:
                    s += 1 

                if(letter):
                    box = box + YELLOW_BOX 
                else: 
                    box = box + WHITE_BOX 
                i += 1
    print(f"{ box }\nNot quite. Play again soon!")