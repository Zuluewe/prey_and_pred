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

if __name__ == "__main__":
    model = Model(width=10, height=10, seed=2)
    ToroidalPrey, ToroidalPredator = make_toroidal_classes(model)

    prey_start = 25 # prey
    for _ in range(prey_start):
        model.add_agent(ToroidalPrey(model, uid=model.next_uid))

    pred_start = 10 # pred
    for _ in range(pred_start):
        model.add_agent(ToroidalPredator(model, uid=model.next_uid))

    # historical data to make graph
    time_steps = []
    prey_counts = []
    pred_counts = []

    model_time = 200 # time
    for _ in range(model_time):
        prey_count = sum(isinstance(a, ToroidalPrey) for a in model.agent)
        pred_count = sum(isinstance(a, ToroidalPredator) for a in model.agent)
        
        time_steps.append(model.time)
        prey_counts.append(prey_count)
        pred_counts.append(pred_count)
        
        print(f"t={model.time}, sheep = {prey_count}, wolf = {pred_count}")
        model.step()

# Visulization in matplotlib (scatterplot)
    fig, ax = plt.subplots()
    
    def update(frame):
        x = np.array(time_steps[:frame])
        y_prey = np.array(prey_counts[:frame])
        y_pred = np.array(pred_counts[:frame])

        # update scatter plot data for predator
        data_pred = np.stack([x, y_pred]).T
        scat_pred.set_offsets(data_pred)
        
        # update scatter plot data for prey
        data_prey = np.stack([x, y_prey]).T
        scat_prey.set_offsets(data_prey)
        
        return (scat_pred, scat_prey)
    
    # Plotting the data
    scat_pred = ax.scatter([], [], c="r", s=5, label='Predator')
    scat_prey = ax.scatter([], [], c="b", s=5, label='Prey')
    
    # Titels
    ax.set_title("Graph over predator and prey population over time")
    ax.set(xlim=[0, model_time], ylim=[0, prey_start + 25], xlabel='Time [t]', ylabel='Population')
    ax.legend()
    
    ani = FuncAnimation(fig, update, frames=len(time_steps), interval=50, blit=True)
    plt.show()

