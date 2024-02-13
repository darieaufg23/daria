from random import randint

s = randint(1,10)
guess = int(input("number"))
count=0
while s != guess:
    print(f"Der Wert war leider nicht {guess}")
    if guess > s:
        print("Zu groß")
    elif guess < s:
        print("Zu klein")
    guess= int(input("neue Zachl: "))
    count = count+1
print(f"Super")
print(count)