import random as rn

guess = 3
while True:
    num = int(input("Enter the number between 1 - 6 :"))
    randnum = rn.randint(1,7)
    if num == randnum:
        print("Good job you !!\nYou guessed correct")
        print("No.of guess took is ",3-guess)
        break
    elif num < randnum :
        guess -=1
        print(f"Ooops !!!\nWrong guess. Pls try again. You have {guess} chances left")
        
    if guess == 0:
        print("You ran out of chances. Betterluck next time")
        break