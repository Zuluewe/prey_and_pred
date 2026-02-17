# prey_and_pred
[![ENG](https://img.shields.io/badge/language-ENG-red)](https://github.com/Zuluewe/prey_and_pred/blob/main/README.eng.md)
[![DK](https://img.shields.io/badge/language-DK-blue)](https://github.com/Zuluewe/prey_and_pred/edit/main/README.md)

In a prey and predator simulation, you want to obtain the result of two graphs that depict the Lotka-Volterra equations. This is because the graphs depict two systems that influence each other in a competitive relationship, which in our context is the competition between predators and prey in a defined biological context.
- Lotka-Volterra equations are defined as follows:

    $\frac{dx}{dt} = kx-axy$

    $\frac{dy}{dt} = bxy - hy$

Equation 1 corresponds to the number of prey animals x at time t. The first term kx expresses the exponential growth of prey animals, which is composed of the birth and death of individuals. The second term, -axy, represents the predators' killing of prey, which is assumed to be proportional to the number of prey times the number of predators.

Equation 2 corresponds to the number of predators y at time t. The first term bxy represents the growth of predators as they consume prey animals. The last term -hy represents the other growth and death of predators depending on other conditions.

![image](assets/ideal_graph.png)

In this coordinate system the x-axes is time and the y-axes is the population number. The blue line represents prey while the red is predators.

## Additions
In my “Predator and Prey” simulation, I have solved the required tasks (which can be read below), and I have added the following:

- Variable: hunger

Solved in the file: [prey.py](https://github.com/Zuluewe/prey_and_pred/blob/main/prey.py) and [predator.py](https://github.com/Zuluewe/prey_and_pred/blob/main/predator.py)

This variable is to insure that the wolved and sheep dont eat constantly so their energy grows exponentially.

 
- Interact for prey

Solved in the file:  [prey.py]([https://example.com](https://github.com/Zuluewe/prey_and_pred/blob/main/prey.py))

I defined the interact funktionen for prey so they can increase their energi og reproduce.

## Tasks
### Task 1 
Solved in the file: [prey.py](https://github.com/Zuluewe/prey_and_pred/blob/main/prey.py) and [predator.py](https://github.com/Zuluewe/prey_and_pred/blob/main/predator.py)
- Rules ✓
    - ~~Prey/Predator must move in a random 4-neighborhood (up/down/left/right)~~
    - ~~Prey/Predator loses energy each turn self.energy -= 1~~
    - ~~self.die() if energy <= 0~~
      
- Implements: ✓
    - ~~Prey.move()~~
    - ~~Predator.move()~~

- Test ✓
    - ~~print the amount of prey/predator pr.step~~

### task 2
Solved in the file: [predator.py](https://github.com/Zuluewe/prey_and_pred/blob/main/predator.py)
- Rules: ✓
  - ~~Predator must be able to eat one prey if there is prey on the same cell.~~
  - ~~When prey is eaten:~~
        - ~~prey dies (prey.die())~~
        - ~~predator gains energy (e.g. +10)~~
- Implements: ✓
    - ~~Predator.interact()~~
        - ~~find prey on the same cell (`model.agent_at()`)~~
        - ~~prey.die() if eaten~~

### Task 3
Solved in the file: [prey.py](https://github.com/Zuluewe/prey_and_pred/blob/main/prey.py) og [predator.py](https://github.com/Zuluewe/prey_and_pred/blob/main/predator.py)
- Rules ✓
    - ~~If prey/predator has high energy, or after a reproduce_rate, it creates a new baby.~~
    - ~~Baby spawns at the same position (or neighbor, if you want)~~
    - ~~The parent loses energy (e.g., halves its energy)~~
      
- Implements ✓
    - ~~Prey.reproduce()~~
    - ~~Predator.reproduce()~~

### Task 4
Solved in the file: [test.py](https://github.com/Zuluewe/prey_and_pred/blob/main/test.py)
- Test ✓
   - ~~Ensure that `position` always lies within the Toroidal world.~~
   - ~~Test that dead agents are removed correctly.~~
   - ~~Test interaction between agents (predators eating prey).~~


### Task 5 
Solved in the file: [run.py](https://github.com/Zuluewe/prey_and_pred/blob/main/run.py)
- Data collection ✓
    - ~~Save data over time~~
    - ~~Amount of prey og predator after every step~~
    - ~~Plot population over time~~ 

- Animation with matplotlib ✓
  - ~~Animate the population over time~~ 
  - (optional) Animate a 2D-world. 
