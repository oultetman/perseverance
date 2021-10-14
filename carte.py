from random import randint


def creer_carte_vide(long_x: int, long_y: int) -> list:
    return [[0 for i in range(long_x)] for j in range(long_y)]


def creer_random_carte(long_x: int, long_y: int) -> list:
    carte = creer_carte_vide(long_x, long_y)
    for i in range(long_y):
        for j in range(long_x):
            if randint(0, 100) > 50:
                carte[i][j] = 1
            else:
                carte[i][j] = 0
    return carte


def affiche_carte(carte: list):
    s = "   "
    for i in range(len(carte[0])):
        s += f"{i:^3}"
    print(s)

    for i in range(len(carte)):
        s = f"{i:^3}"
        for j in range(len(carte[0])):
            if carte[i][j] == 1:
                s += f"{'X':^3}"
            else:
                s += "   "
        print(s)


carte = creer_random_carte(5, 10)
print(carte)
affiche_carte(carte)
