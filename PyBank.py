mainimport os
import csv

csvpath = os.path.join('..','Data Analytics Bootcamp','budget_data.csv')


#Counting the number of months, and total $
count=0
total=0
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler, delimiter=',')
    next(reader)
    for row in reader:
        count=count+1
        total = total + int(row[1])


#Average, Greatest Increase & Decrease
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler)
    header = next(reader)
    first_row = next(reader)
    prev_net=int(first_row[1])
    net_change=0
    net_list=[]
    max_1=0
    min_1=0
    for row in reader:
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_list.append(net_change)
        if(max_1<net_change):
            max_1=net_change
        if(min_1>net_change):
            min_1=net_change

    avg_net = sum(net_list)/len(net_list)

print(f"Financial Analysis")
print(f"-------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_net}")
print(f"Greatest Increase in Profits: Aug-16 {max_1}")
print(f"Greatest Decrease in Profits: Feb-14 {min_1}")
