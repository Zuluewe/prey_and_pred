# prey_and_pred


## Do it yourself
I skal færdiggøre en lille Agent Based Model med
 - en toroidal 2D verden (wrap-around)
 - en phase-based simulationsmotor:
 1. move
 2. interact
 3. reproduce
 4. cleanup (dead)

I får en fil med: 
- `ToroidalPosition` 
- `Agent` med `move()`, `interact`, `reproduce()` som abstract methods
- `Model` med `step()` der kører faserne
- `Prey` og `Predator` med TODO

**I må ikke ændre engine-strukturen**. I skal implementere de manglende metoder.

### Opgave 1 
- Regler ✓
    - Prey/Predator skal flytte sig i et random 4-nabolag(op/ned/venstre/højre)
    - Prey/Predator mister energi hver tur self.energy -= 1 
    - self.die() hvis energy <= 0
      
- Implementér: ✓
    - Prey.move()
    - Predator.move()

- Test ✓
    - print af antal prey/predator pr.step


### Opgave 2
- Regler: ✓
    - Predator skal kunne spise én prey hvis der står en prey på samme celler.
    - Når prey spises:
        - prey dør (prey.die())
        - predator får energi (fx +10)
          
- Implementér: ✓
    - Predator.interact()
        - finde prey på samme celle (`model.agent_at()`)
        - prey.die() hvis er blevet spist
- hint
```python
agents_here = self.model.agents_at(self.position)
prey_at_position = [a for a in agents_here if isinstance(a, Prey)]
```

### Opgave 3
- Regler ✓
    - Hvis prey/predator har høj energi, eller efter en reproduce_rate, laver den en ny baby.
    - Baby spawn'er ved samme position (eller nabo, hvis i vil)
    - Forælderen mister energi (fx halverer sin energi)
      
- Implementér ✓
    - Prey.reproduce()
    - Predator.reproduce()
      
- hint
```python         
    baby = self.__class__(self.model,
                        uid=self.model.next_uid(),
                        position=self.position,
                        energy=10)
    self.model.add_agent(baby)
    self.energy//=2 
```

### Opgave 4 -- Test 
1. Sikre at `position` altid ligger indenfor Toroidal world 
    - Skriv en lille test i i den samme fil eller lav en ny fil: 
    ```python
    def test_toroidal_wrap():
        model = Model(width=10, height=6, seed=1)
        WorldPrey, _ = make_world_classes(model)
        p = WorldPrey(model, uid=0, position=(9,5))
        p.move_by(1,0)
        assert p.position == (0,5)
    ```
2. Test at døde agents fjernes korrekt.
    ```python
    def test_agent_dies():
        model = Model(5,5,seed=1)
        WorldPrey, _ = make_world_classes(model)

        p = WorldPrey(model, uid=0, energy=1)
        model.step()
        assert len(model.agents) == 0
    ```
    
3. Test interaktion mellem agents (predator spiser prey)
    ```python
    TODO
    assert prey not in model.agents
    assert predator.energy >10
    ```

### Opgave 5 -- Datasamling og statisk plot
1. Gem data over tid
    - antal prey og predator efter hver step
2. Plot populationer over tid

### Animation med matplotlib
1. animer population over tid 
2. (optional) Animer 2D-verdenen. 


## Eksperimenter: Programmering som eksperimentel metode

Formålet med dette eksperiment er at undersøge, om 
- en agentbaseret prey–predator-model kan fremvise oscillationer i populationerne af byttedyr og rovdyr,
- hvordan disse oscillationer afhænger af udvalgte parametre i modellen.
- kobler med matematik

### Hypotese

f.x. højere prey-reproductionsrate vil føre til større populationer af prey (byttedyr), hvilket efterfølgende vil medføre en stigning i populationen af predator (rovedyr). 

### Parametre i eksperiment

Der findes følgende elementer i modellen:
- Verdens størrelse (width og height)
- Startantal af prey og predator
- Regler for bevægelse
- Regler for spisning og reproduction
- Sandsynlighed for tilfældige hændelser

I eksperimentet, ændrer vi kunne **én parameter ad gangen**, fx. prey-reproductionsrate. På denne måde kan vi se hvordan parameter påvirker modellen. 

Da modellen er stokastisk, vil to simulationer med samme parametre ikke nødvendigvis give identiske resultater. For at reducere støj, kan vi også køre simulation flere gange med forskellige `seed`. 

|**Parameter**|**Værdi**|
|:---|:---|
|width|40|
|height|30|
|start number prey|300|
|start number predator|40|
|p_eat|0.8|
|predator energy gain|12|
|energy loss per step|1|
|steps per run|500|
|total runs|30|

### Eksperiment og dataopsamling
|**Variabel**|**Beskrivelse**|
|:-----------|:--------------|
|t| tidsstep|
|P(t)| antal prey|
|Q(t)| antal predator|

### Databehandling
For hver parameteropsætning beregnes middelværdien af P(t) og Q(t) over 30 simulations. Resultaterne visualiseres ved hjælpe af plot. 

### Kobling med andre fag
kan kobles med
- Økosystem stabilitet
- ABM design
- statistic
- Lotka-Volterra ligninger

    $\frac{dP}{dt} = aP-bPQ$

    $\frac{dQ}{dt} = -cQ + dPQ$
