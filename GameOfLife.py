from random import randint
from copy import deepcopy
from pprint import pprint
import os
import time

# world_size = 16
# populations = 14
# world = [[] for _ in range(world_size)]
# for i in range(world_size):
#     for j in range(world_size):
#         world[i].append(randint(0, 1))


# new_world = deepcopy(world)


# for _ in range(populations):
#     for x in range(world_size):
#         for y in range(world_size):
#             alives_in_area = 0
#             for i in (-1, 0, 1):
#                 for i in (-1, 0, 1):
#                     if i != 0 and j != 0:
#                         if (
#                             world[(y - 1 + j + world_size) % world_size][
#                                 (x - 1 + i + world_size) % world_size
#                             ]
#                             == 1
#                         ):
#                             alives_in_area += 1
#             if alives_in_area == 3 or alives_in_area == 2:
#                 new_world[x][y] = 1
#             else:
#                 new_world[x][y] = 0
#     time.sleep(0.25)
#     os.system("cls")
#     for i in range(world_size):
#         for j in range(world_size):
#             if new_world[i][j] == 1:
#                 print(f"\N{MEDIUM BLACK CIRCLE}", end="")
#             else:
#                 print(f"\N{MEDIUM WHITE CIRCLE}", end="")
#         print("")
#     world = deepcopy(new_world)

import numpy as np
from tkinter import Tk, Canvas


class World:
    width = 0
    height = 0
    size = (width, height)
    alive_symbol = "\N{MEDIUM BLACK CIRCLE}"
    dead_symbols = "\N{MEDIUM WHITE CIRCLE}"
    states = 2
    cells = np.zeros(shape=size)
    iteration = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = np.random.randint(
            low=0, high=self.states, size=(self.width, self.height)
        )

    def __repr__(self):
        cells_repr = " " + str(self.cells).replace("[", "").replace("]", "")
        return (
            cells_repr.replace("1", self.alive_symbol)
            .replace("0", self.dead_symbols)
            .replace(".", "")
        )

    def check_rule(self, x, y):
        alives_in_area = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i != 0 and j != 0:
                    if (
                        self.cells[(y - 1 + j + self.height) % self.height][
                            (x - 1 + i + self.width) % self.width
                        ]
                        == 1
                    ):
                        alives_in_area += 1
        return 1 if alives_in_area == 3 or alives_in_area == 2 else 0

    def evolv(self, iterations=50):
        new_cells = np.zeros_like(self.cells)
        for _ in range(iterations):
            for x in range(0, self.width):
                for y in range(0, self.height):
                    new_cells[x][y] = self.check_rule(x, y)
            self.cells = deepcopy(new_cells)
            self.iteration += 1
        del new_cells

    def get_data(self):
        """
        get_data [summary]
        Размеры мира
        Текущее поколенее
        Число живых
        Число мертвых
        """
        print(f"Размеры мира:{self.height*self.width} ")
        print(f"Текущее поколение:{self.iteration} ")
        print(f"Число живых:{self.height*self.width-np.count_nonzero(self.cells)} ")
        print(
            f"Число мертвых:{self.height*self.width-(self.height*self.width-np.count_nonzero(self.cells))}"
        )


my_world = World(30, 30)
print(my_world)
my_world.evolv()
print(my_world)
my_world.get_data()
