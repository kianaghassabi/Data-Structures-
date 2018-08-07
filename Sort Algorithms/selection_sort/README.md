# Selection Sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from the unsorted part and putting it at the beginning. 

The array will have two parts in this process. A subarray which is sorted and other subarrays which is yet to be sorted.

![](https://github.com/kianaghss/python/blob/master/Sort%20Algorithms/selection_sort/selectionSort.gif)


## How does it work?

 1-First, it finds the smallest element in the array.
 
 2-Exchange that smallest element with the element at the first position.
 
 3-Then find the second smallest element and exchange that element with the element at the second position.
 
 4-This process continues until the complete array is sorted.



## Time complexity


    Worst Case Time Complexity [ Big-O ]: O(n^2)
    Best Case Time Complexity [Big-omega]: O(n^2)
    Average Time Complexity [Big-theta]: O(n^2)


  Worst case (Reverse List)

![worst case](https://github.com/kianaghss/python/blob/master/Sort%20Algorithms/selection_sort/SelectionSort_worst_case.gif)  

  Average Case
  
![Average case](https://github.com/kianaghss/python/blob/master/Sort%20Algorithms/selection_sort/SelectionSort_Avg_case.gif) 


## Space Complexity
    
    Space Complexity:O(1)
    
    
### Advantage over Bubble Sort

In Selection sort, a maximum of n swap operations are required, whereas in Bubble Sort, up to n swap operation happens for each element, so up to n2 total swap operation are required. These swap (write) operations are memory-intensive, so selection sort becomes even more efficient than Bubble sort for large lists.

In short, Selection Sort is used normally in cases where memory writes are quite expensive than memory reads.

However, both Selection and Bubble Sort take O(n2) time.

   
### Refrences:

   -[codepumpkin](https://codepumpkin.com/selection-sort-algorithms/)
   
