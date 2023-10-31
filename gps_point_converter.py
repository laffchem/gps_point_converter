import csv
import os
import re

# Change this to whatever directory you're using.
os.chdir(r"\\apk-fs\ApkUsers$\JLaffey\Desktop")
print(os.getcwd())
# Blank list to append your stuff to
points = []

# Name the text file
text_file = input('Input the textfile name')
text_file = text_file + '.txt'

# Name your csv file
csv_file = input('What is your csv file going to be called?')
csv_file = csv_name + '.csv'

# Open the text file, just change out the name. The parenthesis are due to how the ipad copies the text values
with open(text_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('(', '').replace(')', '')
        line = line.split(',')
        points.append(line)
        # print(line)

# This removes the inevitable \n value for the new line
for point in points:
    for i in range(len(point)):
        point[i] = re.sub(r'\n', '', point[i])

# Recreates the list with list comp
points = [point for point in points if point != ['']]
print(points)


# Writes the csv file
with open(csv_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['y', 'x'])
    for point in points:
        writer.writerow(point)

f.close()
