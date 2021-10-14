import math
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


def azimut_to_angle_rad(azimut: float) -> float:
    return ((-azimut + 90) % 360) * math.pi / 180


if __name__ == '__main__':
    carte = creer_random_carte(5, 10)
    print(carte)
    affiche_carte(carte)
    for i in range(0, 361, 45):
        print(i, azimut_to_angle_rad(i))
