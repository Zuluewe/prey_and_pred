from model import Model
from prey import Prey
from predator import Predator
from toroidalposition import ToroidalPosition

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def make_toroidal_classes(model):
    class ToroidalPrey(Prey):
        position = ToroidalPosition.from_model(model)

    class ToroidalPredator(Predator):
        position = ToroidalPosition.from_model(model)

    return ToroidalPrey, ToroidalPredator

# testing torodial wrap world
def test_toroidal_wrap():
    model = Model(width=10, height=10, seed=1)
    WorldPrey, _ = make_toroidal_classes(model)
    p = WorldPrey(model, uid=0, position=(9,5))
    position = p.position
    p.move_by(1,0)
    assert p.position == (0,5)

# testing that agents die at 0 energy
def test_agent_dies():
    model = Model(5,5,seed=1)
    WorldPrey, _ = make_toroidal_classes(model)
    p = WorldPrey(model, uid=0, energy=1)
    model.step()
    assert len(model.agent) == 0

# testing interaction between pred and prey
def test_pred_eats_prey():
    model = Model(10,10,seed=1)
    TorodialPrey, TorodialPredator = make_toroidal_classes(model)
    prey = TorodialPrey(model, uid=0, position=(1,1), energy=20, hunger=0)
    predator = TorodialPrey(model, uid=0, position=(1,1), energy=20, hunger=4)
    assert prey not in model.agent
    assert predator.energy >15

if __name__ == "__main__":
    test_toroidal_wrap()
    test_agent_dies()
    test_pred_eats_prey()

# if it doesnt print anything it works and if it doesnt world it'll give an error in the terminal.
