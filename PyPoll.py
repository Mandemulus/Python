import os
import csv

voter_Data = list()

total_Votes = 0

outString = ''

with open('election.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        total_Votes += 1
        voter_Data.append(row[2])
    else:

        outfile = open("PyPoll_Results.txt","w", newline='')
        outString = 'Total Votes:' + str(total_Votes) + '\n'
        outfile.write(outString)

        print('Total Votes:',total_Votes)
        sorted(voter_Data)
        s = set(sorted(voter_Data))
#        print(s, sep = "\n")
#        for x in range(len(voter_Data)):
#        for y in range(len(s)):
        for y in s:
#            print(y)
            print(f'{y:10} : {round(((voter_Data.count(y)/total_Votes)*100),3):5}%',end='')
            print(f'{voter_Data.count(y):10}')
#            print(y,':','\t',round(((voter_Data.count(y)/total_Votes)*100),3),
#           '%\t','(',voter_Data.count(y),')')

           
            outString = f'{y:10}'
            outString = outString + ' : '
            outString = outString + f'{str(round(((voter_Data.count(y)/total_Votes)*100),3)):5}'
            outString = outString + '% (' + f'{str(voter_Data.count(y)):10}' + ' )' + '\n'
            outfile.write(outString)

#        print(*voter_Data, sep = "\n")
#        print(voter_Data)
#        for candidate in voter_Data()
#            print(voter_Data.count(voter_Data[candidate]))
#        print(voter_Data)
#        print('Done')