import numpy as np
import copy
import random
import math
from model import Model
from prey import Prey 
from predator import Predator


class World(Model): 
    """Wolf-sheep Predation Model.
    A model for simulating wolf and sheep (predator-prey) ecosystem modelling.
    """

    def __init__(
        self,
        world_size,
        n_sheep=25,
        n_wolves=10,
        sheep_reproduce=0.18,
        wolf_reproduce=0.35,
        wolf_gain_from_food=10,
    ):
        """Create a wolf-Sheep model with the given parameters.

        Args:
            n_sheep: Number of sheep to start with
            n_wolves: Number of wolves to start with
            sheep_reproduce: Probability of each sheep reproducing each step
            wolf_reproduce: probability of each wolf reproducing each step
            wolf_gain_from_food: Energy a wolf gains from eating a sheep
        """
        # initialize rectangular world (width, height)
        super().__init__(world_size, world_size)
        # keep a convenient square-world size for plotting/np calls
        self.world_size = world_size
        self.time = 0
        self.sheep = []
        self.wolves = []
        self.new_sheep = []
        self.new_wolves = []
        self.sheep_to_remove = []
        self.wolves_to_remove = []


        # Populate world using the agent framework from `model.py`.
        for _ in range(n_sheep):
            pos = self.random_position()
            prey = Prey(self,
                        uid=self.next_uid(),
                        position=pos,
                        energy=20,
                        hunger=0)
            self.sheep.append(prey)
            self.add_agent(prey)

        for _ in range(n_wolves):
            pos = self.random_position()
            wolf = Predator(self,
                            uid=self.next_uid(),
                            position=pos,
                            energy=25,
                            hunger=0)
            self.wolves.append(wolf)
            self.add_agent(wolf)


        self.sheep_reproduce = sheep_reproduce
        self.wolf_reproduce = wolf_reproduce
        self.wolf_gain_from_food = wolf_gain_from_food


    def setup(self):
        # Add newborns, remove the dead
        pass

    def step(self):
        """
        Add newborns, remove the dead,

        """
        # Use the base Model stepping to run each agent's move/interact/reproduce
        super().step()

        # refresh sheep/wolves lists from the global agent list
        self.sheep = [a for a in self.agent if isinstance(a, Prey) and a.alive]
        self.wolves = [a for a in self.agent if isinstance(a, Predator) and a.alive]