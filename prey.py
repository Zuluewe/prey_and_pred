from agent import Agent
from model import Model
import random

class Prey(Agent):
    def __init__(self, 
                 model, 
                 uid, 
                 position = None, 
                 energy: int = 20,
                 hunger: int = 0):
        
        super().__init__(model, uid, position)
        self.energy = energy
        self.hunger = hunger

    def move(self): # When the prey moves it loses 1 energy and gains 1 hunger
        if self.energy > 0:
            self.random_walk()
            self.energy -= 1
            self.hunger += 1

        if self.energy <= 0: # When the prey has 0 energy it dies
            self.die()

    def move_by(self, dx, dy): # to test torodial wrap
        x, y = self.position
        new_position = (x+dx, y+dy)
        self.position = new_position
        return new_position
    
    def interact(self):
        if self.hunger > 3 and self.model.rng.randint(1,100) < 50: # if the prey is hungry enough it has a 50% chance to eat
            self.energy += 10 # prey gains 10 energy when it eats
            self.hunger = 0 # and hunger resets to 0


    def reproduce(self):
        REPRODUCE_THRESHOLD = 27 # need 27 energy to reproduce
        random_number = self.model.rng.randint(1,100)

        if self.energy >= REPRODUCE_THRESHOLD and random_number < 65: # if it has 27 energy it has a 65% chance to reproduce
            baby = self.__class__(self.model,
                                  uid = self.model.next_uid(),
                                  position = self.position,
                                  energy = 15,
                                  hunger = 0)
            self.model.add_agent(baby) 
            self.energy //= 2 # prey loses half its energy when reproducing
            self.hunger += 1 # and gain one hunger