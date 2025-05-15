import numpy as np
import copy
import random
import math
import models 


class WolfSheep(models.model):
    """Wolf-sheep Predation Model.
    A model for simulating wolf and sheep (predator-prey) ecosystem modelling.
    """

    def __init__(
        self,
        width=5,
        height=5,
        initial_sheep=3,
        initial_wolves=2,
        sheep_reproduce=0.4,
        wolf_reproduce=0.05,
        wolf_gain_from_food=20,
        neighbourhood = "von neumann",
        neighbour_range = 1
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
        super.__init__(height, width)
        self.number_sheep = initial_sheep
        self.number_wolves = initial_wolves
        self.sheep_reproduce = sheep_reproduce
        self.wolf_reproduce = wolf_reproduce
        self.wolf_gain_from_food = wolf_gain_from_food
        self.neighbourhood = neighbourhood
        self.neighbour_range = neighbour_range


    def setup(self):
        #self.grid = np.empty(self.width*self.height, dtype=np.dtype(object))
        #randomize_idx = np.random.permutation(self.width*self.height)
        #self.grid[randomize_idx[0:self.number_sheep]] = agents.Sheep(10, 0.04)
        #self.grid[randomize_idx[self.number_sheep:(self.number_sheep+self.number_wolves)]] = agents.Wolf(20, 0.05)
        #self.grid = self.grid.reshape(self.height, self.width)
    
    def step(self):
        """Execute one step of the model's behavior,
        The rules are taken from https://rf.mokslasplius.lt/agent-based-prey-predator-model/
        Now taking into account the two randomly picked cells, one has to apply the following rules:

        - If one cell is occupied by predator and another by prey, then the prey is eaten. After doing so the predator gives a birth to another predator with a certain probability. The new predator is placed in the former prey's cell.
        - If both cells are occupied by the same type of agent, then nothing happens.
        - If we have a prey cell and empty cell, then prey gives a birth to another prey with a certain probability.
        - If we have a predator cell and empty cell, then predator dies with a certain probability.
        - If after the application of the rules above still nothing has changed and movement of the agent is possible, then the agent moves from one cell to another unoccupied cell.
        """
        i = random.randrange(0, self.width-1)
        j = random.randrange(0, self.height-1)
        
        von_neumann_neighbour_list = lambda x, y, d:[(x+i, y+j) for i in range(-d, d+1) for j in
                                   range(abs(i)-d, d+1-abs(i))]

        neighbour_idx_list = von_neumann_neighbour_list(i, j, 1)
        random_neighbour_idx = neighbour_idx_list[np.random.choice(len(neighbour_idx_list), 1)[0]]
        if isinstance(self.grid[i][j], agents.Sheep):
            # Prey: 
            #    - if neighbour is empty, give birth at a certain chance
            #    - if not given birth, move to the empty cell
            if self.grid[random_neighbour_idx] == None:
                offspring = self.grid[i][j].spawn_offspring()
                if offspring:
                    self.grid[random_neighbour_idx] = offspring
                else:
                    self.grid[random_neighbour_idx] = copy.deepcopy(self.grid[i][j])
                    #del self.grid[i][j]
                    self.grid[i][j] = None
        elif isinstance(self.grid[i][j], agents.Wolf):
            # Predator: 
            #   - if neighbour is empty, die at a certain chance
            #   - if the neighbour is another predator, nothing
            #   happened
            #   - if the neighbour is a prey, eat the prey and give birth if possible
            if self.grid[random_neighbour_idx] == None:
                if random.random()<0.02:
                    # del self.grid[random_neighbour_idx]
                    self.grid[i][j] = None
            elif isinstance(self.grid[random_neighbour_idx], agents.Sheep):
                self.grid[random_neighbour_idx] = None
                offspring =  self.grid[i][j].spawn_offspring()
                if offspring:
                    self.grid[random_neighbour_idx] = offspring
                else:
                    self.grid[random_neighbour_idx] = copy.deepcopy(self.grid[i][j])
                    self.grid[i][j] = None
            






