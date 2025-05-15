import numpy

class Cell():
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        self.agents = [] 

    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)

    def is_empty(self):
        return len(self.agents) == 0

    def get_neighbour(self):
        pass 


