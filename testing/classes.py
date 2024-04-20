class Food:

    def __init__(self, name, color, hp_regen):
        self.name = name
        self.color = color
        self.hp_regen = hp_regen


class Character:

    def __init__(self, name, hp, dmg, speed):
        """ This function initializes a class/object with the attribute values passed in the arguments. """
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.speed = speed

    def attack(self):
        print(f'{self.name} attacks, dealing {self.dmg} damage!')

    def eat(self, food):
        print(f'{self.name} eats {food.name}, healing {food.hp_regen} hp!')

    def drink_speed_potion(self):
        self.speed = self.speed * 1.5
        print(f'{self.name} drinks speed potion, increasing speed!')


banana = Food('banana', 'yellow', 15)
strawberry = Food('strawberry', 'red', 10)
ninja = Character('Ninja', 70, 40, 50)
warrior = Character('Warrior', 100, 40, 30)


def combat_and_eat():
    ninja.attack()
    warrior.attack()
    ninja.eat(banana)
    warrior.eat(strawberry)


print(ninja.speed)
ninja.drink_speed_potion()
print(ninja.speed)

combat_and_eat()