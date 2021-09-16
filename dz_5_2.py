import random


def getRandomOdd(start=0, end=10):
    return random.randrange(start // 2, end // 2) * 2 + 1


def main():
    for i in range(10):
        print(getRandomOdd())


if __name__ == "__main__":
    main()
