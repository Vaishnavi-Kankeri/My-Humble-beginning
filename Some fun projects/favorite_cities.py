class City:
  def __init__(self, name, country, population, landmarks, nickname, founding_year):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.nickname = nickname
    self.founding_year = founding_year

New_Delhi = City('New Delhi', 'India', 250000, 'Lotus Temple', 'Apna Delhi', 1931 )

print(vars(New_Delhi))


# class Student: 
#   def __init__(self, name, year, gpa, enrolled):
#     self.name = name
#     self.year = year
#     self.gpa = gpa
#     self.enrolled = enrolled

# daniel = Student('Daniel Li', 10, 4.0, True)
# print(vars(daniel))
# Output: {}