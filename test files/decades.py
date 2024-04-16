import random

age = int(input("How old are you?\n"))
decades = age // 10
years = age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old")

if age > 30:
    print("you're old")
else:
    print("enjoy these years of your life")

roll = random.randint(1,6)
print (roll)
