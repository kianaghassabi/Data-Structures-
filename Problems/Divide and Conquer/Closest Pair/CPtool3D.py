# Hosein Kangavar Nazari - IASBS 30 October
# Closest pair problem in 3D - needed tools

from math import floor

# specific class for holding minimum for 3D
class minimum:
    def __init__(self, x1_value, y1_value, x2_value, y2_value, z1_value, z2_value, distance):
        self.x1 = x1_value
        self.y1 = y1_value
        self.x2 = x2_value
        self.y2 = y2_value
        self.z1 = z1_value
        self.z2 = z2_value
        self.min_value = distance

    def set_value(self, x1_value, y1_value, x2_value, y2_value, z1_value, z2_value, distance):
        self.x1 = x2_value
        self.y1 = y2_value
        self.x2 = x2_value
        self.y2 = y2_value
        self.z1 = z1_value
        self.z2 = z2_value
        self.min_value = distance


def _distance(a=[], b=[]):
    return (((a[0]-b[0]) ** 2)+((a[1]-b[1]) ** 2) + ((a[2]-b[2]) ** 2))**(1/2)


#find in range elements for specefic elem from given set and return a subset
def subset_by_range(set, minRange, maxRange, elem):
    subset = []
    for i in range(0, len(set)):
        if set[i][elem] <= maxRange and set[i][elem] >= minRange:
            subset.append(set[i])
    return subset

# returns min of two given minimum objects 
def min_of_minimums(minOne, minTwo):
    if (minOne.min_value > minTwo.min_value):
        return minTwo
    else:
        return minOne

#binary search in arr from start
#to end element and search for value in specific elem
def binary_search(arr, start, end, value,elem):
    end = end - 1
    while( start < end):
        if(end - start == 1):
            if(arr[end-1][elem]<=value):
                return end-1
            else:
                return start
        else:
            middleValue = floor((start+end)/2)
            if(value == arr[middleValue][elem]):
                return middleValue
            elif(value > arr[middleValue][elem]):
                start = middleValue+1
            else:
                end=middleValue-1
    return start