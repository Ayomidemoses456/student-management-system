secret_number = 5

number = 0
while number < 4:
    print("true")
    number += 1 #is the same with number = number+ 1
    guess_number = int(input("Guess a number. "))
    if guess_number == secret_number:
        print("You won the game")
        print("Thanks for playing the game")
        break
    elif guess_number < secret_number:
        print("guess is lower. Try again") 
    elif guess_number > secret_number:
        print("guess is higher. Try again")         
    else:
        print("invalid data")
else:       
    print("You have exhausted your trial")








































# age = "five"
# name2 = "ayomide"

# print(type(age))
# print(type(__name__))






