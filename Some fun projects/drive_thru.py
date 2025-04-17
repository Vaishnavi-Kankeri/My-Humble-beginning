def welcome():
  return 'WELCOME TO Mc D'

def get_item(a):
  if a == 1:
    return '🍔 Cheeseburger'
  if a == 2:
    return '🍟 Fries'
  if a == 3:
    return '🥤 Soda'
  if a == 4:
    return '🍦 Ice Cream'
  if a == 5:
    return '🍪 Cookie'

print(welcome())
print(get_item(int(input("Enter your number here: "))))