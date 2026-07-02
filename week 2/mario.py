def main():
    mario_bricks(3)


def mario_bricks(size):
    for i in range(size):
        for j in range(size):
            print("*", end = "")
        print()

main()