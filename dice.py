from random import randint

class Dice:
    """A class representing a single dice."""

    def __init__(self, num_sides=6):
        """Assuming that a dice is in the shape of a cube."""
        self.num_sides = num_sides
    
    def roll(self):
        """Return a values between 1 and the number of sides the dice have."""
        return randint(1, self.num_sides)
