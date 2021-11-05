import random
our_number = random.randint(1,100)
while True:
    guess = int(input("Write an integer: "))
    if guess < our_number:
        print("«increase your number»")
    elif guess > our_number:
        print("«decrease your number»")
    else:
        print("Yes, it is correct! Our number is",our_number)
        break
