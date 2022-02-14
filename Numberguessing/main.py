import random
import math

# selecting range
minimum = int(input("Enter the lower range: "))
maximum = int(input("Enter the upper range: "))

# generating the number
x = random.randint(minimum, maximum)
half = maximum / 2
factor = x * 3

count = 0
attempts = math.log(maximum - minimum + 1, 2)


while count < attempts:
    count += 1
    guess: int = int(input("Enter your guess: "))
    if x == guess:
        print("Congratulations your score is ",
              int(count/attempts),)
        break
    elif x > guess:
        print("your guess is too low")
    elif x < guess:
        print("your guess is too high")
if count >= 7:
    print("Game Over.The number is %d " % x)
    print("Better luck next time.")
