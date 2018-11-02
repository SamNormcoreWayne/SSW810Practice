import random


def RandomIntGen(minium, maxium):
    while True:
        yield random.randint(minium, maxium)


def TestGen():
    domain = input('number: ')
    for i in range(0, int(domain)):
        print(next(RandomIntGen(0, 10)))
        print(RandomIntGen(0, 10))


def find_target(target, minimum, maximum, limit):
    if not (isinstance(target, int) and isinstance(minimum, int) and isinstance(maximum, int) and isinstance(limit, int)):
        raise ValueError('One of your inputs is not right. \n')

    gen = RandomIntGen(minimum, maximum)
    for i in range(0, limit):
        if target == next(gen):
            return i
            break
    return 'Not found 5 in ' + str(limit) + ' times. '


def main():
    # TestGen()
    while True:
        quit = input("Enter 'quit' to quit, others to continue. ")
        if quit == 'quit':
            exit()
        target = int(input("Input target: "))
        minimum = int(input("Input min_value: "))
        maximum = int(input("Input max_value: "))
        limit = int(input("Input limit of loops: "))
        try:
            print(find_target(target, minimum, maximum, limit))
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()
