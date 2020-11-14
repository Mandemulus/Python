import os
import csv
#average_Change = 0.00
amount = list()
date = list()
amount_diff = list()

#amt_diff = 0.00

min_Profit_Loss = 0
min_Index = 0
min_Profit_Loss_Prior = 0

max_Profit_Loss = 0
max_Index = 0
max_Profit_Loss_Prior = 0

outString = ''

length = 0.00
i = 1


with open('budget_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)     # reads the header line and does nothing with it
    for row in reader:
        date.append(str(row[0]))
        amount.append(int(row[1]))
    else:
        length = len(amount)
        print("Total Months: ", len(amount))
        print(f'Total Amount: ${sum(amount):8d}')
        while(i < len(amount)):
            amount_diff.append((amount[i])-(amount[i-1]))
            i += 1
        else:
            print(f'Average Change: ${round((sum(amount_diff) / len(amount_diff)),2)}')
           
max_Profit_Loss = max(amount)
max_Index = amount.index(max(amount))
max_Profit_Loss_Prior = (amount[max_Index-1])

min_Profit_Loss = min(amount)
min_Index = amount.index(min(amount))
min_Profit_Loss_Prior = (amount[min_Index-1])

print('Greatest Increase in Profits:',date[max_Index],
    '$(',abs(max_Profit_Loss) + abs(max_Profit_Loss_Prior),')')
print('Greatest Decrease in Profits:',date[min_Index],
    '$(',(abs(min_Profit_Loss) + abs(min_Profit_Loss_Prior))*-1,')')

outfile = open("Analysis/PyBank_Results.txt","w", newline='')
outString = 'Average Change: $' + str(round((sum(amount_diff) / len(amount_diff)),2)) + '\n'
outfile.write(outString)
outString = 'Greatest Increase in Profits:' + str(date[max_Index])  
outString = outString + '($'
outString = outString + str(abs(max_Profit_Loss) + abs(max_Profit_Loss_Prior)) + ')' + '\n'
outfile.write(outString)
outString = 'Greatest Decrease in Profits:' + date[min_Index]
outString = outString + '($' + str((abs(min_Profit_Loss) + abs(min_Profit_Loss_Prior))*-1)
outString = outString + ')' + '\n'
outfile.write(outString)
   
outfile.close()






