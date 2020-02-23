# NFL Super Bowl Pool Odds
Every year we all fill out [Super Bowl pools](https://en.wikipedia.org/wiki/Football_pools) and hope our numbers come up during the game. Well how about set expectations before the game? By scraping Football Reference for Super Bowl past scores and determined the occurance of each of the Super Bowl pool results.

## Notes:
* Since the numbers are randomly assigned, I treated a [1,3] and a [3,1] as the same. 
* This was calculated with getting ANY money as opposed to winning the 1st, Halftime, 3rd, and Final individually. This was because when buying a single box in a pool, your effective value for just winning a single quarter is positive. 
* If you have more than one box, adding each of the boxes chance together gets you overall chance to win overall.

## Results:

![image1](https://imgur.com/lJVweTV.png)

Surprisingly, the most common score is [7,0] followed by [3,0] which are all highly desirable numbers in pools. Since most scoring is in combinations of 7 for a touchdown, and 3 for a field goal, our analysis aligns with numbers like 0, 3 and 7 showing high occurrence rates as well as 10 (0), 14 (4), 13 (3) and other common combinations. 

Bad numbers to avoid: 2, 5, 8. 
(Number I got this year... [2,5])

## Improvements:
* Expand to the rest of the playoffs as all are BO1, win or go home games similar to the Super Bowl to provide more data. 
* Per Quarter win odds that can determine estimated outcome per number combinations. 
* Provide the last time your number combo occured!

