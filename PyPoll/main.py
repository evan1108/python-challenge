
import csv
import os

election_data_csv = "election_data.csv"

# csvfile is the opened file
with open(election_data_csv, newline = '', encoding='utf8') as csv_file:

    # create an iterable list variable
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # skip header row
    next(csv_reader)

    candidates = []
    dict_candidates = {}

    row_count = 0

    # get all of the candidates and add them to a dictionary
    for row in csv_reader:
        row_count = row_count + 1
        if row[2] not in dict_candidates:
            dict_candidates[row[2]] = 1
        else:
            dict_candidates[row[2]] = dict_candidates[row[2]] + 1

    # loop through the candidate names and get the number of votes they received
    winner = ""
    most_votes = 0
    for key in dict_candidates:
        dict_candidates[key] = [dict_candidates[key], round(100*(dict_candidates[key]/row_count),4)]
        if dict_candidates[key][0] > most_votes:
            most_votes = dict_candidates[key][0]
            winner = key

    s = "O'Tooley"

    print('-'*40)
    print("Election Results")
    print('-'*40)
    print(f"Total Votes: {row_count}")
    print('-'*40)
    print(f"Khan: {dict_candidates['Khan'][1]}% ({dict_candidates['Khan'][0]})")
    print(f"Correy: {dict_candidates['Correy'][1]}% ({dict_candidates['Correy'][0]})")
    print(f"Li: {dict_candidates['Li'][1]}% ({dict_candidates['Li'][0]})")
    print(f"O'Tooley: {dict_candidates[s][1]}% ({dict_candidates[s][0]})")
    print('-'*40)
    print(f"Winner: {winner}")
    print('-'*40)


# write to an external file
output_path = "output2.txt"

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f"Total Votes: {row_count}"])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f"Khan: {dict_candidates['Khan'][1]}% ({dict_candidates['Khan'][0]})"])
    csvwriter.writerow([f"Correy: {dict_candidates['Correy'][1]}% ({dict_candidates['Correy'][0]})"])
    csvwriter.writerow([f"Li: {dict_candidates['Li'][1]}% ({dict_candidates['Li'][0]})"])
    csvwriter.writerow([f"O'Tooley: {dict_candidates[s][1]}% ({dict_candidates[s][0]})"])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(['----------------------------'])