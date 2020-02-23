library(tidyverse)
library(ggplot2)

#Initializations
#========================
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

#initialize while loop
i=1 

#number of times you want simulation to run
runs=10000 

#contains the dice that you are rolling 
d = c('wd','wd','gw','gr')

#initilize the matrix of results 
r = matrix(,nrow=runs-1,ncol=length(d))


#The loops and calculations
#========================

while(i<runs){ 
  for (n in 1:length(d)){
    r[i,n] = sample(eval(parse(text = d[n])),1)
  }
  i=i+1 
}
r=data.frame(r)
r$total = apply(cbind(r[,1:length(d)]), 1, function(x) paste(sort(x), collapse=" "))

#cacluations for distributions of faces
r$red=rowSums(r[1:length(d)] == 'r')
r$blue=rowSums(r[1:length(d)] == 'b')
r$green=rowSums(r[1:length(d)] == 'g')
r$na=rowSums(r[1:length(d)] == 'x')
r$totalM = r$red+r$blue+r$green

r = r %>% mutate(run = seq(1:nrow(r)))
r2 = melt(r,id = names(r2 %>% select(seq(1:length(d)),total,run)))
names(r2)[seq(length(names(r2))-1,length(names(r2)))] = c("Resource","N")

ggplot(data = r2) +geom_bar( aes(x = N)) + facet_grid(Resource ~.)
