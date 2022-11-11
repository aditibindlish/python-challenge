import csv


# Path to collect data from the Resources folder
csv_path = "Resources/election_data.csv"

# Open/create an output file and store it in my_report under Analysis folder
my_report = open('Analysis/Election_Result.txt', 'w')

# inialise variables used
total_votes = 0         # to store total votes casted 
candidates = set()    # to store unique candidate names in a set   


# Open the source file in read mode and store it in csvfile and then read this file on commas
with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# iterate to the next row
    next(csvreader)

#loop through the data row wise and refer to each row under variable with same name    
    for row in csvreader:
        total_votes += 1        #calculate total votes counted
        candidates.add(row[2])  #add each new candidate as an element in the set
    print(candidates)           #print list of candidates as a set



## routine for vote Count

# Open the source file in read mode and store it in csvfile and then read this file on commas
with open(csv_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# iterate to the next row
    next(csvreader)

    # Initialize a dictionary to store names against vote counts, dictionary has default values zero and keys from the set candidates
    vote_count = {candidate: 0 for candidate in candidates}
    print(vote_count)
    candidates_list = list(vote_count.keys()) # store candidate names in a list to access each element using index of the list

    #  Loop through the csv file and count each occurence of candidate name....
    for row in csvreader:
        
        if row[2] == candidates_list[0]:
            vote_count[candidates_list[0]] += 1
        
        elif row[2] == candidates_list[1]:
            vote_count[candidates_list[1]] +=1
        
        elif row[2] == candidates_list[2]:
            vote_count[candidates_list[2]] +=1

    
    print(vote_count)
    





# create a readable output format
output = f'''
  Election Results
  -------------------------
  Total Votes: {total_votes}
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  '''
print(output)

