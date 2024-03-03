# Caleb Potts
# 03/03/2024

# Setup Code
# Expected Task: Create a base class `MagicalCreature` and subclasses `Dragon`, `Unicorn`. Each subclass should have a unique `sound` method.


class MagicalCreature:
    def sound(self):
        return "Whoosh!"


class Dragon(MagicalCreature):
    def sound(self):
        return "Roar!"


class Unicorn(MagicalCreature):
    def sound(self):
        return "Neigh!"


dragon = Dragon()
print(dragon.sound())

unicorn = Unicorn()
print(unicorn.sound())
