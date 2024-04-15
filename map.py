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
        self.entities_placed = {}


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
        self.camp_positions = {}

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
        self.camp_positions[l_creature] = l_camp
        self.camp_positions[r_creature] = r_camp


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
    def __init__(self, world_map):
        self.world_map = world_map

    def render(self):
        for (x, y), occupant in self.world_map.coordinates.items():
            self.world_map.grid[y][x] = Tile.get_tile(occupant if occupant else 'empty')
        self.print_grid()

    def print_grid(self):
        for row in self.world_map.grid:
            print("".join(row))


class Populate:
    def __init__(self, world_map, camps_calculator):
        self.world_map = world_map
        self.camps_calculator = camps_calculator

    def place_creatures(self):
        for creature, positions in self.camps_calculator.camp_positions.items():
            self.world_map.entities_placed[creature] = len(positions)
            for x, y in positions:
                self.world_map.coordinates[(x, y)] = creature

    def place_terrain(self):
        empty_coords = [coord for coord, occupant in self.world_map.coordinates.items() if occupant is None]
        entities = self.camps_calculator.entity_distribution.calculate_entities()
        for entity, count in entities.items():
            if entity in self.world_map.entities_placed:
                continue
            else:
                while count > 0:
                    chosen_coord = random.choice(empty_coords)
                    self.world_map.coordinates[chosen_coord] = entity
                    empty_coords.remove(chosen_coord)
                    count -= 1


def launch_simulation():
    world_map = WorldMap()
    entity_distribution = EntityDistribution(world_map)
    camps_calculator = CampsCalculator(entity_distribution)
    camps_calculator.randomize_camps('elf', 'vampire')
    populate = Populate(world_map, camps_calculator)
    populate.place_creatures()
    populate.place_terrain()
    renderer = Render(world_map)
    renderer.render()


if __name__ == "__main__":
    launch_simulation()
