from imdb import Cinemagoer
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import textwrap, os, re


#Config
text_start_height = 70
text_start_width = 70
text_color = (255, 255, 255)
text_color2 = (224, 31, 141)
text_color_outline = (0,0,0)
fontsize = 70
line_size = 110
additional_lines = 0
background_color = (19, 186, 49)
image_width = 1920
font = ImageFont.truetype('arial.ttf', fontsize)
output_dir = "output/"

x = text_start_width
y = text_start_height


def generate_txts(id_string):
    i = Cinemagoer()
    p = i.get_person(id_string)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir) 

    if not os.path.exists(output_dir+p['name']):
        os.mkdir(output_dir+p['name'])
    output = output_dir+p['name']+'/'+p['name']+'.txt'

    print("( + ) "+p['name'])

    if 'actress' not in p['filmography']:
        scrap = p['filmography']['actor']
    else:
        scrap = p['filmography']['actress']

    file = open(output,"w",encoding="utf8")

    for movie in scrap:    
        try:
            file.write("%s - %s (%s)  \n" %(movie['year'], movie['title'], movie['kind']))
        except:
            file.write("Upcoming - %s (%s)  \n" %(movie['title'], movie['kind']))


def draw_text(text, number, draw):
    global y

    lines = textwrap.wrap(text, width=50)
    
    for line in lines:
        draw.text((x-1, y), line, font=font, fill=text_color_outline)
        draw.text((x+1, y), line, font=font, fill=text_color_outline)
        draw.text((x, y-1), line, font=font, fill=text_color_outline)
        draw.text((x, y+1), line, font=font, fill=text_color_outline)
        if (number%2==0):
            draw.text((x, y), line, font=font, fill=text_color)
        else:
            draw.text((x, y), line, font=font, fill=text_color2)
        y += line_size


def generate_file(name):
    numline = 0 

    for line in open(output_dir+'/'+name+'/'+name+'.txt', 'r'):
        numline +=1
        if len(line) > 50:
            numline += 1

    height = (((numline + additional_lines) * line_size) + (text_start_height * 2))
    image_size = (image_width, height)
    image = Image.new('RGB', image_size, background_color)
    draw = ImageDraw.Draw(image)
    number = 0

    file = open(output_dir+'/'+name+'/'+name+'.txt', 'r')

    for row in file:
        draw_text(str(row), number, draw)
        number += 1

    file.close()
    image.save(output_dir+'/'+name+'/'+name+' list.png')


def main_menu():
    global y
    print("Select what you wanna do:")
    print("1. Generate TXTs movies list")
    print("2. Generate IMGs movies list")

    choice = int(input("Select option: (1, 2): "))

    if choice == 1:
        url = input("Pass the link to IMDB list: ")

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        match = re.search(r'ls\d+', url).group()
        new_url = 'https://www.imdb.com/list/'+match+'/export'
        df = pd.read_csv(new_url)

        print("( + ) Found "+str(len(df['Const']))+" actors in link")
        print("( + ) Now generating .txt film list:")

        for id_string in df['Const']:
            id_string = id_string[2:]
            generate_txts(id_string)

    elif choice == 2:

        if not os.path.exists(output_dir):
            print("( ! ) First you must generate .txt")
            main_menu()

        print("( + ) Found "+str(len(os.listdir(output_dir)))+" actors")
        print("( + ) Now generating images film list:")

        for folder in os.listdir(output_dir):
            print("( + ) "+folder)
            generate_file(folder)
            y = text_start_height


if __name__ == '__main__':
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    main_menu()