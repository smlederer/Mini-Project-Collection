# Dice Simulator with Custom Dice

Using Monte Carlo simulations, find the distributions of non-standard dice. 

Originally built to prototype dice for a board game idea, but can be generalized. For this simulation, the faces are different colors (Blue, Red, Green) or Blank spaces. The general idea would be the colors refering to a resource whie the blank is no resource. 

### Initial Parameters

* Minor blue/red/green = [3 B/R/G Mana, 3 Blank]
* Greater blue/red/green = [5 B/R/G Mana, 3 Blank]
* Minor Wild = [G,R,B, 3 Blank]
* Greater Wild = [2 G, 2 R, 2 B]
* Curse Dice = [6 Blank]

These are initialized inthe code attached:

```{r initialize}
#Dice Types
mb = c('b','b','b','x','x','x')
mr = c('r','r','r','x','x','x')
mg = c('g','g','g','x','x','x')
gb = c('b','b','b','b','b','x')
gr = c('r','r','r','r','r','x')
gg = c('g','g','g','g','g','x')
wd = c('g','b','r','x','x','x')
gw = c('g','b','r','g','b','r')
cd = c('x','x','x','x','x','x')
```

Dice size can be inter-changeable, but standard 6 sided dice used with unique faces. 

You choose the dice that you want to roll with the initial parameters by calling them based on stings of the initialized dice:

```{r choose}
#contains the dice that you are rolling 
d = c('wd','wd','gw','gr')
```
The code will then run the simulation of total resources (faces that are a result of rolling the selected dice) that are a result of rolling these dice. 

### Example Result

Example data frame result:

|X1|X2|X3|X4|total|red|blue|green|na|totalM|
|--|--|--|--|-----|---|----|-----|--|------|
| x| x| b| r|brxx |  1|   1|    0| 0|     2|
| r| r| b| r|brrr |  3|   1|    0| 0|     4|
|r|x|b|r|brrx|2|1|0|1|3|
|...|...|...|...|...|...|...|...|...|...|

Example plot of the red resource generated:

![exampleoutput](https://imgur.com/k3NtnGK.jpg)

Allow for simple understanding of the current dice set up and what is expected in resource generation. 

### Application

Determine the expected result of certain rolls (mode specifically) to determine the abundance of resources at different numbers of dice. 

Allows for naive prototyping of mechanics that are reliant on rolling dice and with the advent of easy developement of custom dice, begins to poke into the design space of using custom dice as opposed to standard 6 sided dice. 

### Future Plans
* Shiny app 
    * Allow users defined 6-sided dice faces
    * Allow users to choose number of each user defined dice
