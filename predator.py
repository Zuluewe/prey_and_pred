from agent import Agent
from model import Model
from prey import Prey
import random

class Predator(Agent):

    def __init__(self,
                 model,
                 uid,
                 position=None,
                 energy: int = 10):
        super().__init__(model, uid, position)
        self.energy = energy
        
    def move(self) -> None:
        if self.energy > 0:
            self.random_walk()
            self.energy -= 1

        if self.energy <= 0:
            self.die()

    def interact(self):
        prey_here = self.model.agent_at(self.position)
        for agent in prey_here:
            if isinstance(agent, Prey) and agent.alive:
                agent.die()
                self.energy += 10
                return

    def reproduce(self):
        REPRODUCE_THRESHOLD = 30
        random_number = self.model.rng.randint(1,100)

        if self.energy >= REPRODUCE_THRESHOLD and random_number < 15:
            baby = self.__class__(self.model,
                                  uid = self.model.next_uid(),
                                  position = self.position,
                                  energy = 20)
            self.model.add_agent(baby)
            self.energy //= 2