import os
import threading
import pandas as pd
import numpy as np

def main():
    print("Parliament Election 2024\n")
    key = 4209
    auth = int(input("Enter Key to start the election: "))
    
    if auth == key:
        election_data = pd.read_excel("election_result.xlsx")
        
        for i in range(len(election_data)):
            print("\nParliament Election 2024.")
            print(f"\nName: {election_data.iloc[i]['Name']}")
            print(f"\nContact: {election_data.iloc[i]['Contact']}")
            
            voter_id = int(input("\nEnter Voter ID: "))
            if election_data.iloc[i]["Voter id"] == voter_id:
                print("\nFor Voting Press No of your Party\n")
                print("BJP: 1\nNCP: 2\nSHIVSENA: 3\n")
                
                vote_options = int(input("Now Vote Your Party: "))
                if vote_options == 1:
                    vote = "BJP"
                elif vote_options == 2:
                    vote = "NCP"
                elif vote_options == 3:
                    vote = "SHN"
                else:
                    print("Invalid option.")
                    continue  
                
                election_data.at[i, "Vote"] = vote
                print(f"Vote recorded: {election_data.iloc[i]['Vote']}")
                
                if os.name == 'nt':
                    os.system("cls")
            
        
        auth = int(input("Enter Key for Result of election:  "))
        if auth == key:    
            print("Getting results ready.....\n")
            def result_display():
                print("Parliament Election 2024\n")
                bjp = (election_data["Vote"] == "BJP").sum()
                ncp = (election_data["Vote"] == "NCP").sum()
                shivsena = (election_data["Vote"] == "SHIVSENA").sum()
                result = max([bjp, ncp, shivsena])
                if result == bjp:
                    print(f"BJP is the winner in this election with {bjp} votes")
                elif result == ncp:
                    print(f"NCP is the winner in this election with {ncp} votes")
                elif result == shivsena:
                    print(f"SHIVSENA is the winner in this election with {shivsena} votes")
                election_data.to_excel("election_result1.xlsx", index=False)
                
            timer = threading.Timer(4.0, result_display)
            timer.start()
    else:
        print("Error: Authentication Failed.")
          
if __name__ == "__main__":
    main()
