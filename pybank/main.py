import os
import csv

csvpath = os.path.join('..','pybank','budget_data.csv')


#Counting the number of months
count = 0
#Counting the net change respective month
month_of_change = []
#List for the net change
net_change_list = []
#Greatest increase list
greatinc = ["", 0]
#Greatest decrease list
greatdec = ["", 9999999999999999999]
#Calculating the total
total = 0

#Preparing the calculations of all
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)
    first_row=next(reader)
    count=count+1
    total = int(first_row[1])
    prev_net=int(first_row[1])
    net_change=0
    for row in reader:
        count = count+1
        total = total + int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change += row[0]
        if(greatinc[1]< net_change):
            greatinc[1]=net_change
            greatinc[0]=row[0]
        if(greatdec[1]>net_change):
            greatdec[1]=net_change
            greatdec[0]=row[0]
    avg_net = round(sum(net_change_list)/len(net_change_list),2)


print(f"Financial Analysis\n")
print(f"-------------------\n")
print(f"Total Months: {count}\n")
print(f"Total: ${total}\n")
print(f"Average Change: ${avg_net}\n")
print(f"Greatest Increase in Profits: {greatinc[0]} ({greatinc[1]})\n")
print(f"Greatest Decrease in Profits: {greatdec[0]} ({greatdec[1]})\n")

#Writing to CSV file
pybank_output = os.path.join("Resources", "pybank_output.csv")
with open(pybank_output, "w") as csvfile:
   csvwriter = csv.writer(csvfile, delimiter=',')
   csvwriter.writerow([f"Financial Analysis"])
   csvwriter.writerow([f"----------------------------"])
   csvwriter.writerow([f"Total Months: {count}"])
   csvwriter.writerow([f"Total: ${total}"])
   csvwriter.writerow([f"Average  Change: ${avg_net}"])
   csvwriter.writerow([f"Greatest Increase in Profits: {greatinc}"])
   csvwriter.writerow([f"Greatest Decrease in Profits: {greatdec}"])

#Writing to Text File
pybank_output2 = os.path.join("Analysis", "pybank_output.txt")
with open(pybank_output2,"w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Months: {count}\n")
    txt_file.write(f"Total: ${total}\n")
    txt_file.write(f"Average  Change: ${avg_net}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatinc}\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatdec}\n")
