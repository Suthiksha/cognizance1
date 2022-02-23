from prettytable import PrettyTable
Roll_no =['1','2','3']
Name = ['Clara','Sam','Susan']
Marks = ['95','85','90']
table = PrettyTable(['Roll_no','Name','Marks'])
for x in range(0,4):
    table.add_row([Roll_no[x],Name[x],Marks[x]])
    print (table)

