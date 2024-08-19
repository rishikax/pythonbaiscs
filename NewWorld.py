## python file to make 2 lists and append 5 elements to each list and extend both the list and create a new extended list
list1 = [1,2]
list2 = [3,4]

appendingElements = [2,4,6,8,10]

for i in appendingElements:
    list1.append(i)
    list2.append(i)

print(list1)
print(list2)

list1.extend(list2)

print(list1)