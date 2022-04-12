#Configuration
names = 'names.csv'


import csv, re
from imdb import IMDb
ia = IMDb()

def scrap():
	#person = ia.search_person(find)
	#print(person[0]['name'])

	full_person = ia.get_person(find, info=["filmography"])
	print(full_person["name"])
	output = "txts/%s.txt"%(full_person["name"])
	try:
		dd = full_person["filmography"]
	except:
		dd=full_person
		pass
	for x in range(5):
		try:
			if (dd[x]["actress"]):
				dd=dd[x]
				break
		except:
			pass

	for x in range(5):
		try:
			if (dd[x]["actor"]):
				dd=dd[x]
				break
		except:
			pass
	file = open(output,"w") 

	try:
		for mov in dd["actress"]:
			try:
				#print(mov.keys())
				#print("%s - %s" %(mov["year"], mov["title"]))
				#print(mov.keys())
				if mov["kind"]=="movie":
					kind = ""
				else:
					kind = "(%s)" %(mov["kind"].title())
				file.write("%s - %s %s \r\n" %(mov["year"], mov["title"], kind)) 
			except:
				if mov["kind"]=="movie":
					kind = ""
				else:
					kind = "(%s)" %(mov["kind"].title())
				year = re.match(r'.*([1-2][0-9]{3}-[1-2][0-9]{3})', mov["title"])
				mov = re.sub(r'(\([1-2][0-9]{3}-[1-2][0-9]{3}\))', '', mov["title"])
				if year is not None:
					# Then it found a match!
					#print ("%s - %s" %(year.group(1), mov))
					file.write("%s - %s %s  \r\n" %(year.group(1), mov, kind)) 
	except:
		try:
			for mov in dd["actor"]:
				try:
					#print("%s - %s" %(mov["year"], mov["title"]))
					#print(mov.keys())
					if mov["kind"]=="movie":
						kind = ""
					else:
						kind = "(%s)" %(mov["kind"].title())
					file.write("%s - %s %s  \r\n" %(mov["year"], mov["title"], kind)) 
				except:
					if mov["kind"]=="movie":
						kind = ""
					else:
						kind = "(%s)" %(mov["kind"].title())
					year = re.match(r'.*([1-2][0-9]{3}-[1-2][0-9]{3})', mov["title"])
					mov = re.sub(r'(\([1-2][0-9]{3}-[1-2][0-9]{3}\))', '', mov["title"])
					if year is not None:
						# Then it found a match!
						#print ("%s - %s" %(year.group(1), mov))
						file.write("%s - %s %s \r\n" %(year.group(1), mov, kind)) 
		except:
			dwa(output)
			

	
	file.close()
	file = open(output, "r")
	list = file.readlines()
	file.close()

	list.reverse()

	file = open(output, "w")
	for value in list:
		file.write(value)
	file.write("\r\n\r\nhttps://www.imdb.com/name/nm%s/" %(find))

	file.close()



def dwa(output):
	#person = ia.search_person(find)
	#print(person[0]['name'])

	full_person = ia.get_person(find, info=["filmography"])
	try:
		dd = full_person["filmography"]
	except:
		dd=full_person
		pass
	for x in range(10):
		try:
			if (dd[x]["actress"]) or (dd[x]["actor"]):
				dd=dd[x]
				break
		except:
			pass
	file = open(output,"w") 

	try:
		for mov in dd[0]["actress"]:
			try:
				#print("%s - %s" %(mov["year"], mov["title"]))
				#print(mov.keys())
				if mov["kind"]=="movie":
					kind = ""
				else:
					kind = "(%s)" %(mov["kind"].title())
				file.write("%s - %s %s \r\n" %(mov["year"], mov["title"], kind)) 
			except:
				if mov["kind"]=="movie":
					kind = ""
				else:
					kind = "(%s)" %(mov["kind"].title())
				year = re.match(r'.*([1-2][0-9]{3}-[1-2][0-9]{3})', mov["title"])
				mov = re.sub(r'(\([1-2][0-9]{3}-[1-2][0-9]{3}\))', '', mov["title"])
				if year is not None:
					# Then it found a match!
					#print ("%s - %s" %(year.group(1), mov))
					file.write("%s - %s %s  \r\n" %(year.group(1), mov, kind)) 
	except:
		try:
			for mov in dd[0]["actor"]:
				try:
					#print("%s - %s" %(mov["year"], mov["title"]))
					#print(mov.keys())
					if mov["kind"]=="movie":
						kind = ""
					else:
						kind = "(%s)" %(mov["kind"].title())
					file.write("%s - %s %s  \r\n" %(mov["year"], mov["title"], kind)) 
				except:
					if mov["kind"]=="movie":
						kind = ""
					else:
						kind = "(%s)" %(mov["kind"].title())
					year = re.match(r'.*([1-2][0-9]{3}-[1-2][0-9]{3})', mov["title"])
					mov = re.sub(r'(\([1-2][0-9]{3}-[1-2][0-9]{3}\))', '', mov["title"])
					if year is not None:
						# Then it found a match!
						#print ("%s - %s" %(year.group(1), mov))
						file.write("%s - %s %s \r\n" %(year.group(1), mov, kind)) 
		except:
			try:
				for mov in dd[0]["self"]:
					try:
						#print("%s - %s" %(mov["year"], mov["title"]))
						#print(mov.keys())
						if mov["kind"]=="movie":
							kind = ""
						else:
							kind = "(%s)" %(mov["kind"].title())
						file.write("%s - %s %s \r\n" %(mov["year"], mov["title"], kind)) 
					except:
						if mov["kind"]=="movie":
							kind = ""
						else:
							kind = "(%s)" %(mov["kind"].title())
						year = re.match(r'.*([1-2][0-9]{3}-[1-2][0-9]{3})', mov["title"])
						mov = re.sub(r'(\([1-2][0-9]{3}-[1-2][0-9]{3}\))', '', mov["title"])
						if year is not None:
							# Then it found a match!
							#print ("%s - %s" %(year.group(1), mov))
							file.write("%s - %s %s  \r\n" %(year.group(1), mov, kind))
			except:
				file.write("Aktor prawdopodobnie nie zagrał w żadnym filmie") 



with open("settings.csv") as f:
	mycsv = csv.reader(f)
	mycsv = list(mycsv)
	start = int(mycsv[0][0])



file = open(names)
numline = len(file.readlines())
for x in range(start, numline):
	with open(names) as f:
		mycsv = csv.reader(f)
		mycsv = list(mycsv)
		line_number = x

		data=mycsv[line_number][1]
		fn = re.search(r'([0-9][0-9]{6})', data)

		#print(fn.group(1))
		find=fn.group(1)
		verificationErrors = []
		while True:
			try:
				scrap()
				with open('settings.csv', mode='w') as employee_file:
					setting = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
					setting.writerow([line_number])
				break
			except:
				pass
