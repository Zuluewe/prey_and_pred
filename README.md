# prey_and_pred

I min "Predator and Prey" simulation har jeg løst de krevede opgaver (som kan læses under), samt har jeg tilføjet følgende:

- Variable: hunger

Er løst i filerne: [prey.py](https://github.com/Zuluewe/prey_and_pred/blob/main/prey.py) og [predator.py](https://github.com/Zuluewe/prey_and_pred/blob/main/predator.py)

Dette variable er for at sikre at ulve og får ikke spiser konstant så deres energi stiger eksponentielt.
 
- Interact til prey

Er løst i filerne: [prey.py]([https://example.com](https://github.com/Zuluewe/prey_and_pred/blob/main/prey.py))

Jeg defineret interact funktionen for prey så de kan få energi og reproduce.

## Opgaver
### Opgave 1 
Er løst i filerne: [prey.py](https://github.com/Zuluewe/prey_and_pred/blob/main/prey.py) og [predator.py](https://github.com/Zuluewe/prey_and_pred/blob/main/predator.py)
- Regler ✓
    - ~~Prey/Predator skal flytte sig i et random 4-nabolag(op/ned/venstre/højre)~~
    - ~~Prey/Predator mister energi hver tur self.energy -= 1~~
    - ~~self.die() hvis energy <= 0~~
      
- Implementér: ✓
    - ~~Prey.move()~~
    - ~~Predator.move()~~

- Test ✓
    - ~~print af antal prey/predator pr.step~~

### Opgave 2
Er løst i filerne: [predator.py](https://github.com/Zuluewe/prey_and_pred/blob/main/predator.py)
- Regler: ✓
    - ~~Predator skal kunne spise én prey hvis der står en prey på samme celler.~~
    - ~~Når prey spises:~~
        - ~~prey dør (prey.die())~~
        - ~~predator får energi (fx +10)~~
          
- Implementér: ✓
    - ~~Predator.interact()~~
        - ~~finde prey på samme celle (`model.agent_at()`)~~
        - ~~prey.die() hvis er blevet spist~~

### Opgave 3
Er løst i filerne: [prey.py](https://github.com/Zuluewe/prey_and_pred/blob/main/prey.py) og [predator.py](https://github.com/Zuluewe/prey_and_pred/blob/main/predator.py)
- Regler ✓
    - ~~Hvis prey/predator har høj energi, eller efter en reproduce_rate, laver den en ny baby.~~
    - ~~Baby spawn'er ved samme position (eller nabo, hvis i vil)~~
    - ~~Forælderen mister energi (fx halverer sin energi)~~
      
- Implementér ✓
    - ~~Prey.reproduce()~~
    - ~~Predator.reproduce()~~

### Opgave 4
Er løst i filerne: [test.py](https://github.com/Zuluewe/prey_and_pred/blob/main/test.py)
- Test ✓
   - ~~Sikre at `position` altid ligger indenfor Toroidal world.~~
   - ~~Test at døde agents fjernes korrekt.~~
   - ~~Test interaktion mellem agents (predator spiser prey).~~


### Opgave 5 
Er løst i filerne: [run.py](https://github.com/Zuluewe/prey_and_pred/blob/main/run.py)
- Datasamling ✓
    - ~~Gem data over tid~~
    - ~~antal prey og predator efter hver step~~
    - ~~Plot populationer over tid~~ 

- Animation med matplotlib ✓
  - ~~animer population over tid~~ 
  - (optional) Animer 2D-verdenen. 
