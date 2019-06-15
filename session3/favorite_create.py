fav = ["death note", "neflix", "teaching"]
print(*fav, sep=", ")
input_fav = input("What's fav? ")
fav.append(input_fav)
print(*fav, sep=", ")