import os
import csv
file_to_load=os.path.join("election_results.csv")
file_to_save=os.path.join("analysis","election_analysis.txt")
total_vote=0
candidate_option=[]
candidate_vote={}
county_option=[]
county_vote={}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_county=""
winning_vote = 0
winning_percent = 0

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
    #pull subtotal votes for each county
      county_name=row[1]
      if county_name not in county_option:
        county_option.append(county_name)
        county_vote[county_name]=0
      county_vote[county_name]+=1
    # print(county_vote)
        

      
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
  txt_file.write("Election Results By Counties: \n")

  for county_name in county_vote:
    c_vote=county_vote[county_name]
    c_vote_percent=(float(c_vote)/float(total_vote))*100
    c_results= (f"{county_name}: {c_vote_percent: .1f}%  ({c_vote})\n")
    # print(c_results)
    txt_file.write(c_results)

    if(c_vote > winning_vote) and (c_vote_percent>winning_percent):
      winning_vote=c_vote
      winning_percent=c_vote_percent
      winning_county=county_name
  txt_file.write(f"-------------------------\n")
  txt_file.write(f"The county with the highest turnout: {winning_county}\n")
  txt_file.write(f"-------------------------\n")
  txt_file.write("Election Results By Candidate: \n")
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
    
