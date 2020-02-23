library(tidyverse)
library(gtools)

#Part 1: Calculate Streaks
#Part 2: Total Gold and Interest Calcuations

#### PART 1 Streak Calculations ####

#Create all permations of the wins and losses that can occur.
#Including only fighting rounds as opposed to the 3 creep rounds in the beginning and the 1 every 5 after 10
x = c("W","L")
y = permutations(n = 2,r=8,v=x,repeats.allowed=T)
y_u= unique(y)

#Creep rounds, don't effect lose streaks

#StreakGoldFrame to be used to look up streak
StreakGold = data.frame(Streak = c(seq(1,8),seq(1,10)),
                        W_L = c("W","W","W","W","W","W","W","W","L","L",
                                "L","L","L","L","L","L","L","L"),
                        value = c(0,0,1,1,2,2,3,4,0,0,1,1,2,2,2,2,2,2))



StreakGoldSum = function(vector){
  #determine if a streak occured:
  Str = sequence(rle(as.character(vector))$lengths)
  
  WL = vector
  StreakGoldAmount = 0
  for (i in seq(1,length(vector))){
    StreakGoldAmount = (StreakGold %>% filter(Streak == Str[i],W_L == WL[i]))$value + StreakGoldAmount
  }
  StreakGoldAmount
}

streak = c()
wins = c()

for (i in seq(1:dim(y_u)[1])){
  streak[i] = StreakGoldSum(y_u[i,])
  wins[i] = sum(y_u[i,] == "W")
}

df = data.frame(y_u,streak,wins) %>% mutate(total_G = streak+wins)
names(df)[1:8] = c("R3","R4","R5","R6","R7","R8","R9","R11")



#### PART 2 Total Gold and Interest ####

#1 gold round 1, 2 2, 3 3, 4 4, 5 5, 5 continued after.

round  = seq(1,5)
gold = c(1,2,3,4,5)
GoldPerRoundFrame = data.frame(round,gold)
