# Dota Underlords Streak Analyzer
Created July 2019 [Outdated from patches to the game]

In the strategy game Dota Underlords, you gain gold for winning a round, and also gain more gold if you are on a win streak. For losing, you gain no gold, but will gain gold when on a lose streak. Simply, winning is harder than losing on purpose in the game, so determining when to hedge and lose out to gain more gold can be determined using this program. 

### Process
Permeated every combination possible for the first 10 turns (deemed the most pivotal in the game). Determined which generated the most gold based on:
* Natural gold gain from winning (1g) and losing (0g)
* Streak gold from repetitive winning or losing (see below)

### Win Streak
|Streak|Gold from Streak|
|------|---------------------------|
|1|0|
|2|0|
|3|1|
|4|1|
|5|2|
|6|2|
|7|3|
|8|4|

### Loss Streak
|Streak|Gold from Streak|
|------|---------------------------|
|1|0|
|2|0|
|3|1|
|4|1|
|5|2|
|6|2|
|...|2|
|n|2|

## Results
Winning was still seen as superior to losing, but the worst result was alternating between winning and losing through the game without obtaining a win-streak/loss-streak:

![image1](https://imgur.com/GCBeLqx.png)

...

![image2](https://imgur.com/FA8GyCZ.png)

The interesting thing to determine was how much gold was gained from lose streaking which was seen as a consistent strategy compared to trying to win every round. 
