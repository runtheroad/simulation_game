from emoji import emojize


class Map:
    def __init__(self, length=10, height=5):
        self.length = length
        self.height = height
        self.grid = [[Tile.get_tile("grass") for _ in range(length)] for _ in range(height)]
        self.grid_size = length * height


class Tile:
    tile_types = {
        "empty": emojize(":white_large_square:"),
        "grass": emojize(":shamrock:"),
        "tree": emojize(":evergreen_tree:"),
        "rock": emojize(":mountain:"),
        "elf": emojize(":elf:"),
        "vampire": emojize(":vampire:"),
    }

    @staticmethod
    def get_tile(tile_type):
        return Tile.tile_types.get(tile_type, Tile.tile_types["empty"])


map = Map()
map.grid[0][0] = Tile.get_tile("vampire")
map.grid[1][1] = Tile.get_tile("elf")
map.grid[4][9] = Tile.get_tile("rock")

for row in map.grid:
    print("".join(row))