## The sorting hat 
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

Q1 = int(input('''Q1) Do you like Dawn or Dusk? 
    1) Dawn 
    2) Dusk 
    '''))

if Q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif Q1 == 2:
    Hufflepuff += 1 
    Slytherin += 1
else:
    print('Wrong input')

Q2 = int(input('''
Q2) When I’m dead, I want people to remember me as: 
    1) The Good 
    2) The Great 
    3) The Wise 
    4) The Bold
    '''))

if Q2 == 1:
    Hufflepuff += 2
elif Q2 == 2:
    Slytherin += 2
elif Q2 == 3:
    Ravenclaw += 2
elif Q2 == 4:
    Gryffindor += 2
else:
    print('Wrong input')

Q3 = int(input("""
Q3) Which kind of instrument most pleases your ear? 
    1) The violin 
    2) The trumpet 
    3) The piano 
    4) The drum  
    """))

if Q3 == 1:
    Slytherin += 4
elif Q3 == 2:
    Hufflepuff += 4
elif Q3 == 3:
    Ravenclaw += 4
elif Q3 == 4:
    Gryffindor += 4
else:
    print('Wrong input')

a = [ Gryffindor, Ravenclaw, Hufflepuff, Slytherin]
for i in range(4):
    if i == 0:
        print("The Gryffindor's score:", a[i])
    elif i == 1:
        print("The Ravenclaw's score:", a[i])
    elif i == 2:
        print("The Hufflepuff's score:", a[i])  
    elif i == 3:    
        print("The Slytherin's score:", a[i])
    else:
        print('Wrong input')
        
print('The sorting hat has chosen the house for you!')