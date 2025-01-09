experience = 0

sticks = 0
diamonds = 0

hasPickaxe = False
hasSword = False


while True:
  print("1 - get stick")
  print("2 - get pickaxe")
  print("3 - get sword")
  print("4 - kill Enderdragon")

  choise = input("Select option from menu: ")
  if choise == "1":
    sticks = sticks + 1
    experience += 20
  elif choise == "2":
    hasPickaxe = True
    experience += 70
  elif choise == "3":
    hasSword = True
    experience += 100
  else:
    if hasSword and experience >= 200:
      print("Congratulations you won !")
      exit
    else:
      print("Get sword first and gain 200 of exp !!!")

  print(f"\n\nYou have {experience} of exp")
