import random

class Agent():
    """The base agent class"""
    def __init__(self, energy:int, p_reproduce:int, cell=None):
        """Initialize an agent.
        Args:
            energy: Starting amount of energy
            p_reproduce: Probability of reproduction
            cell: Cell in which the animal starts 
        """
        self.energy = energy
        self.p_reproduce = p_reproduce
        self.cell = cell
    
    def feed(self):
        pass

    def spawn_offspring(self):
        """Create offspring by splitting energy and creating new instance."""
        self.energy /=2
        self.__class__(
            self.energy,
            self.p_reproduce,
            self.cell)
    def move(self):
        """Find a random neighboring cell and move there"""
        pass
    def remove(self):
        """The agent is removed (dead) from the model"""
        pass
    def step(self):
        """Execute one step of the animal's behavior."""
        self.move()
        self.energy -= 1
        # Try to feed 
        self.feed()
        # Handle death and reproduction
        if self.energy < 0:
            self.remove()
        elif random.random()< self.p_reproduce:
            self.spawn_offspring()

class Sheep(Agent):
    def move(self):



class Wolf(Agent):
    def feed(self):
        """If possible, eat a sheep at current location."""
        pass
    def move(self):
        pass


