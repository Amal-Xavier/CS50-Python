def main():
    x = int(input("whats x? "))
    if is_even(x):
        print("its even")
    else:
        print("its odd")

def is_even(n):
    return (n % 2 == 0)

main()