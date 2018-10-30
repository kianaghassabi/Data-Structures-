# Hosein Kangavar Nazari - IASBS 30 October 2018
# Closest pair problem in 3D - using list sorted by x and y
# Time Compelexity:  O(nlog^2(n))

# CPtool: i put some common functions and classes which used in 3D Methods
from CPtool3D import _distance , minimum , min_of_minimums, subset_by_range


from operator import itemgetter
from math import floor
import time
start = time.time()

# reading from file
points = []
file_open = open("./Data/3D/dataGenerator3d.txt", "r")
#file_open = open("./Data/3D/iasbs12_3d.txt", "r")
data = file_open.read()

points = data.split("\n")

DS_standard = []
for i in range(1, len(points)):
    temp = points[i].split(" ")
    DS_standard.append([float(temp[0]), float(temp[1]), float(temp[2])])

sortedByZ = []
sortedByX = []
sortedByY = []

sortedByZ = sorted(DS_standard, key=itemgetter(2))
sortedByY = sorted(DS_standard, key=itemgetter(1))
sortedByX = sorted(DS_standard, key=itemgetter(0))

#assigning a null value as first member of list 
# [used for simpilisity in  indexing problems]
sortedByZ.insert(0, [-10000, -10000, -10000])
sortedByX.insert(0, [-10000, -10000, -10000])



def dccp_two(sortedX, start, end):
    # assign positive infinity to minG
    minG = minimum(0, 0, 0, 0,0,0, 1000.0)
    #if there is less than 4 point use brute force 
    if(end - start <= 2):
        for i in range(start, end):
            for j in range(i+1, end+1):
                minTemp = _distance(sortedX[i], sortedX[j])
                if (minTemp <= minG.min_value):
                    minG.x1 = sortedX[i][0]
                    minG.y1 = sortedX[i][1]
                    minG.z1 = sortedX[i][2]
                    minG.x2 = sortedX[j][0]
                    minG.y2 = sortedX[j][1]
                    minG.z2 = sortedX[j][2]
                    minG.min_value = minTemp
        return minG

    else:
        minL = dccp_two(sortedX, start, floor((end+start-1)/2))
        minR = dccp_two(sortedX, floor((end+start-1)/2)+1, end)
        minG = min_of_minimums(minL, minR)

        # rightest member of left , leftest member of right
        middle = (sortedX[floor((end+start-1)/2)][0] +
                  sortedX[floor((end+start-1)/2)+1][0])/2
        lowwerBoundX = middle - minG.min_value
        upperBoundX = middle + minG.min_value
     

        # making a strip of point sorted by y value 
        stripSorted = subset_by_range(sortedByY, lowwerBoundX, upperBoundX, 0)
        # for each member of strip at first we start from the lowwer bound by y 
        # and compute distance from next 6 elements
        for i in range(0, len(stripSorted)):
            # for each member of strip at first we start from the lowwer bound by y 
            # and compute distance from next 6 elements

            #6 is enough because we just want to look elements that 
            # are after this so points have higher value on that specific
            # element so its a cube and we can put 6 number of point there 
            # so if you use more than 6 numbers, results are the same
 
            if(i + 6 > len(stripSorted)):
                counter = 0
                upper = len(stripSorted)
            else:
                upper = i+6
                counter = 0
            for j in range(i+1, upper):
                counter +=1

                minTemp = _distance(stripSorted[i], stripSorted[j])
                if (minTemp < minG.min_value):
                    minG.x1 = stripSorted[i][0]
                    minG.y1 = stripSorted[i][1]
                    minG.z1 = stripSorted[i][2]
                    minG.x2 = stripSorted[j][0]
                    minG.y2 = stripSorted[j][1]
                    minG.z2 = stripSorted[j][2]
                    minG.min_value = minTemp
# lots of code should be wirte there
# if the result is zero its because  we putted a point in two side or two point in data set are the same
        return minG

def dccp_3d_two(sortedZ, sortedX, start, end):
    # assign positive infinity to minG
    minG = minimum(0, 0, 0, 0, 0, 0, 100000)
    #if there is less than 4 point use brute force 
    if(end - start <= 2):
        for i in range(start, end):
            for j in range(i+1, end+1):
                minTemp = _distance(sortedZ[i], sortedZ[j])
                if (minTemp <= minG.min_value):
                    minG.x1 = sortedZ[i][0]
                    minG.y1 = sortedZ[i][1]
                    minG.z1 = sortedZ[i][2]
                    minG.x2 = sortedZ[j][0]
                    minG.y2 = sortedZ[j][1]
                    minG.z2 = sortedZ[j][2]
                    minG.min_value = minTemp
        return minG

    else:
        minL = dccp_3d_two(sortedZ, sortedX, start, floor((end+start-1)/2))
        minR = dccp_3d_two(sortedZ, sortedX, floor((end+start-1)/2)+1, end)
        minG = min_of_minimums(minL, minR)

        middle = (sortedZ[floor((end+start-1)/2)][2] +
                  sortedZ[floor((end+start-1)/2)+1][2])/2
        lowwerBoundZ = middle - minG.min_value
        upperBoundZ = middle + minG.min_value

        # here we should find point in this strip
        strip3D = subset_by_range(sortedX, lowwerBoundZ, upperBoundZ, 2)
        #assigning a null value as first member of list 
        # [used for simpilisity in  indexing problems]
        strip3D.insert(0, [-10000, -10000, -10000])

        minTemp = dccp_two(strip3D, 1, len(strip3D)-1)

        if (minTemp.min_value <= minG.min_value):
            minG.x1 = minTemp.x1 
            minG.y1 = minTemp.y1
            minG.z1 = minTemp.z1
            minG.x2 = minTemp.x2
            minG.y2 = minTemp.y2
            minG.z2 = minTemp.z2
            minG.min_value = minTemp.min_value
        return minG

# print(sortedByX)


Answer = dccp_3d_two(sortedByZ, sortedByX, 1, len(sortedByZ)-1)
print("The answer is :", Answer.min_value)

end = time.time()
print("Time:", end - start)
