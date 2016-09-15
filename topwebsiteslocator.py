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

  df.loc[index,"city"] = url + ' ' + ' #' + str(df.loc[index,"ranking"])
  df.loc[index,"long"] = location['longitude']
  df.loc[index,"lat"] = location['latitude']

  color = getColour(float(df.loc[index, "ranking"]), df['ranking'].max())

  gmap.marker(df.loc[index,"lat"], df.loc[index,"long"], color,title=df.loc[index,"city"])


#gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
#gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
#gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
#gmap.heatmap(heat_lats, heat_lngs)

#gmap.plot(37.428, -122.145, 'cornflowerblue', edge_width=10)
#gmap.scatter(37.428, -122.145, '#3B0B39', size=40, marker=False)
#gmap.scatter(37.428, -122.145, 'k', marker=True)
#gmap.heatmap(37.428, -122.145)

#gmap.scatter(df['lat'], df['long'], 'k', marker=True)

gmap.draw("mymap.html")
