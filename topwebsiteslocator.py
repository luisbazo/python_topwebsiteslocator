import gmplot
import pandas as pd
import json
import urllib2
from optparse import OptionParser

def getColour(position, total):

    resto = position / total

    color =""
    if (resto < 0.3):
      color = "red"
    elif (resto < 0.5):
      color = "orange"
    elif (resto < 0.7):
      color = "yellow"
    elif (resto < 0.9):
      color = "blue"
    elif (resto <= 1):
      color = "white"
    else:
      color = "black"

    return color

df = pd.read_csv('websites.csv')
df.head()
gmap = gmplot.GoogleMapPlotter(0, 0, 2)

for index, row in df.iterrows():
  url = df.loc[index,"url"]
  urlopen = 'http://freegeoip.net/json/' + url
  f = urllib2.urlopen(urlopen)
  json_string = f.read()
  f.close()
  location = json.loads(json_string)
  text = url + ' ' + ' #' + str(df.loc[index,"ranking"])

  color = getColour(float(df.loc[index, "ranking"]), df['ranking'].max())
  gmap.marker(location['latitude'], location['longitude'], color,title=text)

gmap.draw("index.html")
