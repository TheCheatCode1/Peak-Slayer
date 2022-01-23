name = ""
level =  5
breathingStyle = ""
health =  level * 5 + 500
attack = 5 * level - 3

def setName():
  global name
  name = input("What would you liked to be called? ")
  verify_name = ""

  while (verify_name.lower() != "yes"):
    verify_name = input("Ah so your name is : " + (name) + "? : ")
    if verify_name.lower() == "yes":
      print("Great\n")
    elif verify_name.lower() == "no":
      name = input("What would you liked to be called?")
    else:
      print ("Please type yes or no")

def setBreathingStyle():
  global breathingStyle
  print("Breathing Styles:\n"
      + "--------------------\n"
      + "Flame Breathing : A \n"
      + "Water Breathing : B \n"
      + "Thunder Breathing : C \n"
      + "Wind Breathing : D \n"
      + "Stone Breathing : E \n")

  breaths_choice = (input("Choose Breathing style : "))
  while (breaths_choice != "A" and breaths_choice != "B" and breaths_choice != "C" and breaths_choice != "D" and breaths_choice != "E"):
    print("Invalid input")
    breaths_choice = (input("Choose Breathing style : "))

  if breaths_choice == "A":
    breathingStyle = "Flame Breath"
    print ("Your Breath Is Fire\n")
  elif breaths_choice == "B":
    breathingStyle = "Water Breath"
    print ("Your Breath Is Water\n")
  elif breaths_choice == "C":
    breathingStyle = "Thunder Breath"
    print ("Your Breath Is Thunder\n")
  elif breaths_choice == "D":
    breathingStyle = "Wind Breath"
    print ("Your Breath Is Wind\n")
  elif breaths_choice == "E":
    breathingStyle = "Stone Breath"
    print ("Your Breath Is Stone\n")

def doDamage(damage):
  global health
  health = health - damage
  print("You were dealt", damage, "damage")
  
  if (health < 1):
    print("You are dead")
    return True
  else:
    print("You are on", health, "health \n")
    return False

def getStat(type = "", doPrint = False):
  if doPrint:
    if (type == "Name"):
      print ("Player Name:", name)
    elif (type == "Level"):
      print ("Player Lvl:", level)
    elif (type == "BreathingStyle"):
      print ("Player Breathing Style:", breathingStyle)
    elif (type == "Health"):
      print ("Player Hp:", health)
    elif (type == "Attack"):
      print ("Player Attack:", attack)
    else:
      print ("Player Name:", name)
      print ("Player Lvl:", level)
      print ("Player Breathing Style:", breathingStyle)
      print ("Player Hp:", health)
      print ("Player Attack:", attack)

  if (type == "Name"):
    return name
  elif (type == "Level"):
    return level
  elif (type == "BreathingStyle"):
    return breathingStyle
  elif (type == "Health"):
    return health
  elif (type == "Attack"):
    return attack
  else:
    return ""

from Forms import breathing_forms as forms

def getForms():
  listforms = forms.getMoves(breathingStyle)
  numlistforms = 1
  for i in listforms:
    print ("["+str(numlistforms)+"]" + i)
    numlistforms = numlistforms + 1
  return numlistforms

def useForm(inForm):
  modForm = forms.getMoves(breathingStyle)[inForm]
  modForm = modForm[modForm.find(":")+2:]
  if breathingStyle == "Flame Breath":
    return forms.flame_moves(attack, modForm)
  elif breathingStyle == "Water Breath":
    return forms.water_moves(attack, modForm)
  elif breathingStyle == "Thunder Breath":
    return forms.thunder_moves(attack, modForm)
  elif breathingStyle == "Wind Breath":
    return forms.wind_moves(attack, modForm)
  elif breathingStyle == "Stone Breath":
    return forms.stoney_moves(attack, modForm)

def isMulti(inForm):
  return forms.isMultiAttack(forms.getMoves(breathingStyle)[inForm])