import random
n = random.randrange(1,10)
guess = int(input("Введіть будь-яке число від 1 до 10: "))
while n!= guess:
    if guess < n:
        print("Мало")
        guess = int(input("Введіть число знову: "))
    elif guess > n:
        print("Багато")
        guess = int(input("Введіть число знову: "))
    else:
      break
print("вгадав!")

