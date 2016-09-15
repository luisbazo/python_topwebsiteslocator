# python_topwebsiteslocator

This an example of python program that reads the list of the most popular web sites https://en.wikipedia.org/wiki/List_of_most_popular_websites and prints out a map on google maps with the location of the site server. The markers in the map are colored based in the web site position in the ranking. The most popular ones are colored in red.

The main goal is to have an idea of which locations in the world serve the most popular web sites. San Francisco, Seatle and Asi-Pacific areas concentrate many of the most popular web sites.

Project is composed by 3 files:

1. topwebsiteslocator.py

Python script that reads list of web sites from a csv file and prints out a map with location of sites servers. It does not have any parameters.

2. websites.csv

CSV file with most popular web sites ranking captured from https://en.wikipedia.org/wiki/List_of_most_popular_websites

3. index.html

Html that contains the site map.
Any time the script topwebsiteslocator.py is executed a new version of index.html is generated.

Prerequisites

  Python Libraries

  Use library gmplot to print out map https://github.com/vgm64/gmplot

        pip install gmplot

  Use library urllib2 to find the coordinates of a given url

        pip install urllib2

  Extensions

  The map can be enhaced and also the library gmplot to support publish the map in a web site without the library installed.
  More labels and data could be displayed in the map.
