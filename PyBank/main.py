import csv

csv_path = "Resources/budget_data.csv"

total_PL = 0
max = 0
min = 0

with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    for row in csvreader:    
        total_PL = total_PL + int(row[1])

        print(f"the total: {total_PL}")
 
    for count, value in enumerate(csvreader):
        print(count, value)
