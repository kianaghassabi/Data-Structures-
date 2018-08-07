# Insertion Sort

Insertion Sort is an algorithm used to sort a given list of items. It does so by iterating through the list and building the sorted output one item at a time. Upon each iteration, an item is taken from the list and inserted into the correct position by comparison with its neighbours. This process is repeated until we reach the last item and there are no more left to be sorted.

![](https://github.com/kianaghss/python/blob/master/Sort%20Algorithms/insertion_sort/Insertion-sort-example-300px.gif)

## How does it work?

  1-Get a list of unsorted numbers
  
  2-Set a marker for the sorted section after the first number in the list
  
  3-Repeat steps 4 through 6 until the unsorted section is empty
  
  4-Select the first unsorted number
  
  5-Swap this number to the left until it arrives at the correct sorted position
  
  6-Advance the marker to the right one position
  
  7-Stop

### Advantages:

1-It’s a simple algorithm to implement

2-Performance is very high when operating with small lists

3-Even more so when the list is already mostly sorted, as fewer iterations of the sorting logic need to take place

### Disadvantages:

1-Performance suffers when large lists are used, as this could involve carrying out a lot of comparisons and shifting of array items

2-The algorithm doesn’t perform as well as the merge sort and quick sort algorithms


## Time Complexity

In worst case,each element is compared with all the other elements in the sorted array. For n elements, there will be n^2 comparisons

    Worst Case Time Complexity [ Big-O ]: O(n^2)
    Best Case Time Complexity [Big-omega]: O(n)
    Average Time Complexity [Big-theta]: O(n^2)
    
## Space Complexity
    
    Space Complexity:O(1)
    
   
### Refrences:

   -[medium](https://medium.com/software-engineering-101/algorithms-insertion-sort-eec0e245ec42)

