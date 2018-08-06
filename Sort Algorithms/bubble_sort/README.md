# Bubble Sort

Bubble Sort is a simple algorithm which is used to sort a given set of n elements provided in form of an array with n number of elements. Bubble Sort compares all the element one by one and sort them based on their values.

If the given array has to be sorted in ascending order, then bubble sort will start by comparing the first element of the array with the second element, if the first element is greater than the second element, it will swap both the elements, and then move on to compare the second and the third element, and so on.

If we have total n elements, then we need to repeat this process for n-1 times.

It is known as bubble sort, because with every complete iteration the largest element in the given array, bubbles up towards the last place or the highest index, just like a water bubble rises up to the water surface.

Sorting takes place by stepping through all the elements one-by-one and comparing it with the adjacent element and swapping them if required.

![Bubble_sort](https://github.com/kianaghss/python/blob/master/Sort%20Algorithms/bubble_sort/BubbleSort.gif)

## Complexity

In Bubble Sort, n-1 comparisons will be done in the 1st pass, n-2 in 2nd pass, n-3 in 3rd pass and so on. So the total number of comparisons will be,

    (n-1) + (n-2) + (n-3) + ..... + 3 + 2 + 1 
    Sum = n(n-1)/2 
    i.e O(n^2)

Hence the time complexity of Bubble Sort is O(n^2).

The main advantage of Bubble Sort is the simplicity of the algorithm.

The space complexity for Bubble Sort is O(1), because only a single additional memory space is required i.e. for temp variable.

Also, the best case time complexity will be O(n), it is when the list is already sorted.

Following are the Time and Space complexity for the Bubble Sort algorithm.

    Worst Case Time Complexity [ Big-O ]: O(n^2)
    Best Case Time Complexity [Big-omega]: O(n)
    Average Time Complexity [Big-theta]: O(n^2)
    Space Complexity: O(1)

## Refrences

   -[studytonight](https://www.studytonight.com/data-structures/bubble-sort)
   
   -[codepumpkin](https://codepumpkin.com/bubble-sort/)

