import csv
import os
def reorder(file, fileout, fieldnames, headerlines):
    if os.path.exists(fileout):
        os.remove(fileout)
    #get all fieldnames in order
    with open(file, 'r',encoding='utf-16') as f:
        reader = csv.reader(f)
        for i in range(headerlines):
            next(reader)
        firstrow = next(reader)
        for a in firstrow:
            if a not in fieldnames:
                fieldnames.append(a)
    #get the header line
    with open(file, 'r', encoding='utf-16') as infile, open('temp.csv', 'a', newline='',encoding='utf-16') as outfile:
        # output dict needs a list for new column ordering
        reader = csv.reader(infile)
        #save headerlines
        header = []
        for i in range(headerlines):
            header.append(next(reader))
        writer = csv.writer(outfile)
        for a in reader:
            writer.writerow(a)
    #re-oder file and output it to fileout
    with open('temp.csv', 'r', encoding='utf-16') as infile, open(fileout, 'a', newline='',encoding='utf-16') as outfile:
        #write headerlines
        writer = csv.writer(outfile)
        for h in header:
            writer.writerow(h)
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # reorder the header first
        writer.writeheader()
        reader = csv.DictReader(infile)
        for row in reader:
            # writes the reordered rows to the new file
            writer.writerow(row)
    os.remove("temp.csv")
#get the inputs from the user
print("Input the fieldnames you want to have at the front. E.g.'Axis [s],Background []'. Be careful with spaces! If there are no spaces infront of your fieldnames in the filem, don't put spaces after the comma!")
fields = input()
fields = fields.split(",")
print("How many headerlines do you have. A header is e.g. 'Channel.001' ")
headerlines = int(input())
#get all files from input folder
folder = os.listdir('input/')
for file in folder:
    input = 'input/'
    output = 'output/'
    input += file
    output +=file
    reorder(input, output, fields.copy(), headerlines)
