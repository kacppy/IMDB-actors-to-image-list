# IMDB actors movies list to image converter in Python

Creates list of films that actors played in as png&txt files. (see folder named "example-output")

# How it works?

We need a IMDB actors list ex. https://www.imdb.com/list/ls002477950/
Download it from IMDB site as csv file (export option)

Script from "generate-txt" folder, provides as output txt files with name of actor and list of movies he/she played in
In "generate-img" there are 2 scripts, "list.py" generates list of previously created txt files as "list.csv" file.
"go.py" creates list of films as png file (see folder named "example-output")

# Need "arial.ttf" and "exo.otf" fonts in directory you run python script or replace it with whatever font you want