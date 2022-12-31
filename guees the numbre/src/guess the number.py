from random import randint
guess = randint (0 , 100)

print("")
while True:
    player = int(input ("guess the number from 0, 100 : "))
    
    if (player == guess):
     print("you win")
     break
    
    elif(player > guess):
     print ("your guess is bigger")
    elif(player < guess):
       print("your guess is smaller")
