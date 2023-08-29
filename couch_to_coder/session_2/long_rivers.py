rivers = [ 
       {"name": "Nile", "length": 4157},
       {"name": "Yangtze", "length": 3434},    
       {"name": "Murray-Darling", "length": 2310},    
       {"name": "Volga", "length": 2290},    
       {"name": "Mississippi", "length": 2540},   
       {"name": "Amazon", "length": 3915}
]
# Task 1: to print names of rivers
print("\n")
print("These are the names of all the rivers")
for river in rivers:
    print(river["name"])

# Task 2: Printing out the total length of all rivers
print("\n")
total_length = 0
for river in rivers:
    total_length += river["length"]
print(f"The total length of all the rivers is {total_length}m")

# Task 3: to print names of rivers that begin with 'M'
print("\n")
print("The following rivers start with letter M")
for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])
    else:
        continue

#Task 4: To print out the length of rivers in Miles
print("\n")
for river in rivers:
    lengthInMiles = river['length']/1.6
    print(f"The {river['name']} river is {river['length']} in meters and is {lengthInMiles} in miles ")