def main():
    number = get_number("whats x? ")
    print(f"x is {number}")


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass
        
      

main()
        