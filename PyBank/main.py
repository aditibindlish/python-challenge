import csv

# Path to collect data from the Resources folder
csv_path = "Resources/budget_data.csv"

# Open/create an output file and store it in my_report under Analysis folder
my_report = open('Analysis/Budget_Analysis.txt', 'w')

# inialise variables used
total_PL = 0            # to store total profit and loss over the period
months = 0              # to store total number of months in the dataset 
previous_plm= 1088983   # to store the first Profit/loss to be used in change in p/l
total_change = 0        # to store total of the change in p/l for calculating average of this change
Max = ['',0]            # to store greatest total increase and corresponding date in a list 
Min = ['',0]            # to store greatest total decrease and corresponding date in a list 

# Open the source file in read mode and store it in csvfile and then read this file on commas
with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# iterate to the next row
    next(csvreader)


#loop through the data row wise and refer to each row under variable with same name    
    for row in csvreader: 
        pl_m = int(row[1])                  #store monthly profit/loss data in a variable
        total_PL+= pl_m                     #find running total of monthly proft/loss data
        months += 1                         #counter to count number of months
        change = pl_m - previous_plm        #calculate change in proft/loss
        total_change += change              #calculate total of this change
        previous_plm = pl_m                 #update the previous month data in the corresponding variable
       
        #    calculate greatest increase
        if change > Max[1]:
            Max[1] = change
            Max[0] = row[0]
        
        #    calculate greatest decrease
        if change < Min[1]:
            Min[1] = change
            Min[0] = row[0]


# create a readable output format
output = f'''
  Financial Analysis
  ----------------------------
  Total Months: {months}
  Total: ${total_PL:,.2f}
  Average Change: ${total_change/(months-1):,.2f}
  Greatest Increase in Profits: {Max[0]} ${Max[1]:,.2f}
  Greatest Decrease in Profits: {Min[0]} ${Min[1]:,.2f}
  '''

print(output)

# write the output in the Budget_Abalysis.txt file created earlier  
my_report.write(output)