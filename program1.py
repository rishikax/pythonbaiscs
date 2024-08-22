# create a program to write mathematical tables of any number, and save it to a list

def mathTable(n): # takes one argument as the number for which we need a table
    table = []
    for i in range(1,11):
        multip = i * n
        table.append(multip)
    return table # returns the list which has all the elements of the table

tableofTwo = mathTable(2)
print(tableofTwo)

tableof49 = mathTable(49)
print(tableof49)