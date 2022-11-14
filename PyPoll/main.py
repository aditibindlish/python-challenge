import csv


# Path to collect data from the Resources folder
csv_path = "Resources/election_data.csv"



# inialise variables used
total_votes = 0         # to store total votes casted 
candidates = {}         # to store candidate names as keys and vote count as values of the key in the dictionary  
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
    # print(candidates)    

# extract value of dictionary, store it in new dictionary 

candidates_Percentage = {}.fromkeys(candidates)

new_cd=candidates_Percentage.keys()
for key in new_cd:
    candidates_Percentage[key]=round((candidates[key])*100/total_votes,3)
    
 
# to store candidate name as key in a newdict with values as votes and percentage votes
newdict = {}
for key in new_cd:
    newdict[key] = [candidates[key],candidates_Percentage[key]]
# print(f'new dict is {newdict}')
# output3 = (f'''
# {newdict}
# ''')

output1 = f'''
  Election Results
  -------------------------
  Total Votes: {total_votes}
  -------------------------'''

print(output1)  

max = 0
for key in new_cd:
    print('    ', key, ':' , newdict[key][1],'%' ,',(', newdict[key][0],')') 
    if candidates_Percentage[key]>max:
        max = candidates_Percentage[key]
        winner = key
output2 =(f'''
  -------------------------
  Winner: {winner}
  -------------------------
''')
print(output2)



# Open/create an output file 'Election_Result.txt' and store it in variable my_report under Analysis folder

my_report = open('Analysis/Election_Result.txt', 'w')

# write the output in the Election_Result.txt file created above  

my_report.write(output1)

for k in newdict.keys():
    my_report.write("\n %s: %s%% ,(%s) \n" % (k,newdict[k][1],(newdict[k][0])))

my_report.write(output2)

