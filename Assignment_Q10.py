# Caleb Potts
# 02/03/2024

# Setup Code
# Expected Task: Implement a class with methods for casting spells, reducing health points, and determining the winner.


class Wizard:
    def __init__(self, name, health_points=100):
        self.name = name
        self.health_points = health_points

    def cast_spell(self, opponent, damage):
        print(f"{self.name} casts a spell on {opponent.name}!")
        # Reduce opponent's health points
        opponent.reduce_health(damage)

    def reduce_health(self, damage):
        self.health_points -= damage
        print(f"{self.name} loses {damage} health points.")
        if self.health_points <= 0:
            print(f"{self.name} has been defeated!")

    @staticmethod
    def determine_winner(wizard1, wizard2):
        if wizard1.health_points <= 0:
            return f"{wizard2.name} wins!"
        elif wizard2.health_points <= 0:
            return f"{wizard1.name} wins!"
        else:
            return "The battle continues..."


# Example usage
wizard1 = Wizard("Voldemort")
wizard2 = Wizard("Harry Potter")

while True:
    wizard1.cast_spell(wizard2, 15)
    if wizard2.health_points <= 0:
        break
    wizard2.cast_spell(wizard1, 20)
    if wizard1.health_points <= 0:
        break

print(Wizard.determine_winner(wizard1, wizard2))
