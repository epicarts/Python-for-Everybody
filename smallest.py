smallest = None
for value in [9, 2, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('Atfer', smallest)
