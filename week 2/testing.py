try:
    x = int(input("what the x? "))
except ValueError:
    print("x is not an integer")
else:

    print(f"x is {x}")  # <-- This line is sitting out in the open now!