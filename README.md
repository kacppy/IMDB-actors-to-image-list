# IMDB Movies List into IMG Generator

A script has been created to scrape IMDB to generate a list of actors and collect information about the movies they have each played in. The script will generate both a .txt list of movies and a .png list image for each actor.

See "example-output" folder in the repository.

# Special Note:
I made an update to my old project, because today I looked at the code and saw how bad I had written it a few years ago, and it was giving me a headache.

Original code from the second branch came from ~ 2017.

# Usage

## Instalation

1. Download repository
2. Install all requrements using:
```
pip install -r requirements.txt
```
3. Run script using python, depending on the system you use, for example:
```
python3 IMDB_Movies_List_Gen.py
```

## Interface
![Interface](https://i.imgur.com/X5bxSFU.png)

1. 
After selecting first option, we need to provide direct link to IMDB actors list, for example:
```
https://www.imdb.com/list/ls054840033/

imdb.com/list/ls054840033/
```
It will generate .txt files with a list of movies for each actor from the provided link.


2. 
Option 2 is only available after successfully generating a .txt file from Option 1. 
It will generate image files with movie lists for each actor in the list. 

## Configuration

We can easily change the configuration options in the code at the beginning of the file:

![Configuration](https://i.imgur.com/6bk6C8F.png)

## Output Example:

Available in the "example-output" folder in the repository.

# License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

