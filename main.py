data = open("names.txt")
for name in data.readlines()
    print(f"Hello, {name}")
data.close()