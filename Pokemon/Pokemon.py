class Pokemon():
  def __init__(self, name, level, type, maximum_health, current_health, is_knocked_out):
    self.name = name
    self.level = level
    self.type = type
    self.maximum_health = maximum_health
    self.current_health = current_health
    self.is_knocked_out = is_knocked_out
   
  def lose_health(self, decrease_amount):
    self.current_health = self.current_health - decrease_amount
    if self.current_health > 0:
      print("{} has taken {} damage. Current health is {}.".format(self.name, decrease_amount, self.current_health))
    else:
      self.current_health = 0
      print("{} has taken {} damage.".format(self.name, decrease_amount))
  
  def regain_health(self, regain_amount):
    self.current_health = self.current_health + regain_amount
    if self.current_health > self.maximum_health:
      self.current_health = self.maximum_health
      print("{} has been healed to it´s maximum HP {}.".format(self.name, self.maximum_health))
    else:
      print("{} has been healed by {}. Current health is {} HP.".format(self.name, regain_amount, self.current_health))
  
  def knock_out(self):
    self.is_knocked_out = True
    print("{} has lost all of it´s HP. {} is knocked out.".format(self.name, self.name))

  def revive(self):
    self.is_knocked_out = False
    print("{} has been revived and is ready for another adventure!".format(self.name))



shiggy = Pokemon("Shiggy", 20, "Water", 100, 100, False)

shiggy.lose_health(100)
print(shiggy.current_health)
shiggy.regain_health(15)
print(shiggy.current_health)
