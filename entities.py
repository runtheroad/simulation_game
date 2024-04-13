class Entity:

    def __init__(self):
        pass


class Grass(Entity):
    def __init__(self):
        super().__init__()
        self.is_passable = True


class Rock(Entity):
    def __init__(self):
        super().__init__()
        self.is_passable = False


class Tree(Entity):
    def __init__(self):
        super().__init__()
        self.is_passable = False


class Creature(Entity):
    def __init__(self, health, speed, power):
        super().__init__()
        self.health = health
        self.speed = speed
        self.power = power

    def make_move(self):
        pass


class Elf(Creature):
    def __init__(self, name, health, speed, power):
        super().__init__(health, speed, power)
        self.name = name

    def make_move(self):
        pass

    def attack(self, target):
        pass


class Vampire(Creature):
    def __init__(self, name, health, speed, power):
        super().__init__(health, speed, power)
        self.name = name

    def make_move(self):
        pass

    def attack(self, target):
        pass
