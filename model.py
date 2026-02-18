import random

class Model:
    def __init__(self, width, height, seed=None):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive!")
        self.width = width
        self.height = height
        self.rng = random.Random(seed)
        self.agent = []
        self.time = 0
        self._next_uid = 0
    
    def random_position(self):
        return (self.rng.randrange(self.width), self.rng.randrange(self.height))
    
    def add_agent(self, agent):
        self.agent.append(agent)

    def remove_agent(self, agent):
        self.agent.remove(agent)

    def agent_at(self, pos):
        return [agent for agent in self.agent if agent.position == pos]

    def next_uid(self):
        uid = self._next_uid
        self._next_uid +=1
        return uid 

    def step(self):
        """
        Random sequence for fairness
        
        """ 

        self.rng.shuffle(self.agent)
        for agent in self.agent:
            if agent.alive:
                agent.move()
                agent.interact()
                agent.reproduce()

        self.agent = [agent for agent in self.agent if agent.alive]
        
        self.time += 1
        
    def run(self, steps:int):
        for _ in range(steps):
            self.step()