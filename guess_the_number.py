import random

random_num = random.randint(1,100);
guessing_count=0
guess=0
while (guess != random_num):
    guess = int(input("Enter your guess between 1 to 100 :"));
    if (random_num>guess):
        if(random_num-guess<=10):
            print("Your guess is slightly less than the number. Keep guessing")
        else:
            print("Your guess is too less than the target. Keep guessing!!")
    elif(random_num<guess):
        if(guess-random_num<=10):
            print("Your guess is slightly greater than the number. Keep guessing")
        else:
            print("Your guess is too greater than the target. Keep guessing!!")
    guessing_count+=1
        
print(f"Congratulations!!!\n You have guessed the right number in {guessing_count} attempts")

    

