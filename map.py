from emoji import emojize
import os
from time import sleep


class WorldMap:
    def __init__(self, length=10, height=5):
        self.length = length
        self.height = height
        self.grid = [[Tile.get_tile("empty") for _ in range(length)] for _ in range(height)]
        self.coordinates = {(x, y): None for x in range(length) for y in range(height)}


class EntityDistribution:
    def __init__(self, world_map):
        self.world_map = world_map
        self.distribution = {
            'elf': 0.1,
            'vampire': 0.1,
            'grass': 0.3,
            'rock': 0.15,
            'tree': 0.15,
            'empty': 0.2,
        }

    def calculate_entities(self):
        total_cells = self.world_map.height * self.world_map.length
        total_entities = {entity: int(total_cells * percentage) for entity, percentage
                          in self.distribution.items()}
        return total_entities


class CampsCalculator:
    def __init__(self, world_map, creatures):
        self.world_map = world_map
        self.creatures = creatures

    def calculate_regions(self):
        left_region_width = int(self.world_map.length * 0.2)
        right_region_width = left_region_width

        left_region = [(x, y) for x in range(left_region_width) for y in range(self.world_map.height)]
        right_region = [(x, y) for x in range(self.world_map.length - right_region_width, self.world_map.length)
                        for y in range(self.world_map.height)]
        return left_region, right_region

    # def create_camp(self, creature):
    #     return [(x, y) for x in range(self.calculate_camp_size(creature)) for y in range(self.world_map.height)]


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


# class Populate():
#     def __init__(self, to_populate, terrain, entities):
#         self.to_populate = to_populate
#         self.terrain = terrain
#         self.entities = entities
#
#     def populate(self):
#         while self.terrain or self.entities:


# worldmap = WorldMap()
# print(worldmap.coordinates)
# renderer = Render(worldmap)
# renderer.render()

wm = WorldMap()
ent = EntityDistribution(wm)
camps = CampsCalculator(wm, ent)
print(camps.calculate_regions())
print(ent.calculate_entities())
print(wm.coordinates)
