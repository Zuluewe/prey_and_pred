import numpy as np
from matplotlib import pyplot as plt, animation
from pred_prey_model import World

def run_app():
    model = World(200)

    fig, ax = plt.subplots()
    ax.set_xlim(0, model.world_size)
    ax.set_ylim(0, model.world_size)
    ax.set_aspect("equal")

    prey_scatter = ax.scatter([], [], s=20, c="blue")
    pred_scatter = ax.scatter([], [], s=40, c="red", marker="^")
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update(frame):
        model.step()

        prey_pos = np.array([[s.x, s.y] for s in model.sheep])
        pred_pos = np.array([[w.x, w.y] for w in model.wolves])

        prey_scatter.set_offsets(prey_pos)
        pred_scatter.set_offsets(pred_pos)

        text.set_text(f"t={model.time}  prey={len(model.sheep)} preds={len(model.wolves)}")
        return prey_scatter, pred_scatter, text

    ani = animation.FuncAnimation(fig,
                                  update,
                                  interval=300,
                                  blit=False,
                                  cache_frame_data=False,
                                  )
    plt.show()

if __name__ == "__main__":
    run_app()