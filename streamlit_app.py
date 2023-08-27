from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import random
from time import sleep
import requests as rq

"""
# meow 

happy birthday! 

this is your own personal drinking game with meow song geneorator included! Straight out of HITS N WIGS 
"""

url = "https://github.com/georginakind/meow/blob/main/hits_n_wigs.xlsx"
data = rq.get(url).content
df = pd.read_excel(BytesIO(data))

st.write(df)
st.write("data below")
st.write(data)


#st.write('Good Morning') #displayed when the button is clicked
#enter_player = st.text_input('Enter player name: ')
#create_player_list.append(enter_player)
#st.write(create_player_list)

create_player_list = ["george", "jose", "dani", "josh"]
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
