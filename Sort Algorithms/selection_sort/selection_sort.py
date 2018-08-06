#defining the selection sort function
def Selection_sort(mylist):
    for i in range (0,len(mylist)-1):
        minimum=i #the element is set to the minumum

        #checking whether the other elements are smaller than the current minimum
        for j in range (i+1,len(mylist)):
            if mylist[j] < mylist[minimum]:
                minimum=j
        #swapping the minimum element with the current min
        temp=mylist[i]
        mylist[i]=mylist[minimum]
        mylist[minimum]=temp

    return mylist

#defining list
mylist=[4,19,7,16,3,21,1,0,11,80]

#calling the sort function for the list
sorted=Selection_sort(mylist)

#displaying the sorted list
print(sorted)
