stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  print(stock_prices[x-1])

def max_price(a, b):
  1 <= a <= 20 and 1 <= b <= 20
  print(max(stock_prices[a:b+1]))

def min_price(a, b):
  1 <= a <= 20 and 1 <= b <= 20
  print(min(stock_prices[a:b+1]))

price_at(1)
max_price(1,4)
min_price(1,4)