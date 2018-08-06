#defining the insertion sort function
def InsertionSort(mylist):   
    #The first item is already sorted so we start the for loop from the index=1
    for i in range(1,len(mylist)):
        current=mylist[i] #current variable known as a key
        j=i-1 #the last element for comparing
        while current< mylist[j] and j>=0:
            mylist[j+1]=mylist[j]
            j=j-1
        mylist[j+1]=current
    return mylist #return the sorted list

#defining the list
mylist=[0,20,10,4,6,9,11,2,3]

#calling a function
sorted=InsertionSort(mylist)

#displaying the result
print(sorted)