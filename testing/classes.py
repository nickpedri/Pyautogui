class Food:

    def __init__(self, name, color, hp_regen):
        self.name = name
        self.color = color
        self.hp_regen = hp_regen


class Items:

    def __init__(self, name):
        self.name = name


class Character:

    def __init__(self, name, hp, dmg, speed, defense, items=[], alive=True):
        """ This function initializes a class/object with the attribute values passed in the arguments. """
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.speed = speed
        self.defense = defense
        self.alive = alive
        self.items = items
        if self.hp <= 1:
            self.alive = False

    def attack(self, target):
        dmg_dealt = self.dmg - target.defense
        target.hp -= dmg_dealt
        if target.hp <= 1:
            target.alive = False
        print(f'{self.name} attacks {target.name}, dealing {dmg_dealt} damage!')

    def eat(self, food):
        print(f'{self.name} eats {food.name}, healing {food.hp_regen} hp!')

    def drink_speed_potion(self):
        self.speed = self.speed * 1.5
        print(f'{self.name} drinks speed potion, increasing speed!')


def check_status(character):
    if character.alive:
        status = 'alive'
    else:
        status = 'dead :('
    print(f'{character.name} has {character.hp} health, and is {status}')


banana = Food('banana', 'yellow', 15)
strawberry = Food('strawberry', 'red', 10)
ninja = Character('Ninja', 60, 40, 50, 10)
warrior = Character('Warrior', 100, 30, 30, 15)


def testing():
    ninja.attack()
    warrior.attack()
    ninja.eat(banana)
    warrior.eat(strawberry)
    print(ninja.speed)
    ninja.drink_speed_potion()
    print(ninja.speed)


check_status(ninja)
warrior.attack(ninja)
warrior.attack(ninja)
warrior.attack(ninja)
check_status(ninja)

