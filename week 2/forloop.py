def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("how many meows? "))
        if n > 0:
            break
    return n

def meow(m):
    for i in range(m):
        print("meow")


main()