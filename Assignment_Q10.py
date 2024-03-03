# Caleb Potts
# 03/03/2024

# Setup Code
# Expected Task: Implement a class with methods for casting spells, reducing health points, and determining the winner.


class Wizard:
    def __init__(self, name, health_points=100):
        self.name = name
        self.health_points = health_points

    def cast_spell(self, opponent, damage):
        print(f"{self.name} casts a spell on {opponent.name}!")
        opponent.reduce_health(damage)

    def reduce_health(self, damage):
        self.health_points -= damage
        print(f"{self.name} loses {damage} health points.")
        if self.health_points <= 0:
            print(f"{self.name} has been defeated!")

    @staticmethod
    def determine_winner(wizard1, wizard2):
        if wizard1.health_points <= 0:
            return f"After a duel between {wizard1.name} and {wizard2.name}, {wizard2.name} wins with {wizard2.health_points} health points left."
        elif wizard2.health_points <= 0:
            return f"After a duel between {wizard1.name} and {wizard2.name}, {wizard1.name} wins with {wizard1.health_points} health points left."
        else:
            return "The battle continues..."


wizard1 = Wizard("Harry")
wizard2 = Wizard("Draco")

while True:
    wizard1.cast_spell(wizard2, 10)
    if wizard2.health_points <= 0:
        break
    wizard2.cast_spell(wizard1, 10)
    if wizard1.health_points <= 0:
        break

print(Wizard.determine_winner(wizard1, wizard2))
