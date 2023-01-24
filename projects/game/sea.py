import random
from enum import Enum
import numpy as np


class Cell:
    def __init__(self, ship=None):
        self.ship = ship
        self.is_selected = False

    def is_ship(self):
        if self.ship == None:
            return False
        return True


class Direct(Enum):
    up = "up"
    down = "down"
    right = "right"
    left = "left"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


class Ship:
    def __init__(self, point, length, direct):
        self.points = self.get_points_by_direct(point, length, direct)
        self.area = self.get_area_points()
        self.health = length
        self.length = length

    def is_alive(self):
        if self.health == 0:
            return False
        return True

    def get_points_by_direct(self, point, length, direct):
        if direct == Direct.up.value:
            return Point(
                slice(point.x - length + 1, point.x + 1), slice(point.y, point.y + 1)
            )

        elif direct == Direct.down.value:
            return Point(slice(point.x, point.x + length), slice(point.y, point.y + 1))

        elif direct == Direct.right.value:
            return Point(slice(point.x, point.x + 1), slice(point.y, point.y + length))

        elif direct == Direct.left.value:
            return Point(
                slice(point.x, point.x + 1), slice(point.y - length + 1, point.y + 1)
            )

    def get_area_points(self):
        return Point(
            slice(max(0, self.points.x.start - 1), max(0, self.points.x.stop + 1)),
            slice(max(0, self.points.y.start - 1), max(0, self.points.y.stop + 1)),
        )

    def is_inside(self, x, y):
        if x in range(self.points.x.start, self.points.x.stop) and y in range(
            self.points.y.start, self.points.y.stop
        ):
            return True
        return False

    def damage(self):
        if self.is_alive():
            self.health -= 1


class Sea:
    def __init__(self, row, col, list_lenght_ships):
        self.row = row
        self.col = col
        self.list_lenght_ships = list_lenght_ships
        self.make_coordinates()
        self.make_ships()

    def make_coordinates(self):
        self.coordinates = np.empty((self.row, self.col), dtype=object)
        for y, x in np.ndindex(self.coordinates.shape):
            self.coordinates[x, y] = Cell()

    def make_ships(self):
        self.ships = []
        for length in self.list_lenght_ships:
            self.ships.append(self.make_ship(length))

    def get_posible_points(self):
        posible_points = []
        for y, x in np.ndindex(self.coordinates.shape):
            if not self.coordinates[x, y].is_ship():
                posible_points.append(Point(x, y))

        return posible_points

    def mark_as_ship(self, points, ship):
        for cell in self.coordinates[points.x, points.y].flatten():
            cell.ship = ship

    def mark_as_selected(self, points):
        for cell in self.coordinates[points.x, points.y].flatten():
            cell.is_selected = True

    def make_ship(self, length):
        posible_points = self.get_posible_points()
        random.shuffle(posible_points)
        for point in posible_points:
            directs = np.array([direct.value for direct in Direct])
            random.shuffle(directs)
            for direct in directs:
                ship = self.get_random_ship(point, length, direct)
                if ship is not None:
                    self.mark_as_ship(ship.points, ship)
                    return ship

        raise Exception(f"Not Make Ship by length {length}")

    def is_points_valid(self, points):
        if points.x.start < 0 or points.y.start < 0:
            return False

        if points.x.stop > self.row - 1 or points.y.stop > self.col - 1:
            return False

        return True

    def is_area_ship_valid(self, area):
        for cell in self.coordinates[area.x, area.y].flatten():
            if cell.is_ship():
                return False
        return True

    def get_random_ship(self, point, length, direct):
        ship = Ship(point, length, direct)

        if self.is_points_valid(ship.points) and self.is_area_ship_valid(ship.area):
            return ship
        return None

    def target_ship(self, point):
        cell = self.coordinates[point.x, point.y]
        ship = cell.ship

        ship.damage()
        if not ship.is_alive():
            self.mark_as_selected(ship.area)
            return ship.area
        else:
            cell.is_selected = True
            return Point(slice(point.x, point.x + 1), slice(point.y, point.y + 1))

    def get_changes_by_bomb_attack(self, point):
        selected_cell = self.coordinates[point.x, point.y]

        if selected_cell.is_ship():
            return self.target_ship(point)

        else:
            selected_cell.is_selected = True
            return Point(slice(point.x, point.x + 1), slice(point.y, point.y + 1))

    def get_count_ships_by_length(self, length):
        count = 0
        for ship in self.ships:
            if ship.is_alive() and ship.length == length:
                count += 1

        return count
