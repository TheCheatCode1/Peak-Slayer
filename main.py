import replit

import player
import enemy

# Game Intro
print ("Welcome to Peak Slayer\n"
     + "This is a Fan Made Demon Slayer RPG\n"
     + "In this RPG you will fight demons\n")

player.setName()
player.setBreathingStyle()
replit.clear()
player.getStat("", True)
print()

enemy.createEnemy("Boss Alpha", 5, 2)
enemy.getStat("", True)
print()
enemy.createEnemy("Boss Beta", 9, 5)
enemy.setEnemy("Boss Beta")
enemy.getStat("", True)
print()
enemy.setEnemy("Boss Alpha")

won = False
dead = False
while (not won and not dead):
  print("[",enemy.getStat("Name", False),"]:\n"
      + "--------------------\n"
      + "Attack : A \n"
      + "Switch Target: B \n"
      + "Use Breathing Form : C \n")

  player_choice = (input("Choose option : "))
  while (player_choice != "A" and player_choice != "B" and player_choice != "C"):
    print("Invalid input")
    player_choice = (input("Choose option : "))

  if player_choice == "A":
    won = enemy.doDamage(player.getStat("Attack"))
    enemy.aliveCheck()

    if(not won): #Enemy Turn
      tempEnemy = enemy.getStat("Name")
      enemy.zeroEnemy()
      for i in range(enemy.getEnemyCount()):
        dead = player.doDamage(enemy.getStat("Damage"))
        if dead:
          break
        if (i < enemy.getEnemyCount()):
          enemy.incrementEnemy()
      enemy.setEnemy(tempEnemy)
  elif player_choice == "B":
    enemy.printEnemies()
    target_choice = (input("Input the name of the enemy you would like to attack: "))
    while (not enemy.checkName(target_choice)):
      print("Invalid input")
      target_choice = (input("Input the name of the enemy you would like to attack: "))
    enemy.setEnemy(target_choice)
    print()
  elif player_choice == "C":
    validInput = player.getForms()
    player_choice = int(input("Choose option: "))
    while (player_choice < 0 or player_choice > validInput):
      print("Invalid input")
      player_choice = int(input("Choose option: "))
    if (player.isMulti(player_choice-1)):
      tempEnemy = enemy.getStat("Name")
      enemy.zeroEnemy()
      for i in range(enemy.getEnemyCount()):
        won = enemy.doDamage(player.useForm(player_choice-1))
        enemy.incrementEnemy()
      enemy.setEnemy(tempEnemy)
      enemy.aliveCheck()
    else:
      won = enemy.doDamage(player.useForm(player_choice-1))
      enemy.aliveCheck()

    if(enemy.getEnemyCount() == 0):
      enemy.createEnemy("Boss Alpha2", 5, 2)
      enemy.getStat("", True)
      print()
      enemy.createEnemy("Boss Beta2", 9, 5)
      enemy.setEnemy("Boss Beta")
      enemy.getStat("", True)
      print()
      enemy.setEnemy("Boss Alpha")
      
      #print("You win")
      #won = True

    if(not won): #Enemy Turn
      tempEnemy = enemy.getStat("Name")
      enemy.zeroEnemy()
      for i in range(enemy.getEnemyCount()):
        dead = player.doDamage(enemy.getStat("Damage"))
        if dead:
          break
        if (i < enemy.getEnemyCount()):
          enemy.incrementEnemy()
      enemy.setEnemy(tempEnemy)