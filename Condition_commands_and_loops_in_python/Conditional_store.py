price = int(input())

if price > 50000:
    price = price * 0.8
elif 50000 >= price > 20000:
    price = price * 0.9
else:
    pass

print(price)