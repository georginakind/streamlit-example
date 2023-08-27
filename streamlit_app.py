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

if st.button('reset friends'):
    create_player_list = [] 

else:
    enter_player = st.text_input("Enter your player name: ")
    create_player_list.append(enter_player)
    st.write(enter_player)

    while enter_player != "done":
        enter_player = st.text_input("Enter your player name: ")
        create_player_list.append(enter_player)
        print(enter_player)   

    create_player_list.remove("done")
    st.write("your players:", (create_player_list))

      
st.button('YEHAW LETS PLAY')




with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
