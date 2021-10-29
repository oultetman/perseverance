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


def scan_360(terrain: list, angular_step: int, portee_telemetre: int) -> list:
    pass


class Terrain:
    def __init__(self, long_x: int, long_y: int, resolution: float,new:bool=False):
        self.resolution = resolution
        self.long_x = int(long_x / self.resolution)
        self.long_y = int(long_y / self.resolution)
        self.carte = []
        if new:
            self.create_new_terrain()
        else:
            self.create_clear_terrain()

    def create_clear_terrain(self):
        self.carte = [[None for j in range(self.long_x)] for i in range(self.long_y)]

    def create_new_terrain(self):
        self.carte = []
        for i in range(self.long_y):
            self.carte.append([])
            for j in range(self.long_x):
                if randint(0, 100) > 50 and not i==j==5 :
                    self.carte[i].append(1)
                else:
                    self.carte[i].append(0)

    def __str__(self):
        s = "   "
        for i in range(self.long_x):
            s += f"{i:^3}"
        s += "\n"
        for i in range(self.long_y):
            s += f"{i:^3}"
            for j in range(self.long_x):
                if self.carte[i][j] == 1:
                    s += f"{'X':^3}"
                elif self.carte[i][j] == 0:
                    s += f"{'*':^3}"
                else:
                    s += "   "
            s += "\n"
        return s

    def mesure(self, pos: tuple, dmax: float, azimut: int) -> tuple:
        angle_rd = azimut_to_angle_rad(azimut)
        for d in range(1, int(dmax / self.resolution)):
            x = int(d * math.cos(angle_rd)) + pos[0]
            y = -int(d * math.sin(angle_rd)) + pos[1]
            if 0 <= x < len(self.carte[0]) and 0 <= y < len(self.carte) and self.carte[y][x] == 1:
                return d * self.resolution
        return -1


class Perseverance:
    def __init__(self, terrain):
        self.terrain = terrain
        self.fuel = 100
        self.carte = Terrain(100, 100, 10)
        self.pos_carte = 5, 5
        self.pos_terrain = randint(0, self.terrain.long_x), randint(0, self.terrain.long_y)
        self.dmax_telemetre = 40
        self.pas_telemetre = int(self.dmax_telemetre / self.carte.resolution)

    def telemetre(self,azimut:int):
        return self.terrain.mesure(self.pos_carte, self.dmax_telemetre, azimut)

    def scan_360(self):
        for azimut in range(0, 360, 10):
            distance = self.telemetre(azimut)
            angle_rd = azimut_to_angle_rad(azimut)
            if distance != -1:
                d = distance/self.carte.resolution
            else:
                d = self.dmax_telemetre/self.carte.resolution
            for dis in range(1,int(d)):
                x = int(dis * math.cos(angle_rd)) + self.pos_carte[0]
                y = -int(dis * math.sin(angle_rd)) + self.pos_carte[1]
                if 0 <= x <= len(self.carte.carte[0]) and 0 <= y <= len(self.carte.carte):
                    self.carte.carte[y][x] = 0
                #print(x,y,self.carte.carte[y][x])
            if distance!=-1:
                x = int(d * math.cos(angle_rd)) + self.pos_carte[0]
                y = -int(d * math.sin(angle_rd)) + self.pos_carte[1]
                self.carte.carte[y][x] = 1

if __name__ == '__main__':
    # carte = creer_random_carte(5, 10)
    # print(carte)
    # affiche_carte(carte)
    # for i in range(0, 361, 45):
    #     print(i, azimut_to_angle_rad(i))
    p = Perseverance(Terrain(100,100,10.0,True))
    print(p.terrain)
    print(p.carte)
