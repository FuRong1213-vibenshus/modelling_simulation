import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors 
from agents import Sheep, Wolf
from model import WolfSheep
class App():
    def __init__(self, model):
        self.model = model

    def __map(self, obj):
        if isinstance(obj, Sheep): 
            val = 1
        elif isinstance(obj,Wolf):
            val = 2
        else:
            val = 0

    def display_grid(self):
       cmap = colors.ListedColormap(['green', 'blue', 'red'])
       map_class_to_color = np.vectorize(self.__map)
       normed_grid = map_class_to_color(self.model.grid)
       bounds = [0, 1, 2]
       norm = colors.BoundaryNorm(bounds, cmap.N)

       fix, ax = plt.subplots()
       ax.imshow(normed_grid, cmap=cmap, norm=norm)
       ax.grid(which='major', axis='both', linestyle='-', color='k',
               linewidth=2)

    def run(self):
        self.model.setup()
        self.display_grid()



model = WolfSheep(5, 5, 4, 2)

app = App(model)
app.run()
