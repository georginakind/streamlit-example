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

create_player_list = []
accepted_pretty_names = {'gk', 'george', 'G', "George"}
pete_names = {"pete", "Pete"}
dani_names = {"Dani", "dani", "Dannielle", "dannielle", "DTK", "dtk"}

enter_player_1 = st.text_input("enter player 1 name:")
if enter_player_1 in accepted_pretty_names:
    st.write("omg she's so pretty")
elif enter_player_1 in pete_names:
    st.write("WOOF who let the dogs out!!") 
elif enter_player_1 in dani_names:
    st.write("pickles, nice to see you using the beautiful game")
else: st.write(enter_player_1)
create_player_list.append(enter_player_1)

enter_player_2 = st.text_input("enter player 2 name:")
if enter_player_2 in accepted_pretty_names:
    st.write("omg she's so pretty")
elif enter_player_2 in pete_names:
    st.write("WOOF who let the dogs out!!") 
elif enter_player_2 in dani_names:
    st.write("pickles, nice to see you using the beautiful game")
else: st.write(enter_player_2)
create_player_list.append(enter_player_2)

enter_player_3 = st.text_input("enter player 3 name:")
if enter_player_3 in accepted_pretty_names:
    st.write("omg she's so pretty")
elif enter_player_3 in pete_names:
    st.write("WOOF who let the dogs out!!") 
elif enter_player_3 in dani_names:
    st.write("pickles, nice to see you using the beautiful game")
else: st.write(enter_player_3)
create_player_list.append(enter_player_3)

enter_player_4 = st.text_input("enter player 4 name:")
if enter_player_4 in accepted_pretty_names:
    st.write("omg she's so pretty")
elif enter_player_4 in pete_names:
    st.write("WOOF who let the dogs out!!") 
elif enter_player_4 in dani_names:
    st.write("pickles, nice to see you using the beautiful game")
else: st.write(enter_player_4)
create_player_list.append(enter_player_4)

enter_player_5 = st.text_input("enter player 5 name:")
if enter_player_5 in accepted_pretty_names:
    st.write("omg she's so pretty")
elif enter_player_5 in pete_names:
    st.write("WOOF who let the dogs out!!") 
elif enter_player_5 in dani_names:
    st.write("pickles, nice to see you using the beautiful game")
else: st.write(enter_player_5)
create_player_list.append(enter_player_5)

st.write(create_player_list)

url = 'https://raw.githubusercontent.com/georginakind/meow/main/hits_n_wigs.csv'
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))
st.write(df.head(5))

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
