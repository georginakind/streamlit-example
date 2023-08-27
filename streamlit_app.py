from collections import namedtuple
import altair as alt
import math
import pandas as pd
import io
import requests
import streamlit as st
import random
from time import sleep
import requests as rq

"""
# meow 

happy birthday! 

this is your own personal drinking game with meow song geneorator included! Straight out of HITS N WIGS 
"""


#st.write('Good Morning') #displayed when the button is clicked
#enter_player = st.text_input('Enter player name: ')
#create_player_list.append(enter_player)
#st.write(create_player_list)

create_player_list = ["george", "jose", "dani", "josh"]
st.write(create_player_list)

enter_player_1 = st.text_input("enter player 1 name:")
st.write(enter_player_1)
create_player_list.append(enter_player_1)

enter_player_2 = st.text_input("enter player 2 name:")
st.write(enter_player_2)
create_player_list.append(enter_player_2)

enter_player_3 = st.text_input("enter player 3 name:")
st.write(enter_player_3)
create_player_list.append(enter_player_3)

enter_player_4 = st.text_input("enter player 4 name:")
st.write(enter_player_4)
create_player_list.append(enter_player_4)

st.write(create_player_list)

decision_options = ["drink", "action"]
action_options = ["hit the deck", "hands up", "girls drink", "boys drink", "they drink", "least drunk drink", "touch a dog", "touch a wall", "stand up"]


if st.button('LETS GO GIRLS'):
  decision = random.choice(decision_options)
  if decision == "drink":
    player = random.choice(create_player_list)
    st.write((player), "drink!")

  elif decision == "action":
    action = random.choice(action_options)
    st.write("ACTION:", (action))

  else: 
    st.write("you did sometihng wrong G")
