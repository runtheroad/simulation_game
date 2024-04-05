import random

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
    def __init__(self, entity_distribution):
        self.world_map = entity_distribution.world_map
        self.entity_distribution = entity_distribution

    def _calculate_regions(self):
        left_region_width = int(self.world_map.length * 0.2)
        right_region_width = left_region_width

        left_region = [(x, y) for x in range(left_region_width) for y in range(self.world_map.height)]
        right_region = [(x, y) for x in range(self.world_map.length - right_region_width, self.world_map.length)
                        for y in range(self.world_map.height)]
        return left_region, right_region

    def _get_creature_quantity(self, creature):
        total_entities = self.entity_distribution.calculate_entities()
        return total_entities.get(creature)

    def randomize_camps(self, l_creature, r_creature):
        left_reg, right_reg = self._calculate_regions()
        l_c = self._get_creature_quantity(l_creature)
        r_c = self._get_creature_quantity(r_creature)
        l_camp = random.sample(left_reg, l_c)
        r_camp = random.sample(right_reg, r_c)
        return l_camp, r_camp


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


class Populate:
    def __init__(self, to_populate, entities):
        self.to_populate = to_populate,
        self.entities = entities

   # def place_creatures(self):



# worldmap = WorldMap()
# print(worldmap.coordinates)
# renderer = Render(worldmap)
# renderer.render()

wm = WorldMap()
ent = EntityDistribution(wm)
camps = CampsCalculator(ent)
print(camps.randomize_camps("elf", "vampire"))

print(wm.coordinates)
