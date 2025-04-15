import random

def fortune():
  a = random.randint(0, 7)
  if a == 0:
    print("Don't pursue happiness – create it.")
  elif a == 1:
    print("All things are difficult before they are easy.")
  elif a == 2:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif a == 3:
    print("Someone in your life needs a letter from you.")
  elif a == 4:
    print("Don't just think. Act!")
  elif a == 5:
    print("Your heart will skip a beat.")
  elif a == 6:
    print("The fortune you search for is in another cookie.")
  elif a == 7:
    print("Help! I'm being held prisoner in a Chinese bakery!")
  
fortune()
fortune()
fortune()
fortune()
fortune()
fortune()
fortune()
fortune()
