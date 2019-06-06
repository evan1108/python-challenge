import os
import csv

# file path
# budget_data_csv = os.path.join("..", "..", "..", "NUCHI201905DATA2","03-Python","Homework","PyBank", "Resources", "budget_data.csv")
# budget_data_csv = "../../../NUCHI2019DATA2/03-Python/Homework/PyBank/Resources/budget_data.csv"
budget_data_csv = "budget_data.csv"

# csvfile is the opened file
with open(budget_data_csv, newline = '', encoding='utf8') as csv_file:

    # create an iterable list variable
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # skip header row
    next(csv_reader)

    # instantiate variables
    num_months = 0
    total_pl = 0
    min_pl = 0
    min_pl_month = ""
    max_pl = 0
    max_pl_month = ""

    # loop through the rows in the file and get P&L max, mins, number of months
    for row in csv_reader:
        num_months = num_months + 1
        total_pl = total_pl + int(row[1])
        if int(row[1]) < min_pl:
            min_pl = int(row[1])
            min_pl_month = row[0]
        elif int(row[1]) > max_pl:
            max_pl = int(row[1])
            max_pl_month = row[0]
    
    average_pl = round(total_pl/num_months, 2)

print('Financial Analysis')
print('----------------------------')
print(f"Total Months: {num_months}")
print(f"Total: {total_pl}")
print(f"Average Change: {average_pl}")
print(f"Greatest Increase in Profits: {max_pl_month} ({max_pl})")
print(f"Greatest Decrease in Profits: {min_pl_month} ({min_pl})") 


output_path = "output.txt"

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Months: '+ str(num_months)])
    csvwriter.writerow([f'Total: {total_pl}'])
    csvwriter.writerow([f"Average Change: {average_pl}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {max_pl_month} ({max_pl})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {min_pl_month} ({min_pl})"])