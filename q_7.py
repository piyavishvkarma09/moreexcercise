list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
list3=[]
for i in list2:
    if i in list1:
        # print(i)
        list3.append(i)
        list3.sort()
print(list3)
