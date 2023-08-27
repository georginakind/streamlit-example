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

create_player_list = ["george", "jose", "dani", "josh"]
st.write(create_player_list)

action_options = ["hit the deck", "hands up", "girls drink", "boys drink", "they drink", "least drunk drink", "touch a dog", "touch a wall", "stand up"]
