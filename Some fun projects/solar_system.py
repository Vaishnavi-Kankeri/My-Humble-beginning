from math import pi as π
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury': r = 2440
elif random_planet == 'Venus': r = 6052
elif random_planet == 'Earth': r = 6371
elif random_planet == 'Mars': r = 3390
elif random_planet == 'Saturn': r = 58232
else: print("Oops! An error occurred.")

area = 4*π*r**2

print(random_planet)
print(int(area))
