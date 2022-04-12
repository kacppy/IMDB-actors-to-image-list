import os, csv

f=open("list.csv",'a')
w=csv.writer(f)
for path, dirs, files in os.walk("txts"):
    for filename in files:
        w.writerow([filename])
