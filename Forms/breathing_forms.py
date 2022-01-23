def flame_moves(attack,type):
  # damage = attack * movepower + modifier
  damage = 0
  if type == "Unknowing Fire":
    damage = attack * 1.5 + 10
  elif type == "Rising Scorching Sun":
    damage = attack * 1.5 + 30
  elif type == "Blazing Universe":
    damage = attack * 1.5 + 35
  elif type == "Blooming Flame Undulation":
    damage = attack * 1.5 + 40
  elif type == "Flame Tiger":
    damage = attack * 1.7 + 50
  elif type == "Rengoku":
    damage = attack * 2.5 + 100
  else:
    damage = -1
  return damage

def water_moves(attack,type):
  # damage = attack * movepower + modifier
  damage = 0
  if type == "Water Surface Slash":
    damage = attack * 1.5 + 10
  elif type == "Water Wheel":
    damage = attack * 1.5 + 30
  elif type == "Flowing Dance":
    damage = attack * 1.5 + 35
  elif type == "Striking Tide":
    damage = attack * 1.5 + 40
  elif type == "Blessed Rain After the Drought":
    damage = attack * 1.7 + 50
  elif type == "Drop Ripple Thrust":
    damage = attack * 1.7 + 50
  elif type == "Whirlpool":
    damage = attack * 2.5 + 100
  elif type == "Waterfall Basin":
    damage = attack * 1.5 + 30
  elif type == "Splashing Water Flow, Turbulent":
    damage = attack * 1.7 + 50
  elif type == "Constant Flux":
    damage = attack * 2.5 + 100
  else:
    damage = -1
  return damage

def thunder_moves(attack,type):
  # damage = attack * movepower + modifier
  damage = 0
  if type == "Thunderclap and Flash":
    damage = attack * 1.5 + 10
  elif type == "Rice Spirit":
    damage = attack * 1.5 + 30
  elif type == "Thunder Swarm":
    damage = attack * 1.5 + 35
  elif type == "Distant Thunder":
    damage = attack * 1.5 + 40
  elif type == "Heat Lightning":
    damage = attack * 1.7 + 50
  elif type == "Rumble and Flash":
    damage = attack * 2.5 + 100
  else:
    damage = -1
  return damage

def wind_moves(attack,type):
  # damage = attack * movepower + modifier
  damage = 0
  if type == "Dust Whirlwind Cutter":
    damage = attack * 1.5 + 10
  elif type == "Claws-Purifying Wind":
    damage = attack * 1.5 + 30
  elif type == "Clean Storm Wind Tree":
    damage = attack * 1.5 + 35
  elif type == "Rising Dust Storm":
    damage = attack * 1.5 + 40
  elif type == "Cold Mountain Wind":
    damage = attack * 1.7 + 50
  elif type == "Black Wind Mountain Mist":
    damage = attack * 2.5 + 100
  elif type == "Gale, Sudden Gusts":
    damage = attack * 1.5 + 30
  elif type == "Primary Gale Slash":
    damage = attack * 1.5 + 35
  elif type == "Idaten Typhoon":
    damage = attack * 1.5 + 35
  else:
    damage = -1
  return damage

def stoney_moves(attack,type):
  # damage = attack * movepower + modifier
  damage = 0
  if type == "Serpentinite Bipolar":
    damage = attack * 1.5 + 10
  elif type == "Upper Smash":
    damage = attack * 1.5 + 30
  elif type == "Stone Skin":
    damage = attack * 1.5 + 40
  elif type == "Volcanic Rock, Rapid Conquest ":
    damage = attack * 1.7 + 50
  elif type == "Arcs of Justice":
    damage = attack * 2.5 + 100
  else:
    damage = -1
  return damage

def getMoves(breath):
  if breath == "Flame Breath":
    return ["First Form: Unknowing Fire", "Second Form: Rising Scorching Sun", "Third Form: Blazing Universe", "Fourth Form: Blooming Flame Undulation", "Fifth Form: Flame Tiger", "Ninth Form: Rengoku"]
  elif breath == "Water Breath":
    return ["First Form: Water Surface Slash", "Second Form: Water Wheel", "Third Form: Flowing Dance", "Fourth Form: Striking Tide", "Fifth Form: Blessed Rain After the Drought", "Sixth Form: Whirlpool", "Seventh Form: Drop Ripple Thrust", "Eighth Form: Waterfall Basin", "Ninth Form: Splashing Water Flow, Turbulent", "Tenth Form: Constant Flux"]
  elif breath == "Wind Breath":
    return ["First Form:Dust Whirlwind Cutter", "Second Form: Claws-Purifying Wind", "Third Form: Clean Storm Wind Tree", "Fourth Form: Rising Dust Storm", "Fifth Form: Cold Mountain Wind", "Sixth Form: Black Wind Mountain Mist", "Seventh Form: Gale, Sudden Gusts", "Eighth Form: Primary Gale Slash", "Ninth Form: Idaten Typhoon"]
  elif breath == "Wind Breath":
    return ["First Form: Thunderclap and Flash", "Second Form: Rice Spirit", "Third Form: Thunder Swarm", "Fourth Form: Distant Thunder", "Fifth Form: Heat Lightning", "Sixth Form: Rumble and Flash"]
  elif breath == "Stone Breath":
    return ["First Form: Serpentinite Bipolar", "Second Form: Upper Smash", "Third Form: Stone Skin", "Fourth Form: Volcanic Rock, Rapid Conquest","Fifth Form: Arcs of Justice"]

def isMultiAttack(type):
  if (type == "Flame Tiger","Waterfall Basin","Idaten Typhoon","Rice Spirit", "Rumble and Flash", "Dust Whirlwind Cutter","Whirlpool"):
    return True
  else:
    return False