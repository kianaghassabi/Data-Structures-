
import random

#  a specefic sized array filled with random values


def randomArray(sizeArray):
    lst = [None]*sizeArray
    for i in range(sizeArray):
        lst[i] = random.randint(1, 99999)
    return lst


# 1  mil array with random values
list = randomArray(1000000)


# def calculateAction():
#     action = action+1


def mergeSort(list):
    if len(list) > 1:
        # calculateAction()
        # split list into two equal sections
        # find the middle from round floor of list length
        middle = len(list)//2
        left = list[0:middle]
        right = list[middle:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
# when both spilited lists have elements to merge
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
