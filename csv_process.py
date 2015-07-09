#!/usr/bin/python
import csv
with open('csv_input.csv') as inpfile:
    with open('csv_output.csv', 'w') as outfile:
        reader = csv.DictReader(inpfile)
        writer = csv.DictWriter(outfile,'Last Name,First Name,Gender,Marital Status,Birth Order,Quote'.split(','))
        writer.writeheader()
        for row in sorted(reader, key=lambda x:int(x['Birth Order'])):
            if row['Gender'] == 'M':
                row['Gender'] = 'Male'
            elif row['Gender'] == 'F':
                row['Gender'] = 'Female'
            writer.writerow(row)
