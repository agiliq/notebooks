This tutorial will teach you how to convert sql to pandas. (And vice versa).

This uses two csv files, which are in thie repo:

* buildings.csv [list of tallest building](https://en.wikipedia.org/wiki/List_of_tallest_buildings_in_the_world) taken from wikipedia.
* continents.csv: A mapping of countries to continents

We also have a buildings.db which is a sqlite file which has the same data as csv files. We will show a sql statement, and then a pandas expression to get the same result. The sql statement can be used with the buildings.db. The required libraries can be installed with `pip install -r requirements.txt`
