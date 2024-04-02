from emoji import emojize
import os
from time import sleep


class WorldMap:
    def __init__(self, length=10, height=5):
        self.length = length
        self.height = height
        self.grid = [[Tile.get_tile("empty") for _ in range(length)] for _ in range(height)]
        self.grid_size = length * height
        self.coordinates = {(y, x): None for y in range(height) for x in range(length)}


class Tile:
    tile_types = {
        "empty": emojize(":brown_square:"),
        "grass": emojize(":shamrock:"),
        "tree": emojize(":evergreen_tree:"),
        "rock": emojize(":mountain:"),
        "elf": emojize(":elf:"),
        "vampire": emojize(":vampire:"),
    }

    @staticmethod
    def get_tile(tile_type):
        return Tile.tile_types.get(tile_type, Tile.tile_types["empty"])


class Render:
    def __init__(self, to_render):
        self.to_render = to_render

    def render(self):
        for row in self.to_render.grid:
            print("".join(row))


# worldmap = WorldMap()
# print(worldmap.coordinates)
# renderer = Render(worldmap)
# renderer.render()
