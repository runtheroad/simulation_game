class Entity:

    def __init__(self):
        self.is_passable = True
        self.passing_cost = 1


class Mud(Entity):
    def __init__(self):
        super().__init__()
        self.passing_cost = 2


class Grass(Entity):
    def __init__(self):
        super().__init__()


class Rock(Entity):
    def __init__(self):
        super().__init__()
        self.is_passable = False


class Tree(Entity):
    def __init__(self):
        super().__init__()
        self.passing_cost = 2


class Creature(Entity):
    def __init__(self, name, health, speed, power, fov_range):
        super().__init__()
        self.health = health
        self.speed = speed
        self.power = power
        self.fov_range = fov_range
        self.name = name

    def make_move(self):
        pass


class Elf(Creature):
    def __init__(self, name=None, health=100, speed=3, power=5, attack_range=3, fov_range=3):
        super().__init__(name, health, speed, power, fov_range)
        self.attack_range = attack_range

    def make_move(self):
        pass

    def attack(self, target):
        pass


class Vampire(Creature):
    def __init__(self, name=None, health=100, speed=2, power=10, attack_range=1, fov_range=2):
        super().__init__(name, health, speed, power, fov_range)
        self.attack_range = attack_range

    def make_move(self):
        pass

    def attack(self, target):
        pass
