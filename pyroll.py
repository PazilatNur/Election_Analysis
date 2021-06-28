import os
import csv
file_to_load=os.path.join("election_results.csv")
file_to_save=os.path.join("analysis","election_analysis.txt")
total_vote=0
candidate_option=[]
candidate_vote={}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
  # To do: read and analyze the data here.
    file_reader=csv.reader(election_data)
# Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
      total_vote+=1   
      # print(total_vote)
      candidate_name=row[2]
      if candidate_name not in candidate_option:
        candidate_option.append(candidate_name)
        candidate_vote[candidate_name]=0

      candidate_vote[candidate_name]+=1
# print(candidate_option)
# print(candidate_vote)
with open(file_to_save,"w") as txt_file:
  election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_vote:,}\n"   #{total_vote:,} print number with , seperater
    f"-------------------------\n")
            #The "end" parameter below is added to ensure that nothing will be printed on the last line when the election_results. 
            # Anything code that is printed after print(election_results, end="") will be printed on a newline.

  txt_file.write(election_results)

  for candidate_name in candidate_vote:
    votes=candidate_vote[candidate_name]
    vote_percent=(votes/total_vote)*100
    # print(f"{candidate_name}: recieved {vote_percent:.1f}% of the total votes")
    candidate_results= (f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")
    
    #print(candidate_results)
    txt_file.write(candidate_results)

    if (votes > winning_count) and (vote_percent > winning_percentage):
      winning_count = votes
      winning_percentage = vote_percent
      winning_candidate = candidate_name

  winning_candidate_summary = (
      f"-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"-------------------------\n")
  print(winning_candidate_summary)
  txt_file.write(winning_candidate_summary)
    
