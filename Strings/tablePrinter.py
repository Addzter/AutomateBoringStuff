tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    iteration = 0
    lst1, lst2, lst3 = table
    
    for lst in table:
        for item in lst:
            print(lst1[iteration].rjust(10), lst2[iteration].rjust(10), lst3[iteration].rjust(10))
            iteration += 1
            
        if iteration > len(lst) - 1:
            break




printTable(tableData)
