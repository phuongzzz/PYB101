class Pokemon(object):
  attack = 12
  defense = 10
  health = 15
  p_type = "Normal"

  health_boost = 0
  attack_boost = 0
  defense_boost = 0
  evolve = 0

  def __init__(self, name, level = 5):
    self.name = name
    self.level = level

  def train(self):
    self.update()
    self.attack_up()
    self.defense_up()
    self.health_up()
    self.level = self.level + 1
    if self.level%self.evolve == 0:
      return self.level, "Evolved!"
    else:
      return self.level

  def attack_up(self):
    self.attack += self.attack_boost
    return self.attack

  def defense_up(self):
    self.defense += self.defense_boost
    return self.defense

  def health_up(self):
    self.health += self.health_boost
    return self.health

  def update(self):
    self.health_boost = 5
    self.attack_boost = 3
    self.defense_boost = 2
    self.evolve = 10

  def __str__(self):
    self.update()
    return "Pokemon name: {}, Type: {}, Level: {}\r\nAttack: {}, Defense: {}, Health: {}".format(self.name, self.p_type, self.level, self.attack, self.defense, self.health)

class Grass_Pokemon(Pokemon):
  attack = 15
  defense = 14
  health = 12
  p_type = "Grass"
  weak = ""
  strong = ""

  def update(self):
    self.health_boost = 6
    self.attack_boost = 2
    self.defense_boost = 3
    self.evolve = 12

  def __init__(self, name,level = 5):
    super().__init__(name, level)
    self.weak = "Dark"
    self.strong = "Psychic"

  def train(self):
    self.update()
    if self.level >= 10: self.attack_up()
    self.defense_up()
    self.health_up()
    self.level = self.level + 1
    if self.level%self.evolve == 0:
      return self.level, "Evolved!"
    else:
      return self.level

  def moves(self):
    self.p_moves = ["razor leaf", "synthesis", "petal dance"]

  def action(self):
    return self.name + " knows a lot of different moves!"
  
class Ghost_Pokemon(Pokemon):
  p_type = "Ghost"
  weak = "Dark"
  strong = "Psychic"

  def __init__(self, name,level = 5):
    super().__init__(name, level)

class Fire_Pokemon(Pokemon):
  p_type = "Fire"
  weak = "Water"
  strong = "Grass"

  def __init__(self, name,level = 5):
    super().__init__(name, level)

class Flying_Pokemon(Pokemon):
  p_type = "Flying"
  weak = "Electric"
  strong = "Fighting"

  def __init__(self, name,level = 5):
    super().__init__(name, level)
# Testing
# pokemon = Pokemon('Alomomola', 9)
# print(pokemon)
# print('------')
# print('Traning: ', pokemon.train())
# print('------')
# print(pokemon)

# p1 = Grass_Pokemon('Petilil', 9)
# print(p1)
# print('------')
# print('Traning: ', p1.train())
# print('------')
# print(p1)
# print('------')
# print('Traning: ', p1.train())
# print('------')
# print(p1)

# print(Ghost_Pokemon('Cofagrigus', 10))
# print(Fire_Pokemon('Reshiram', 12))
# print(Ghost_Pokemon('Zapdos', 9))