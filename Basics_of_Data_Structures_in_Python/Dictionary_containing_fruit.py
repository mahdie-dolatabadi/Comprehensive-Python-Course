# defining the dictionary
fruit_prices = {"apple" : 1500,
                "banana" : 1000, 
                "orange" : 1200}

# Update the price of banana
fruit_prices['banana'] = 1100

# remove the apple
fruit_prices.pop('apple')

# show the new dictionary
print(fruit_prices)