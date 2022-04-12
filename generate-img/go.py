from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import textwrap
import csv, os,re, sys, shutil


#Config
text_start_height = 70
text_start_width = 70
text_color = (255, 255, 255)
text_color2 = (250, 72, 72)
text_color_outline = (0,0,0)
fontsize = 70
line_size = 110
additional_lines = 14
background_color = (247, 179, 34)
image_width = 1920
font = ImageFont.truetype("exo.otf", fontsize)
txts_dir = "txts"
output_dir = "img/"


def create_imdb_info(output):
	shutil.copy(os.path.join(txts_dir, actors), os.path.join(output_dir, output+".txt"))




def create_title(data, output):
	x = 30
	y = 30

	height = 1080
	napis = "movies list"
	napis = napis.upper()
	data = data.upper()
	size = 120
	

	while (((ImageFont.truetype("arial.ttf", size).getsize(data)[0]) + (ImageFont.truetype("arial.ttf", int(0.75 * size)).getsize(napis)[0]))>1840):
		size -= 1

	while (((ImageFont.truetype("arial.ttf", size).getsize(data)[0]) + (ImageFont.truetype("arial.ttf", int(0.75 * size)).getsize(napis)[0]))<1840):
		size += 1


	check = ((ImageFont.truetype("arial.ttf", size).getsize(data)[0]) + (ImageFont.truetype("arial.ttf", int(0.75 * size)).getsize(napis)[0]))
	while ((check + (2 * x))<1910):
		x += 1

	while (((ImageFont.truetype("arial.ttf", size).getsize(data)[1]) + (2 * y))<(height / 6)):
		y += 1
	
	while (((ImageFont.truetype("arial.ttf", size).getsize(data)[1]) + (2 * y))>(height / 6)):
		y -= 1

	font = ImageFont.truetype("arial.ttf", size)
	image_size = (image_width, height)
	image = Image.new('RGBA', image_size, (0,0,0,0))
	draw = ImageDraw.Draw(image)

	draw.rectangle(((0, 00), (1920, (height/6 + 20))), fill=background_color)

	line_width = font.getsize(data)[0]
	draw.text((x-1, y), data, font=font, fill=text_color_outline)
	draw.text((x+1, y), data, font=font, fill=text_color_outline)
	draw.text((x, y-1), data, font=font, fill=text_color_outline)
	draw.text((x, y+1), data, font=font, fill=text_color_outline)
	draw.text((x, y), data, font=font, fill=text_color2)

	x += line_width+20 
	y += int(0.25 * size)

	draw.text((x-1, y), napis, font=ImageFont.truetype("arial.ttf", int(0.75 * size)), fill=text_color_outline)
	draw.text((x+1, y), napis, font=ImageFont.truetype("arial.ttf", int(0.75 * size)), fill=text_color_outline)
	draw.text((x, y-1), napis, font=ImageFont.truetype("arial.ttf", int(0.75 * size)), fill=text_color_outline)
	draw.text((x, y+1), napis, font=ImageFont.truetype("arial.ttf", int(0.75 * size)), fill=text_color_outline)
	draw.text((x, y), napis, font=ImageFont.truetype("arial.ttf", int(0.75 * size)), fill=text_color2)

	image.save(output_dir+output+" title.png")


def create_list(output):
	global draw, x, y
	
	x = text_start_width
	y = text_start_height

	file = open(txts_dir+"/"+actors)
	numline = (len(file.readlines()) - 3)

	height = (((numline + additional_lines) * line_size) + (text_start_height * 2))
	image_size = (image_width, height)
	image = Image.new('RGB', image_size, background_color)
	draw = ImageDraw.Draw(image)
	print(actors)
	print(numline)
	for xd in range(0, numline):
		with open(txts_dir+"/"+actors) as f:
			mycsv = csv.reader(f)
			mycsv = list(mycsv)
			line_number = xd
			data=mycsv[line_number][0]
			#print(font.getsize(data))
			draw_text(data, xd)
			image.save(output_dir+output+" list.png")




def draw_text(text, number):
	global y
	lines = textwrap.wrap(text, width=50)

	if (number%2==0):
		for line in lines:
			draw.text((x-1, y), line, font=font, fill=text_color_outline)
			draw.text((x+1, y), line, font=font, fill=text_color_outline)
			draw.text((x, y-1), line, font=font, fill=text_color_outline)
			draw.text((x, y+1), line, font=font, fill=text_color_outline)
			draw.text((x, y), line, font=font, fill=text_color)
			y += line_size
	else:
		for line in lines:
			draw.text((x-1, y), line, font=font, fill=text_color_outline)
			draw.text((x+1, y), line, font=font, fill=text_color_outline)
			draw.text((x, y-1), line, font=font, fill=text_color_outline)
			draw.text((x, y+1), line, font=font, fill=text_color_outline)
			draw.text((x, y), line, font=font, fill=text_color2)
			y += line_size


def piece(actors, xp):
	actor_name = re.sub(r'(.txt)', '', actors)
	
	sys.stdout.write("{0} {1}/{2} \r".format(actor_name, xp, numlines))
	sys.stdout.flush()
	#print(actor_name)
	if not os.path.exists(output_dir+actor_name):
		os.mkdir(output_dir+actor_name)
	output = actor_name+"/"+actor_name

	create_list(output)
	create_title(actor_name, output)
	create_imdb_info(output)





#Main Script
def test():

	count = open("list.csv")
	global numlines
	numlines = len(count.readlines())

	for xp in range(0, numlines):
		with open("list.csv") as f:
			mycsv = csv.reader(f)
			mycsv = list(mycsv)
			line_numbers = xp
			#print(xp)
			global actors
			actors=mycsv[line_numbers][0]
			piece(actors, xp)

test()