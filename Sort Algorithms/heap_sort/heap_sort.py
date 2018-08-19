#define heapsort function
def heapsort(mylist):
    
    #Building heap
    heapsize=len(mylist)
    for i in range((heapsize//2)-1,-1,-1):
        heapify(mylist,heapsize,i)

    for i in range(heapsize-1,-1,-1):
        #swapping mylist[0] with mylist[i]
        temp=mylist[i]
        mylist[i]=mylist[0]
        mylist[0]=temp

        #heapifty
        heapify(mylist,i,0)

        

#define heapify
def heapify(mylist,heapsize,root):
    
    largest=root
    #defining children of nodes
    left_child=(2*root)+1
    right_child=(2*root)+2

    if left_child < heapsize and mylist[left_child] > mylist[largest]:
        largest=left_child

    if right_child < heapsize and mylist[right_child] > mylist[largest]:
        largest=right_child
    
    if largest != root :
        #swap
        temp=mylist[root]
        mylist[root]=mylist[largest]
        mylist[largest]=temp

        #calling heapify
        heapify(mylist,heapsize,largest)

#creating list
mylist=[3,2,11,6,7,5,43]

#callin function
heapsort(mylist)
print("sorted list : ",mylist)