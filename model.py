import numpy as np
import random
import math

class WolfSheep():
    """Wolf-sheep Predation Model.
    A model for simulating wolf and sheep (predator-prey) ecosystem modelling.
    """

    def __init__(
        self,
        width=20,
        height=20,
        initial_sheep=100,
        initial_wolves=50,
        sheep_reproduce=0.04,
        wolf_reproduce=0.05,
        wolf_gain_from_food=20,
    ):
        """Create a wolf-Sheep model with the given parameters.

        Args:
            height: Height of the grid
            width: Width of the grid
            initial_sheep: Number of sheep to start with
            initial_wolves: Number of wolves to start with
            sheep_reproduce: Probability of each sheep reproducing each step
            wolf_reproduce: probability of each wolf reproducing each step
            wolf_gain_from_food: Energy a wolf gains from eatinga sheep
        """

    
