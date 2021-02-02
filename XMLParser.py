import pandas as pd
from xml.etree.ElementTree import parse

file = 'standard_jan21frl_xml.xml'

document = parse(file)

name = []
country = []
sex = []
title = []
rating = []
games = []
birthday = []

for player in document.iterfind('player'):
    name.append(player.findtext('name'))
    country.append(player.findtext('country'))
    sex.append(player.findtext('sex'))
    title.append(player.findtext('title'))
    rating.append(player.findtext('rating'))
    birthday.append(player.findtext('birthday'))
                  
df = pd.DataFrame({'name':name, 
                   'country':country, 
                   'sex':sex,
                   'title':title,
                   'rating':rating,
                   'birthday':birthday
                  })
print(df)
df.to_csv('std_jan_2021.csv')
