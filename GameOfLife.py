from random import randint
from copy import deepcopy
from pprint import pprint
import os
import time
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
    iterations = -1
    alives_cells = 0
    dead_cells = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = np.random.randint(
            low=0, high=self.states, size=(self.width, self.height)
        )
        self.world_size = self.height * self.width
        self.update_metadata()

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
        self.update_metadata()
        del new_cells

    def update_metadata(self):
        self.iterations += 1
        self.alives_cells = np.count_nonzero(self.cells)
        self.dead_cells = self.world_size - self.alives_cells

    def get_info(self):
        """
        get_data [summary]
        Размеры мира
        Текущее поколенее
        Число живых
        Число мертвых
        """
        info = f"{self.world_size=}\n{self.iterations=}\n{self.alives_cells=}\n{self.dead_cells=}"
        return info


my_world = World(30, 30)
print(my_world)
my_world.evolv()
print(my_world)
print(my_world.get_info())
