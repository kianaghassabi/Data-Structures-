
#defining the sort function
def counting_sort(list):
    
    sortedlist=[]

    max_element=findmaximum(list)

    #creating a list for counting the occurence of the elements
    countinglist=[0]*(max_element+1)

    for i in mylist:
        countinglist[i]+=1

    for i in range(len(countinglist)-1):
        while countinglist[i]>0:
            sortedlist.append(i)
            countinglist[i]-=1

    return sortedlist
       
#definin the function for finding the maximum number in a given list 
def findmaximum(mylist):
    maximum=mylist[0]
    for i in range(len(mylist)):
        if mylist[i]>maximum:
            temp=maximum
            maximum=mylist[i]
    return maximum


#creating a list to be sorted
mylist=[1,4,3,2,2,9,4,5]
result=findmaximum(mylist)

#calling the function
sorted=counting_sort(mylist)
print("sorted list: ",sorted)