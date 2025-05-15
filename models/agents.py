import random

class Agent():
    """The base agent class"""
    def __init__(self, energy, p_reproduce, model):
        """Initialize an agent.
        Args:
            energy: Starting amount of energy
            p_reproduce: Probability of reproduction
            cell: Cell in which the animal starts 
        """
        self.energy = energy
        self.p_reproduce = p_reproduce
        self.model = model

    def agents_nearby(self):
        pass 
    
    def current_cell():
        """Returns the cell that the agent is currently standing on, based on its
        coordinates.
        """
        pass 

    def destroy():
        pass

    def jump_to(self, x, y):
        """ Move the agent to a specified point.
        Args:
            x - Destination x-coordinate
            y - Destination y-coordinate """
        pass

    def feed(self):
        pass

    def spawn_offspring(self):
        """Create offspring by splitting energy and creating new instance."""
        if random.random()< self.p_reproduce:
            self.energy /=2
            return self.__class__(self.energy, self.p_reproduce)
        else: 
            return None

    def move(self):
        """Find a random neighboring cell and move there"""
        pass
    def remove(self):
        """The agent is removed (dead) from the model"""
        pass
    def step(self):
        """Execute one step of the animal's behavior."""

class Sheep(Agent):

    def step(self):
        self.move()
        # self.energy -= 1
        # Try to feed 
        self.feed()
        # Handle death and reproduction
        if self.energy < 0:
            self.remove()
        elif random.random()< self.p_reproduce:
            self.spawn_offspring()
    
    def move(self):
        pass


class Wolf(Agent):
    def feed(self):
        """If possible, eat a sheep at current location."""
        pass
    def step(self):
        self.move()
        self.energy -= 1
        # Try to feed 
        self.feed()
        # Handle death and reproduction
        if self.energy < 0:
            self.remove()
        elif random.random()< self.p_reproduce:
            self.spawn_offspring()

    def move(self):
        pass


