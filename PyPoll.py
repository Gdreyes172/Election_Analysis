# The data we need to retrieve
# 1) Get the total# of votes
# 2) Get a complete list of Candidates
# 3) Get the % of votes per Candidate
# 4) The total# of votes per Candidate
# 5) The winner of the election based on popular vote

# Open the data file
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("C:/Users/Gustavo/OneDrive/Documents/0001_DataAnalystCourse/03_Module3/Election_Analysis/Resources/election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Create a filename variable to a direct to indirect path to the file
file_to_save = os.path.join("C:/Users/Gustavo/OneDrive/Documents/0001_DataAnalystCourse/03_Module3/Election_Analysis/analysis",'election_analysis.txt')
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")