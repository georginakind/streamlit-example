from collections import namedtuple
import altair as alt
import math
import pandas as pd
import io
import requests
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

meow_list = ['Nu Flow by Big Brovaz', 'Angel by Shaggy, Rayvon', 'How Will I Know by Whitney Houston', 'Push It by Salt-N-Pepa', "What's Luv? (feat. Ja-Rule & Ashanti) by Fat Joe, Ja Rule, Ashanti", 'Kiss Me by Sixpence None The Richer', 'You Get What You Give by New Radicals', 'Closing Time by Semisonic', 'Come On Eileen by Dexys Midnight Runners', "It Wasn't Me by Shaggy, Rik Rok", 'Party Up by DMX', "Don't Go Breaking My Heart by Elton John, Kiki Dee", 'Steal My Sunshine - Single Version by LEN', 'Take on Me by a-ha', 'Live Your Life - feat. Rihanna by T.I., Rihanna', "Livin' On A Prayer by Bon Jovi", 'Africa by TOTO', 'A Thousand Miles by Vanessa Carlton', 'Shoop by Salt-N-Pepa', 'In Da Club by 50 Cent', "Don't Stop Believin' by Journey", 'You Give Love A Bad Name by Bon Jovi', 'I\'ll Be There for You - Theme From "Friends" by The Rembrandts', 'One Week by Barenaked Ladies', 'Believe by Cher', 'Semi-Charmed Life by Third Eye Blind', "Summer Of '69 by Bryan Adams", "Gettin' Jiggy Wit It by Will Smith", 'No Scrubs by TLC', "Stacy's Mom by Fountains Of Wayne", 'Video Killed The Radio Star by The Buggles', 'What Is Love by Haddaway', 'Return of the Mack by Mark Morrison', 'Iris by The Goo Goo Dolls', 'Down by Jay Sean, Lil Wayne', 'This Is How We Do It by Montell Jordan, Wino', 'Heaven Is A Place On Earth by Belinda Carlisle', 'We Built This City by Starship', 'Let Me Love You by Mario', 'U Remind Me by Usher', 'Hotline Bling by Drake', "Can't Feel My Face by The Weeknd", 'Billie Jean by Michael Jackson', "Don't Stop 'Til You Get Enough by Michael Jackson", 'I Want You Back by The Jackson 5', 'Blame It on the Boogie by The Jacksons', 'The Middle by Jimmy Eat World', 'Sweet Home Alabama by Lynyrd Skynyrd', 'Smells Like Teen Spirit by Nirvana', 'The Boys Are Back In Town by Thin Lizzy', 'Young Hearts Run Free by Candi Staton', 'Accidentally In Love by Counting Crows', 'Dancing in the Moonlight by Toploader', 'American Boy (feat. Kanye West) by Estelle, Kanye West', 'Finally by CeCe Peniston', 'Reach by S Club', 'Love On Top by BeyoncÌ©', 'High by Lighthouse Family', 'I Love You Always Forever by Donna Lewis', 'Angels by Robbie Williams', 'Let Me Entertain You by Robbie Williams', 'Spinning Around by Kylie Minogue', 'Another One Bites The Dust - Remastered 2011 by Queen', "Don't Stop Me Now - Remastered 2011 by Queen", 'Under Pressure - Remastered 2011 by Queen, David Bowie', 'Bohemian Rhapsody - Remastered 2011 by Queen', "Say My Name by Destiny's Child", 'Crazy In Love (feat. Jay-Z) by BeyoncÌ©, JAY-Z', "Bootylicious by Destiny's Child", 'Deja Vu (feat. Jay-Z) by BeyoncÌ©, JAY-Z', "Everybody (Backstreet's Back) - Radio Edit by Backstreet Boys", 'I Wanna Dance with Somebody (Who Loves Me) by Whitney Houston', 'Uptown Girl by Billy Joel', 'Wake Me Up Before You Go-Go by Wham!', 'Celebrate Good Times (Come On) by Funktown America', "Hey Mickey You're so Fine by The Original Chin Chins", 'Mambo No. 5 (a Little Bit of...) by Lou Bega', 'Wannabe by Spice Girls', 'Bring It All Back by S Club', 'Get the Party Started by P!nk', 'The Way You Make Me Feel - Single Version by Michael Jackson', 'Play That Funky Music by Wild Cherry', 'Rock Your Body by Justin Timberlake', "Love Shack by The B-52's", 'Tubthumping - Radio Edit by Chumbawamba', "Keep On Movin' by Five, Steve Mac", 'Rock DJ by Robbie Williams', "U Can't Touch This by MC Hammer", "I'm Still Standing by Elton John", 'Hit Me With Your Best Shot by Pat Benatar', 'This Love by Maroon 5', 'Dancing Queen by ABBA', 'Mamma Mia by ABBA', 'Waterloo by ABBA', 'Body by Loud Luxury, Brando', 'Millionaire by Kelis, AndrÌ© 3000', 'Signs by Snoop Dogg, Charlie Wilson, Justin Timberlake', "Day 'N' Nite - Crookers Remix by Kid Cudi, Crookers", 'California Gurls by Katy Perry, Snoop Dogg', 'Fake Magic by Peking Duk, AlunaGeorge, Aluna', 'All Night (feat. Knox Fortune) by Chance the Rapper, Knox Fortune', 'Sexual by NEIKED, Dyo', 'Shake It by Metro Station', 'Whatever You Like by T.I.', 'Just the Way You Are by Milky', 'You Sexy Thing - Radio Edit by T-Shirt', 'Year 3000 by Busted', 'Shake It Off by Taylor Swift', 'The Horses by Daryl Braithwaite', 'Sk8er Boi by Avril Lavigne', 'Strawberry Kisses 2017 by Nikki Webster, Sam Mac', 'Slice of Heaven by Dave Dobbyn', 'September by Earth\\, Wind & Fire', 'Low (feat. T-Pain) by Flo Rida, T-Pain', 'April Sun in Cuba by Dragon', "That Don't Impress Me Much by Shania Twain", 'You\'re The One That I Want - From "Grease" Original Motion Picture Soundtrack by John Travolta, Olivia Newton-John', "Greased Lightnin' - From ‰ÛÏGrease‰Û\x9d Soundtrack by John Travolta, Jeff Conaway", 'Breaking Free by Troy, Gabriella, Disney', "We're All In This Together by High School Musical Cast, Disney", 'The Best of Both Worlds by Hannah Montana', 'Since U Been Gone by Kelly Clarkson', 'Leave (Get Out) by JoJo', 'Where Is The Love? by Black Eyed Peas', 'My Humps by Black Eyed Peas', 'Pump It by Black Eyed Peas', '...Baby One More Time by Britney Spears', 'Oops!...I Did It Again by Britney Spears', 'Time of Our Lives by Pitbull, Ne-Yo', 'Fireball (feat. John Ryan) by Pitbull, John Ryan', 'Shots by LMFAO, Lil Jon', 'Drive by Shannon Noll', 'SeÌ±orita by Justin Timberlake', 'Promiscuous by Nelly Furtado, Timbaland', "I'm Like A Bird by Nelly Furtado", 'Maneater by Nelly Furtado', 'These Words by Natasha Bedingfield', 'Get Ur Freak On by Missy Elliott', 'Work It by Missy Elliott', 'Dancing in the Moonlight by Toploader', 'American Boy (feat. Kanye West) by Estelle, Kanye West', 'Party In The U.S.A. by Miley Cyrus', 'Everywhere - 2017 Remaster by Fleetwood Mac', 'Dance Wiv Me by Dizzee Rascal, Calvin Harris, Chrom3', "I'm Coming Out by Diana Ross", 'Holiday by Dizzee Rascal, Laidback Luke', 'Freaky Friday (feat. Chris Brown) by Lil Dicky, Chris Brown', 'September by Earth\\, Wind & Fire', 'Ms. Jackson by Outkast', 'Remind Me to Forget by Kygo, Miguel', 'Wall To Wall by Chris Brown', 'Gotta Go My Own Way - From "High School Musical 2" by Troy, Gabriella Montez', 'All My Friends by Snakehips, Tinashe, Chance the Rapper', "Livin' It Up by Ja Rule, Case", 'Just Wanna Be With You by High School Musical Cast, Zac Efron, Lucas Grabeel, Olesya Rulin, Vanessa Hudgens', 'Waterfalls by TLC', "Don't You (Forget About Me) - Remastered by Simple Minds", 'Hey Ya! - Radio Mix / Club Mix by Outkast', "Ghetto Supastar (That is What You Are) (feat. Ol' Dirty Bastard & MÌ_a) by Pras, Ol' Dirty Bastard, MÌ_a", 'No Diggity by Chet Faker', 'Whatta Man by Salt-N-Pepa, En Vogue', 'Trick Me by Kelis', "It Wasn't Me by Shaggy, Rik Rok", 'Hypnotize - 2014 Remaster by The Notorious B.I.G.', 'Ignition - Remix by R. Kelly', 'In Da Club by 50 Cent', 'My Neck, My Back (Lick It) by Khia', 'Gold Digger by Kanye West, Jamie Foxx', 'Milkshake by Kelis', 'Pony by Ginuwine', 'Jenny from the Block (feat. Jadakiss & Styles P.) - Track Masters Remix by Jennifer Lopez, Jadakiss, Styles P', 'Be Faithful by Fatman Scoop, Crooklyn Clan', 'Roses by Outkast', 'One More Time by Daft Punk', 'Teenage Crime - Radio Edit by Adrian Lux', "Drop It Like It's Hot by Snoop Dogg, Pharrell Williams", 'London Bridge by Fergie', 'Like A G6 by Far East Movement, The Cataracs, DEV', 'Cola by CamelPhat, Elderbrook', 'Thrift Shop (feat. Wanz) by Macklemore & Ryan Lewis, Macklemore, Ryan Lewis, Wanz', "Jessie's Girl by Rick Springfield", "Stacy's Mom by Bowling For Soup", 'Cha Cha Slide by Mr. C', '(Your Love Keeps Lifting Me) Higher & Higher by Jackie Wilson', "Signed, Sealed, Delivered (I'm Yours) by Stevie Wonder", "You Can't Hurry Love - 2016 Remaster by Phil Collins", 'I Want You Back by The Jackson 5', 'Gasolina by Daddy Yankee', 'Get Busy by Sean Paul', 'Lady (Hear Me Tonight) by Modjo', "This Girl - Kungs Vs. Cookin' On 3 Burners by Kungs, Cookin' On 3 Burners", 'Show Me Love (feat. Robin S.) by Steve Angello, Laidback Luke, Robin S', 'Formation by BeyoncÌ©', 'Mi Gente (feat. BeyoncÌ©) by J Balvin, Willy William, BeyoncÌ©', 'Valerie (feat. Amy Winehouse) - Version Revisited by Mark Ronson, Amy Winehouse', 'Shooting Stars by Bag Raiders', 'Swalla (feat. Nicki Minaj & Ty Dolla $ign) by Jason Derulo, Nicki Minaj, Ty Dolla $ign', "Can't Hold Us (feat. Ray Dalton) by Macklemore & Ryan Lewis, Macklemore, Ryan Lewis, Ray Dalton", 'Pursuit Of Happiness - Extended Steve Aoki Remix (Explicit) by Kid Cudi, MGMT, Ratatat', 'Pony by Ginuwine', 'Party Up by DMX', 'Jump Around by House Of Pain', "Can't Stop by Red Hot Chili Peppers", 'Lady Marmalade - From "Moulin Rouge" Soundtrack by Christina Aguilera, Lil\' Kim, MÌ_a, P!nk', "It Wasn't Me by Shaggy, Rik Rok", 'Teenage Dirtbag by Wheatus', 'Praise You - Radio Edit by Fatboy Slim', 'Million Voices - Radio Edit by Otto Knows', 'Umbrella by Rihanna, JAY-Z', 'The Way You Make Me Feel - 2012 Remaster by Michael Jackson', 'Touch The Sky by Kanye West, Lupe Fiasco', 'Tribute by Tenacious D', 'Rock DJ - 2004 Mix by Robbie Williams', 'Hot In Herre by Nelly', 'Memories (feat. Kid Cudi) by David Guetta, Kid Cudi', "In My Mind by Dynoro, Gigi D'Agostino", "Let's Groove by Earth\\, Wind & Fire", "I See You Baby - Fatboy Slim Radio Edit by Groove Armada, Gram'ma Funk", 'House Work by Jax Jones, Mike Dunn, MNEK', 'Move Your Feet by Junior Senior', 'Heartbreaker by MSTRKRFT', 'Bitch Better Have My Money by Rihanna', 'My Love by Route 94, Jess Glynne', 'Wearing My Rolex - Radio Edit by Wiley', 'Lose Control (feat. Ciara & Fat Man Scoop) by Missy Elliott, Ciara, Fatman Scoop', 'Shake That by Eminem, Nate Dogg', 'Dirrty by Christina Aguilera, Redman', 'Beautiful Soul by Jesse McCartney', 'Move on Up - Single Edit by Curtis Mayfield', 'Follow Me by Uncle Kracker', 'Khe Sanh - 2011 Remastered by Cold Chisel', 'All Star by Smash Mouth', 'Mr. Brightside by The Killers', 'What About Me by Shannon Noll', "You're the Voice by John Farnham", 'Walking On Sunshine by Katrina & The Waves', 'Girls Just Want to Have Fun by Cyndi Lauper', "Stayin' Alive by Bee Gees", "Ain't No Mountain High Enough by Marvin Gaye, Tammi Terrell", "Hips Don't Lie (feat. Wyclef Jean) by Shakira, Wyclef Jean", 'Down Under by Men At Work', 'S Club Party by S Club', 'All The Small Things by blink-182', "I'm Gonna Be (500 Miles) by The Proclaimers", "Don't Stop Movin' by S Club", 'American Pie by Don McLean', 'Hakuna Matata by Billy Eichner, Seth Rogen, JD McCrary, Childish Gambino', 'Torn by Natalie Imbruglia', 'Stick to the Status Quo by High School Musical Cast, Disney', "Buy U a Drank (Shawty Snappin') (feat. Yung Joc) by T-Pain, Yung Joc", 'Counting The Beat by The Swingers', 'Easy Lover by Philip Bailey, Phil Collins', 'Mystery Man by Hot Potato Band', 'Sweet Caroline by Neil Diamond', 'December, 1963 (Oh What a Night!) by Frankie Valli & The Four Seasons', 'Hollaback Girl by Gwen Stefani', '(You Drive Me) Crazy by Britney Spears', 'The Salmon Dance by The Chemical Brothers', "That Don't Impress Me Much by Shania Twain", 'Jack & Diane by John Mellencamp', 'Point of View - Radio Edit by DB Boulevard', "That Don't Impress Me Much by Shania Twain", 'The Impression That I Get by The Mighty Mighty Bosstones', 'Shake Your Groove Thing by Peaches & Herb', 'Hey Baby by DJ ÌÐtzi, The Bellamy Brothers', 'The Fresh Prince of Bel-Air by DJ Jazzy Jeff & The Fresh Prince', 'Come On Eileen by Dexys Midnight Runners', 'Give It Up by KC & The Sunshine Band', 'SexyBack (feat. Timbaland) by Justin Timberlake, Timbaland', "Let's Get Loud by Jennifer Lopez", 'This Is How We Do It by Montell Jordan, Wino', 'Forever by Chris Brown', 'Dreams - 2004 Remaster by Fleetwood Mac', 'Boyfriend by Justin Bieber', 'Eenie Meenie by Justin Bieber, Sean Kingston', 'U Smile by Justin Bieber', 'Love Story by Taylor Swift', 'You Belong With Me by Taylor Swift', 'Teach Me How to Dougie by Cali Swag District', 'The Anthem by Good Charlotte', 'Gimme! Gimme! Gimme! (A Man After Midnight) by ABBA', 'Gimme More by Britney Spears', 'Work Bitch by Britney Spears', "Can't Get You out of My Head by Kylie Minogue", 'Love at First Sight by Kylie Minogue', 'On a Night like This by Kylie Minogue', 'Ice Ice Baby by Vanilla Ice', 'Spice Up Your Life by Spice Girls', "U Can't Touch This by MC Hammer", 'Whenever, Wherever by Shakira', 'Who Do You Think You Are by Spice Girls', 'Pon de Replay by Rihanna', 'Celebration - Single Version by Kool & The Gang', "Jessie's Girl by Jessies Girl", "That Don't Impress Me Much - Dance Mix by Shania Twain", 'Come on over Baby (All I Want Is You) - Radio Version by Christina Aguilera', 'SOS by Rihanna', 'Kiss Me Thru The Phone by Soulja Boy, Sammie', 'Crank That (Soulja Boy) by Soulja Boy', 'Young, Wild & Free (feat. Bruno Mars) by Snoop Dogg, Wiz Khalifa, Bruno Mars', 'Party In The U.S.A. by Miley Cyrus', 'Trumpets by Jason Derulo', 'TiK ToK by Kesha', 'Umbrella by Rihanna, JAY-Z', 'Thrift Shop (feat. Wanz) by Macklemore & Ryan Lewis, Wanz', 'Bad Blood by Taylor Swift', 'Firework by Katy Perry', 'Call Me Maybe by Carly Rae Jepsen', 'U Smile by Justin Bieber', 'Pump It by Black Eyed Peas', "Hips Don't Lie (feat. Wyclef Jean) by Shakira, Wyclef Jean", 'Glamorous by Fergie, Ludacris', 'Candy Shop by 50 Cent, Olivia', 'I Kissed A Girl by Katy Perry', 'A Thousand Miles by Vanessa Carlton', 'In Da Club by 50 Cent', "Buy U a Drank (Shawty Snappin') (feat. Yung Joc) by T-Pain, Yung Joc", 'Promiscuous by Nelly Furtado, Timbaland', 'Yeah! (feat. Lil Jon & Ludacris) by Usher, Lil Jon, Ludacris', "Don't Cha by The Pussycat Dolls, Busta Rhymes", 'Fergalicious by Fergie, will.i.am', 'Hot In Herre by Nelly', 'Pon de Replay by Rihanna', "Ridin' Solo by Jason Derulo", 'My Humps by Black Eyed Peas', 'Kiss Kiss (feat. T-Pain) by Chris Brown, T-Pain', 'Temperature by Sean Paul', 'I Want You Back by The Jackson 5', 'Since U Been Gone by Kelly Clarkson', '7 Things - Single Version by Miley Cyrus', 'Sexy Can I feat. Yung Berg by Ray J', 'Whatever You Like by T.I.', 'Mr. Brightside by The Killers', 'Where Is The Love? by Black Eyed Peas', 'Complicated by Avril Lavigne', 'My Humps by Black Eyed Peas', 'What Makes You Beautiful by One Direction', 'You Belong With Me by Taylor Swift', 'Tipsy - Radio Mix by J-Kwon', 'I Love College by Asher Roth', "Jessie's Girl by Rick Springfield", 'Dirty Little Secret by The All-American Rejects', 'London Bridge by Fergie', 'Year 3000 by Jonas Brothers', 'Last Friday Night (T.G.I.F.) by Katy Perry', 'Empire State Of Mind by JAY-Z, Alicia Keys', 'Rack City by Tyga', 'Welcome to the Black Parade by My Chemical Romance', 'Shalala Lala by Vengaboys', 'Work by Kelly Rowland', 'Just A Little by Liberty X', 'Come Said The Boy - Digitally Remastered by Mondo Rock', 'Every Little Thing She Does Is Magic by The Police', 'Everybody Wants To Rule The World by Tears For Fears']



create_player_list = []
accepted_pretty_names = {'gk', 'george', 'G', "George", "g"}
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

#url = 'https://raw.githubusercontent.com/georginakind/meow/main/hits_n_wigs.csv'
#download = requests.get(url).content
#df = pd.read_csv(io.StringIO(download.decode('utf-8')))
#st.write(df.head(5))

decision_options = ["drink", "action", "meow", "meow"]
action_options = ["hit the deck", "hands up", "girls drink", "boys drink", "they drink", "least drunk drink", "touch a dog", "touch a wall", "stand up"]


if st.button('LETS GO GIRLS'):
  decision = random.choice(decision_options)
  if decision == "drink":
    player = random.choice(create_player_list)
    st.write((player), "drink!")
 
  elif decision == "meow":
      meow_song_selection = random.choice(meow_list)
      player = random.choice(create_player_list)
      st.write((player), "Meeeow this song:\n", "EVERYONE LOOK AWAY")
      sleep(5)
      st.write(meow_song_selection)
      
  elif decision == "action":
    action = random.choice(action_options)
    st.write("ACTION:", (action))

  else: 
    st.write("you did sometihng wrong G")
