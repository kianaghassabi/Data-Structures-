#defining a bubble sort function
def bubbleSort(mylist):
    for j in range(len(mylist)-1,0,-1):
        for i in range(0,j): 
            if mylist[i] > mylist[i+1]: #swap the the numbers using the temp variable 
                temp=mylist[i]
                mylist[i]=mylist[i+1]
                mylist[i+1]=temp
    return mylist

#defining list
mylist=[4,9,7,6,3,2,1,90,11,80]

#calling the sort function for the list
sorted=bubbleSort(mylist)

#displaying the sorted list
print(sorted)
