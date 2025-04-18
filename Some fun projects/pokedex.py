class Pokemon:
  def __init__(self, entry , name, types , description , is_caught , region):
    self.entry = entry
    self.name = name
    self.types  = types 
    self.description  = description 
    self.is_caught  = is_caught 
    self.region = region 

  def speak(self):
    print(self.name + '!')

  def display_details(self):
    print("Entry Number: " + str(self.entry))
    print("Name: " + self.name)
    print("Type: " + self.types)
    print("Description: " + self.description)
    print(self.is_caught)
    print("Region: " + self.region)


Pikachu = Pokemon(25, 'Pikachu', 'Electric', "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", 'Pikachu has already been caught!', 'Kentai')

Pikachu.speak()
Pikachu.display_details()