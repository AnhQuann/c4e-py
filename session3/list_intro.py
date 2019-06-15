# List
# index

# 1. READ
# print(menu)
# print(menu[-4])

# use loop
# loop items
# for item in menu:
#     print(item)

# loop index
# for index in range(len(menu)):
#     print(index)

# loop item and index
# for index, item in enumerate(menu):
#     print(index, item)

# 2. CREATE
# menu = ["Com", "Canh", "Thit"]
# menu.append("Rau")
# print(menu)

# 3. UPDATE
# menu = ["Com", "Canh", "Thit"]
# menu[0] = "Pho"
# print(menu)

# 4. DELETE
menu = ["Com", "Canh", "Thit"]
# del menu[1]
menu.remove("Canh")
print(menu)