import csv


# Path to collect data from the Resources folder
csv_path = "Resources/election_data.csv"

# Open/create an output file and store it in my_report under Analysis folder
my_report = open('Analysis/Election_Result.txt', 'w')

# inialise variables used
total_votes = 0         # to store total votes casted 
candidates = {}         # to store candidate names as keys and vote count as values of the key   
candidates_Percentage = {} # to store candidate names as keys and percentage votes as values of the key

# Open the source file in read mode and store it in csvfile and then read this file on commas
with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# iterate to the next row
    next(csvreader)

#loop through the data row wise and.....     
    for row in csvreader:
        total_votes += 1        #calculate total votes counted
        
        if row[2] in candidates:
            candidates[row[2]] +=1
        else:
            candidates[row[2]] =1
    print(candidates)    

# extract value of dictionary

candidates_Percentage = {}.fromkeys(candidates)

new_cd=candidates_Percentage.keys()
for key in new_cd:
    candidates_Percentage[key]=(candidates[key])/total_votes
    print(f'{candidates_Percentage[key]:,%}')
 

newdict = {}
for key in new_cd:
    newdict[key] = [candidates[key],candidates_Percentage[key]]
print(f'new dict is {newdict}')


output = f'''
  Election Results
  -------------------------
  Total Votes: {total_votes}
  -------------------------'''
print(output)  

max = 0
for key in new_cd:
    print(key, ':' , newdict[key][1], ',(', newdict[key][0],')') 
    if candidates_Percentage[key]>max:
        max = candidates_Percentage[key]
        winner = key
print(f'''-------------------------
Winner: {winner}
-------------------------
''')




    

# write the output in the Budget_Abalysis.txt file created earlier  
my_report.write(output)

