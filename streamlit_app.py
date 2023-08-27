from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import random
from time import sleep
"""
# meow 

happy birthday! 

this is your own personal drinking game with meow song geneorator included! Straight out of HITS N WIGS 
"""

#st.write('Good Morning') #displayed when the button is clicked
#enter_player = st.text_input('Enter player name: ')
#create_player_list.append(enter_player)
#st.write(create_player_list)

st.write("Type 'done' when you've run out of friends")

action_options = ["hit the deck", "hands up", "girls drink", "boys drink", "they drink", "least drunk drink", "touch a dog", "touch a wall", "stand up"]
#create_player_list = [] 
#enter_player = st.text_input("Enter your player name: ")
#create_player_list.append(enter_player)
#st.write(enter_player)
#st.write(create_player_list)

#while enter_player != "done":
#    enter_player = st.text_input("Enter your player name: ")
#    create_player_list.append(enter_player)
#    print(enter_player) 
#    print(create_player_list)

#create_player_list.remove("done")
#st.write("your players:", (create_player_list))
#print(create_player_list)

create_player_list = [george, jose, tahls] 
if st.button('YEHAW LETS PLAY'):

    decision_options = ["drink", "action"]
    decision = random.choice(decision_options)
    #if decision == "never have i ever":
    #    never_question = random.choice(never_list)
    #    print(never_question)   
    
    if decision == "action":
        action = random.choice(action_options)
        st.write("ACTION:", (action))

    #elif decision == "meow":
    #    meow_song_selection = random.choice(meow_list)
    #    player = random.choice(create_player_list)
    #    print((player)," meow this song\n",
    #      "EVERYONE LOOK AWAY\n",)
    #    sleep(5)
    #    print(meow_song_selection)

    elif decision == "drink":
        player = random.choice(create_player_list)
        print((player), "drink!")

    else: print(decision)
