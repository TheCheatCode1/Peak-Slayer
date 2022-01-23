import random
currentEnemy = 0 #Pos in enemyList Array
enemyList = []

def getCurrentEnemy():
  return currentEnemy

def getEnemyCount():
  return len(enemyList)

def createEnemy(name, health, damage):
  level_list = [1, 4, 5, 2, 7]
  enemyLevel = random.choice(level_list)
  enemyHp = 5 * health * enemyLevel
  enemyDamage = 2 * damage * enemyLevel
  enemyList.append({'Name': name, 'Level': enemyLevel, 'Health': enemyHp, 'Damage': enemyDamage})

def printEnemies():
  for x in enemyList:
    print("[", x['Name'],"] is at", x['Health'], "health")

def checkName(testName):
  for x in enemyList:
    if(x['Name'] == testName):
      return True
  return False

def setEnemy(testName):
  global currentEnemy
  i = 0
  for x in enemyList:
    if(x['Name'] == testName):
      currentEnemy = i
    i = i + 1

def incrementEnemy():
  global currentEnemy
  currentEnemy = currentEnemy + 1

def zeroEnemy():
  global currentEnemy
  currentEnemy = 0

def doDamage(damage):
  global currentEnemy
  enemyList[currentEnemy]['Health'] = enemyList[currentEnemy]['Health'] - damage
  
  if (enemyList[currentEnemy]['Health'] < 1):
    print(enemyList[currentEnemy]['Name'], "has perished \n")
    currentEnemy = currentEnemy - 1
  else:
    print(damage, "Damage Dealt to", enemyList[currentEnemy]['Name'], enemyList[currentEnemy]['Health'], "Hp remaining \n")
  return False

def aliveCheck():
  for x in enemyList:
    if(x['Health'] < 1):
      enemyList.remove(x)

def getStat(type = "", doPrint = False):
  if (doPrint):
    if (type == "Name"):
      print ("Demon Name:", enemyList[currentEnemy]['Name'])
    elif (type == "Level"):
      print ("Demon Lvl:", enemyList[currentEnemy]['Level'])
    elif (type == "Health"):
      print ("Demon Hp:", enemyList[currentEnemy]['Health'])
    elif (type == "Damage"):
      print ("Demon Damage:", enemyList[currentEnemy]['Damage'])
    else:
      print ("Demon Name:", enemyList[currentEnemy]['Name'])
      print ("Demon Lvl:", enemyList[currentEnemy]['Level'])
      print ("Demon Hp:", enemyList[currentEnemy]['Health'])
      print ("Demon Damage:", enemyList[currentEnemy]['Damage'])
  
  if (type == "Name"):
    return enemyList[currentEnemy]['Name']
  elif (type == "Level"):
   return enemyList[currentEnemy]['Level']
  elif (type == "Health"):
    return enemyList[currentEnemy]['Health']
  elif (type == "Damage"):
    return enemyList[currentEnemy]['Damage']
  else:
    return ""