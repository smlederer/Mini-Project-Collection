# Loop Hero River Placement Simulation
Created March 2021

[Loop Hero](https://store.steampowered.com/app/1282730/Loop_Hero/) is a game where placing buildings and scenery affects battle and stats of your character. Placement is important and leads to optimizations made while playing the game. One optimization revolves around the River tile that gives all adjacent tiles 2x value and can stack with other Rivers that are adjacent to the same tile.

Some behaviors of rivers are as follows:
* Only have a degree of 2 (in and out, can't fork).
* Must start at the edge of the map.

### Current Implementation

Currently a random walk across a n x m matrix till the step limit of the river is met or there is no longer a possible move for a river to be placed. After, the total value is calculated treating every space in the area as a base value of 2 (this is usually the value of one of the cards used with the river).

### Further Work

1. Implement weights for River tile placement based on the neighbors of neighboring tiles (1 depth search)
  * Prefer tiles with higher room keep placing tiles based on probability weights in the simulation.
