names = []

with open("names.txt") as file:
    for list in file:
        names.append(list.rstrip())

for name in sorted(names):
    print(f"hello,{name}")