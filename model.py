import numpy as np
import random
import math
import agents 

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

        self.height = height
        self.width = width
        self.number_sheep = initial_sheep
        self.number_wolves = initial_wolves
        #self.sheep_reproduce = sheep_reproduce
        #self.wolf_reproduce = wolf_reproduce
        #self.wolf_gain_from_food


    def setup(self):
        self.grid = np.empty(self.width*self.height, dtype=np.dtype(object))
        randomize_idx = np.random.permutation(self.width*self.height)
        self.grid[randomize_idx[0:self.number_sheep]] = agents.Sheep(10, 0.04)
        self.grid[randomize_idx[self.number_sheep:(self.number_sheep+self.number_wolves)]] = agents.Wolf(20, 0.05)
        self.grid = self.grid.reshape(self.height, self.width)

