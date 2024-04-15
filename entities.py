class Entity:

    def __init__(self):
        self.is_passable = True
        self.passing_cost = 1

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
    def __init__(self, health, speed, power):
        super().__init__()
        self.health = health
        self.speed = speed
        self.power = power


    def make_move(self):
        pass


class Elf(Creature):
    def __init__(self, name, health=100, speed=3, power=5, attack_range=3):
        super().__init__(health, speed, power)
        self.name = name
        self.attack_range = attack_range

    def make_move(self):
        pass

    def attack(self, target):
        pass


class Vampire(Creature):
    def __init__(self, name, health=100, speed=2, power=10, attack_range=1):
        super().__init__(health, speed, power)
        self.name = name
        self.attack_range = attack_range


    def make_move(self):
        pass

    def attack(self, target):
        pass
