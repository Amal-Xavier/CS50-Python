name = (input("what's your name? "))

match name:
    case "Harry" | "hermione" | "Ron":
        print("Gryffindor")
    case "Draco" | "voldemort":
        print("Slytherin")
    case _:
        print("Who?")