# Wordle Wave Function Collapse

[Wordle](https://www.nytimes.com/games/wordle/index.html) is a word game that people will take turns to guess a 5 letter word, where you are scored on each word whether it is correct placement and correct letter (green) or the letter exists in the word (yellow). These two signals (CorrectWord, LetterInWord) power the guessing ability of players as they have 6 chances to guess the 5 letter word. 

Using a similar framework to [Wave Function Collpase](https://youtu.be/2SuvO4Gi7uY) that we see used in video games to create procedural generation that is not just random noise and in solving sudoku. Using this framework that collapses the possibility space every time a correct letter is guessed in Wordle, we can both understand the possibility space (given a list of possible words) AND also score the best words to start that collpase the most possibility space. 

# Results

Using this methodology, we were able to find that while `arose` does not have the highest Norm_Place, a metric that determines how often we will get a green, it does have a high Norm_Else which measures the yellow. Combining these two values gives it the highest score among all guesses and was what I ended up using from then on to guess for Wordle. 

Other good guesses that were discovered were: `cares`, `tares`, `cores`, `tears` among others. 