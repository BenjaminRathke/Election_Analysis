# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# #. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote.

#Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
  
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total votes varialble
total_votes = 0

# Initialize a list variable to hold candidate names
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1
        
        # Retrieve candidate name from the current iteration's row
        candidate_name = row[2]
        
        # Add candidate name to the candidate_options list using the append() method if it has not been added to the candidate_options list from line 22 yet.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
                                 
# Print candidate options
print(candidate_options)

# Print the total votes.
print(total_votes)




    

        