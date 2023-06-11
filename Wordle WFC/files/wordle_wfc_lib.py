##-----Part 1

#create weights for inplace, and elsewhere values

def letter_summer(word):
    w_iter = 0
    value_place = 0
    value_else = 0
    for letter in word:
        value_place +=  [(x_df['placement'] == w_iter+1) & (x_df['character'] == letter.upper())]['count'].item()
        value_else += x_df[(x_df['placement'] != w_iter+1) & (x_df['character'] == letter.upper())]['count'].sum()
        w_iter += 1
    return value_place,value_else


##-----Part 2

#find letters in and not in words
def is_letter_in_word(target_word, guess):
    x = []
    y = []
    for i in list(guess):
        if i in list(target_word):
            x.append(i)
        else:
            y.append(i)
    return x,y

#create a script that takes all possible solutions and collapses to the highest rated one till it reaches the right word. 
def wfc_solve(target_word,list, method='total_value',starting_word = None):
    #method can be value_else, value_place, total_value
    
    list_of_columns = ['first_letter','second_letter','third_letter','fourth_letter','fifth_letter']
    
    guess_list = []
    wfc_list = list.copy()
    guess_count = 0
    if starting_word:
        guess = starting_word
    else:

        guess = wfc_list.query('unique_chars==5').sort_values(by = method,ascending = False).head(1)['word'].item() #start with a word with max different characters

    while (guess_count < 100): #hard code a limit of 100 guesses
        #define a new guess
        
       
        #see if letters in target:
        if guess != target_word:
            in_word,not_in_word = is_letter_in_word(target_word,guess)
            for i in not_in_word:
                wfc_list = wfc_list[wfc_list['first_letter'] != i]
                wfc_list = wfc_list[wfc_list['second_letter'] != i]
                wfc_list = wfc_list[wfc_list['third_letter'] != i]
                wfc_list = wfc_list[wfc_list['fourth_letter'] != i]
                wfc_list = wfc_list[wfc_list['fifth_letter'] != i]
        
        
        
        #clamp letters that are in the right place
        
            for j in in_word:
                index = 0
                for k in target_word:
                    if j == k:
                        wfc_list = wfc_list[wfc_list[list_of_columns[index]] == j]
                    index += 1
         
        guess_count += 1    
        
        guess_list.append(guess)
        
        if guess == target_word:
            break
        else:
            wfc_list = wfc_list[wfc_list['word'] != guess]
        guess = wfc_list.sort_values(by = method,ascending = False).head(1)['word'].item()    
            
    return guess_list