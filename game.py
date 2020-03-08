import random


def game(n):
    bank = 0   # our bank
    rounds = n - 1  # number of rounds
    s = 0
    flag = False  # cheak to generate of random peoples after every rounds

    def check(c):
        if c < 0: return n-1  # if was first and then we need last
        if c > n-1: return 0  # other way
        return c

    def check_choice(randommember):
        num = random.randint(1, 6)  # generate tossing the cube
        # print(n,num, randommember)
        if num <= 2:  # if one or two on cube
            randommember = check(randommember - 1)
        if num >= 5:  # if five or six
            randommember = check(randommember + 1)
        return randommember  # if three or four

    while rounds != 0:
        if not flag:  # generate peoples after every rounds and at the beginning
            randommember1 = random.randint(0, n - 1)  # generate first member
            randommember2 = random.randint(0, n - 1)  # generate second
            #print("1")
        if randommember1 == randommember2:  # if cubes are in one player
            bank += s ** 2  # calculate bank
            n -= 1  # number of players minus one
            s = 0
            rounds -= 1
            # print("2")
            flag = False  # for generating new random members
            continue

        randommember1 = check_choice(randommember1)  # tossing a cube and passing it
        randommember2 = check_choice(randommember2)
        flag = True
        s += 1
        # print(randommember1 , randommember2)

    return int(bank)


summ = 0
num = 1000
for i in range(num):
    g = game(50)
    summ += g

print("{:.9e}".format(summ / num))