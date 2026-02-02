from agent import Agent
from model import Model
import random

class Prey(Agent):
    def __init__(self, 
                 model, 
                 uid, 
                 position = None, 
                 energy: int = 25,
                 hunger: int = 0):
        
        super().__init__(model, uid, position)
        self.energy = energy
        self.hunger = hunger

    def move(self):
        if self.energy > 0:
            self.random_walk()
            self.energy -= 1
            self.hunger += 1

        if self.energy <= 0:
            self.die()
    
    def interact(self):
        if self.hunger > 1 and self.model.rng.randint(1,100) > 50:
            self.energy += 10
            self.hunger = 0


    def reproduce(self):
        REPRODUCE_THRESHOLD = 27
        random_number = self.model.rng.randint(1,100)

        if self.energy >= REPRODUCE_THRESHOLD and random_number < 25:
            baby = self.__class__(self.model,
                                  uid = self.model.next_uid(),
                                  position = self.position,
                                  energy = 15)
            self.model.add_agent(baby)
            self.energy //= 2