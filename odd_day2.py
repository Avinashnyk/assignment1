list= [1,2,3,4,5,6,7,8,9,23,44,55,26,78,9876]

list1 = []
list2 = []

for i in list:
    if i % 2 == 0:
        list1.append(i)
    else:
        list2.append(i)
# print(list1)
# print(list2)        
print('Number of Even Numbers : ',len(list1))
print('Number of Odd Numbers : ', len(list2))        
