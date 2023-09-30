color_in = str(input("Which color block will you be building on? "))
money_in = int(input("How much money do you have to spend? "))

# Dictionary of cost for each block color numerically
cost_Dict = {
    'purple': 50,
    'light blue': 50,
    'maroon': 100,
    'orange': 100,
    'red': 150,
    'yellow': 150,
    'green': 200,
    'dark blue': 200
}

# Dictionary of the English numbers
number_Dict = {
    0: 'none',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'hotels',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'hotel'
}

# Dictionary of sizes for each block in numeric version
sizeNumDict = {
    'purple': 2,
    'light blue': 3,
    'maroon': 3,
    'orange': 3,
    'red': 3,
    'yellow': 3,
    'green': 3,
    'dark blue': 2
}

# Dictionary of size of blocks in English
size_Dict = {
    'purple': 'two',
    'light blue': 'three',
    'maroon': 'three',
    'orange': 'three',
    'red': 'three',
    'yellow': 'three',
    'green': 'three',
    'dark blue': 'two'
}

# Calculate the maximum number of hotels and houses that can be built
max_hotels = money_in // (5 * cost_Dict[color_in])  # Each hotel costs as much as 5 houses
max_houses = (money_in % (5 * cost_Dict[color_in])) // cost_Dict[color_in]

# Check if you can afford any houses or hotels
if money_in >= 50:
    # First will print function to tell you properties and the cost of each house
    print(f'There are {sizeNumDict[color_in]} {color_in} properties, and each will cost {cost_Dict[color_in]} dollars.')

    # Generate the output
    if max_hotels >= 1:
        if max_houses > 0:
            house_str = f' and {number_Dict[max_houses]} houses'
        else:
            house_str = ''
        hotel_str = f'{number_Dict[max_hotels]} hotels'
        print(f'You can build {hotel_str}{house_str} on the {color_in} properties.')
    elif max_houses > 0:
        print(f'You can build {number_Dict[max_houses]} houses on the {color_in} properties.')
else:
    print('You cannot afford any houses.')
