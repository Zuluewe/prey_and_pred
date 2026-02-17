from agent import Agent
from model import Model
from prey import Prey
import random

class Predator(Agent):
    def __init__(self,
                 model,
                 uid,
                 position=None,
                 energy: int = 15,
                 hunger: int = 0):
        super().__init__(model, uid, position)
        self.energy = energy
        self.hunger = hunger
        
    def move(self): # When the prey moves it loses 1 energy and gains 1 hunger
        if self.energy > 0:
            self.random_walk()
            self.energy -= 1
            self.hunger += 1

        if self.energy <= 0:
            self.die()

    def interact(self):
        prey_here = self.model.agent_at(self.position)
        for agent in prey_here:
            if isinstance(agent, Prey) and agent.alive and self.hunger > 3: # if the there is a live prey in same box that and predator is hungry enough it will eat
                agent.die()
                self.energy += 10 # prey gains 10 energy when it eats
                self.hunger = 0 # and hunger resets to 0

    def reproduce(self):
        REPRODUCE_THRESHOLD = 30 # need 30 energy to reproduce
        random_number = self.model.rng.randint(1,100)

        if self.energy >= REPRODUCE_THRESHOLD and random_number < 82 and self.hunger <= 1: # has 82% chance to reproduce
            baby = self.__class__(self.model,
                                  uid = self.model.next_uid(),
                                  position = self.position,
                                  energy = 20,
                                  hunger = 0)
            self.model.add_agent(baby)
            self.energy //= 2 # pred loses half its energy when reproducing
            self.hunger += 2 # and gain two hunger