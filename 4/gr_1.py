import random

hp = 100
money = 1000

print("1 - gun")
print("2 - flashbang")
print("3 - sniper riffle")

option1 = input("Pick weapon: ")

if option1 == "1":
  money -= 300
elif option1 == "2":
  money -= 150
else:
  money -= 400


print("1 - headshot")
print("2 - bodyshot")
print("3 - legshot")

option2 = input("Option: ")


if option2 == "1":
  hp = hp - 70 - random.randint(0, 30)
elif option2 == "2":
  hp = hp - 45
else:
  hp = hp - 25

print(hp)
