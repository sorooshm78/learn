import random
from enum import Enum

import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Cell(Enum):
    empty = "o"
    ship = "#"
    select = "x"
    target = "*"


class Ship:
    def __init__(self, point, length, direct):
        if direct == "up":
            self.points = Point(
                slice(point.x - length + 1, point.x + 1), slice(point.y, point.y + 1)
            )

        if direct == "down":
            self.points = Point(
                slice(point.x, point.x + length), slice(point.y, point.y + 1)
            )

        if direct == "right":
            self.points = Point(
                slice(point.x, point.x + 1), slice(point.y, point.y + length)
            )

        if direct == "left":
            self.points = Point(
                slice(point.x, point.x + 1), slice(point.y - length + 1, point.y + 1)
            )

        self.range_points = Point(
            slice(max(0, self.points.x.start - 1), max(0, self.points.x.stop + 1)),
            slice(max(0, self.points.y.start - 1), max(0, self.points.y.stop + 1)),
        )

    def get_points(self):
        return self.points

    def get_range_points(self):
        return self.range_points


class Table:
    row = 10
    col = 10

    def __init__(self):
        self.coordinates = np.full((self.row, self.col), Cell.empty.value)
        self.ships = []
        self.make_ships()

    def make_ships(self):
        self.make_ship(4)
        self.make_ship(3)
        self.make_ship(2)
        self.make_ship(2)
        self.make_ship(1)
        self.make_ship(1)

    def make_ship(self, length):
        while True:
            point = self.get_random_empty_point()
            directs = np.array(["up", "down", "right", "left"])
            random.shuffle(directs)
            for direct in directs:
                ship = self.get_ship(point, length, direct)
                if ship is not None:
                    self.coordinates[ship.points.x, ship.points.y] = Cell.ship.value
                    self.ships.append(ship)
                    return

    def get_random_empty_point(self):
        while True:
            x = random.randrange(self.row)
            y = random.randrange(self.col)
            if self.coordinates[x, y] == Cell.empty.value:
                return Point(x, y)

    def get_ship(self, point, length, direct):
        ship = Ship(point, length, direct)

        point = ship.get_points()
        range_points = ship.get_range_points()

        if self.coordinates[point.x, point.y].size != length:
            return None

        if Cell.ship.value in self.coordinates[range_points.x, range_points.y]:
            return None

        return ship


# Manage Game
class SeaBattle:
    def __init__(self, user_id):
        self.start_new_game()

    def start_new_game(self):
        self.table = Table()

    def get_table_game(self):
        return self.table.coordinates

    def select_cell(self, x, y):
        selecte_cell = self.table.coordinates[x, y]
        if selecte_cell == Cell.ship.value or selecte_cell == Cell.target.value:
            cell = Cell.target.value
        else:
            cell = Cell.select.value

        self.table.coordinates[x, y] = cell
        return cell

    def is_end_game(self):
        if Cell.ship.value not in self.table.coordinates:
            return True
        return False


sea = SeaBattle("1")
print(sea.get_table_game())
