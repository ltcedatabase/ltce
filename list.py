list=[]
num=int(input('enter total number of elements in the list:'))
for n in range(num):
    elements=int(input('enter number'))
    list.append(elements)
    print('sum of elements in given list is:',sum(list))
