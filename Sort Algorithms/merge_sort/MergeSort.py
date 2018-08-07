
import random

# fill a specefic size of array with random values


def randomArray(sizeArray):
    lst = [None]*sizeArray
    for i in range(sizeArray):
        lst[i] = random.randint(1, 99999)
    return lst


# 1  mil array with random values
list = randomArray(1000000)

# action = 0


# def calculateAction():
#     action = action+1


def mergeSort(list):
    if len(list) > 1:
        # calculateAction()
        # split array in two equal section
        # find middle from round floor of list length
        middle = len(list)//2
        left = list[0:middle]
        right = list[middle:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
# when 2 spilited list have elements
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
# when left one is empty
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
# when left one is empty
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1


mergeSort(list)
print(list)
print("--------------------")
# print("Action: ", action)
