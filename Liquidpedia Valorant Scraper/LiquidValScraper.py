#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4  import BeautifulSoup
import requests
import pandas as pd

characterDB = ['Cypher','Sage','Jett','Phoenix','Brimstone','Breach','Viper','Sova','Reyna','Omen','Raze']
mapDB = ['Haven','Bind','Ascent','Split']

def get_lp_val_stats(event):
    
    x = requests.get(event)
    soup = BeautifulSoup(x.text,features="lxml")
    found = soup.findAll("div", {"class": "bracket-popup-body-match-container"})

    map_ = []
    character = []
    team = []
    game = []
    winner = []
    tot = 0
    for i in range(0,len(soup.findAll("div", {"class": "bracket-popup-body-match-container"}))):

        found = soup.findAll("div", {"class": "bracket-popup-body-match-container"})[i]

        for h in mapDB:
            if len(found.findAll(title = h)) == 1:
                theMap = h

        if str(found.findAll("div", {"class": "bracket-popup-body-match-leftcheck"})).find('GreenCheck')>0:
            win = 1
        else:
            win = 2

        for j in characterDB:

            if len(found.findAll("div",{"class":"hide-mobile","style":'float:left;margin-left:10px'})[0].findAll(title = j)) ==1:
                character.append(j)
                team.append(1)
                game.append(i)
                map_.append(theMap)
                winner.append(win)
                tot = tot+1
            if len(found.findAll("div",{"class":"hide-mobile","style":'float:right;margin-right:10px'})[0].findAll(title = j)) ==1:
                character.append(j)
                team.append(2)
                game.append(i)
                map_.append(theMap)
                winner.append(win)
                tot = tot+1




    df_pivot = pd.DataFrame({'Game':game,'Map':map_,'Character':character,'Team':team,'Winner':winner}).pivot_table(index = 'Character',values = "Team",aggfunc = 'count')

    export = df_pivot.reset_index()
    export.columns = ['Character','Picks']
    export['Pick%'] = round(export['Picks']/(tot/5),2)
    export = export.sort_values(by = "Pick%",ascending = False)
    return export


def get_lp_val_charXmap(event):
    x = requests.get(event)
    soup = BeautifulSoup(x.text,features = "lxml")
    found = soup.findAll("div", {"class": "bracket-popup-body-match-container"})

    map_ = []
    character = []
    team = []
    game = []
    winner = []
    tot = 0
    for i in range(0,len(soup.findAll("div", {"class": "bracket-popup-body-match-container"}))):

        found = soup.findAll("div", {"class": "bracket-popup-body-match-container"})[i]

        for h in mapDB:
            if len(found.findAll(title = h)) == 1:
                theMap = h

        if str(found.findAll("div", {"class": "bracket-popup-body-match-leftcheck"})).find('GreenCheck')>0:
            win = 1
        else:
            win = 2

        for j in characterDB:

            if len(found.findAll("div",{"class":"hide-mobile","style":'float:left;margin-left:10px'})[0].findAll(title = j)) ==1:
                character.append(j)
                team.append(1)
                game.append(i)
                map_.append(theMap)
                winner.append(win)
                tot = tot+1
            if len(found.findAll("div",{"class":"hide-mobile","style":'float:right;margin-right:10px'})[0].findAll(title = j)) ==1:
                character.append(j)
                team.append(2)
                game.append(i)
                map_.append(theMap)
                winner.append(win)
                tot = tot+1




    df_pivot = pd.DataFrame({'Game':game,'Map':map_,'Character':character,'Team':team,'Winner':winner}).pivot_table(index = 'Character',columns = "Map",values = "Team",aggfunc = 'count')
    df_pivot.reset_index()
    df_pivot = df_pivot.fillna(0)
    df_pivot['total'] = df_pivot['Ascent'] + df_pivot['Bind'] + df_pivot['Split'] + df_pivot['Haven']
    for i in df_pivot.columns:
        df_pivot[i] = round((df_pivot[i]/df_pivot['total'])*100,2)
    return df_pivot