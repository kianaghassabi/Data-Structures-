# Hosein Kangavar Nazari - IASBS 30 October 2018
# Closest pair problem in 3D - [ x & y sorted ]
# Time Compelexity:  O(nlog^2(n))


# CPtool: i put some common functions and classes which used in 3D Methods
from CPtool3D import _distance , minimum , min_of_minimums , subset_by_range

from operator import itemgetter
from math import floor
import time

# reading from file

file_open = open("./Data/3D/dataGenerator3d.txt", "r")
#file_open = open("./Data/3D/iasbs12_3d.txt", "r")
data = file_open.read()
points = data.split("\n")

DS_standard = []
for i in range(1, len(points)):
    temp = points[i].split(" ")
    DS_standard.append([float(temp[0]), float(temp[1]), float(temp[2])])

sortedZ = []
sortedX = []

sortedZ = sorted(DS_standard, key=itemgetter(2))
#assigning a null value as first member of list 
# [used for simpilisity in  indexing problems]
sortedZ.insert(0, [-10000, -10000, -10000])


def dccp_three(sortedX,sortedY, start, end):
    # assign positive infinity to minG
    minG = minimum(0, 0, 0, 0, 0, 0, 100000)
    #if there is less than 4 point use brute force 
    if(end - start <= 2):
        for i in range(start,end):
            for j in range(i+1,end+1):
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
        minL = dccp_three(sortedX,sortedY, start, floor((end+start-1)/2))
        minR = dccp_three(sortedX,sortedY, floor((end+start-1)/2)+1, end)
        minG = min_of_minimums(minL, minR)

        # rightest member of left , leftest member of right
        middle = (sortedX[floor((end+start-1)/2)][0] +
                  sortedX[floor((end+start-1)/2)+1][0])/2
        lowerBound = middle - minG.min_value
        upperBound = middle + minG.min_value

        strip = subset_by_range(sortedY,lowerBound,upperBound,0)
        # print (len(strip))
        for i in range(0,len(strip)):
            for j in range(i+1,len(strip)):
                if(abs(strip[i][1]-strip[j][1]) > minG.min_value):
                    break
                minTemp = _distance(strip[i],strip[j])
            
                if (minTemp < minG.min_value):
                    minG.x1 = strip[i][0]
                    minG.y1 = strip[i][1]
                    minG.z1 = strip[i][2]
                    minG.x2 = strip[j][0]
                    minG.y2 = strip[j][1]
                    minG.z2 = strip[j][2]
                    minG.min_value = minTemp
        # if the result is zero its because  we putted a point in two side or two point in data set are the same
        return minG


def dccp_3d_three(start, end):
    # assign positive infinity to minG
    minG = minimum(0, 0, 0, 0, 0, 0, 1000000)
    #if there is less than 4 point use brute force 
    if(end - start <= 2):
        for i in range(start, end):
            for j in range(i+1, end):
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
        minL = dccp_3d_three(start, floor((end+start-1)/2))
        minR = dccp_3d_three(floor((end+start-1)/2)+1, end)
        minG = min_of_minimums(minL, minR)

        middle = (sortedZ[floor((end+start-1)/2)][2] +
                  sortedZ[floor((end+start-1)/2)+1][2])/2
        lowerBoundZ = middle - minG.min_value
        upperBoundZ = middle + minG.min_value

        # here we should find point in this strip
        strip3D = subset_by_range(sortedZ[start:end], lowerBoundZ, upperBoundZ, 2)
        #tempSortedY=subset_by_range(sortedYGlobal,lowerBoundZ,upperBoundZ,2) 
        tempSortedY=sorted(strip3D,key=itemgetter(1)) 
        #assigning a null value as first member of list 
        # [used for simpilisity in  indexing problems]
        strip3D=sorted(strip3D,key=itemgetter(0))
        strip3D.insert(0, [-10000, -10000, -10000])
        minTemp = dccp_three(strip3D,tempSortedY, 1, len(strip3D)-1)

        if (minTemp.min_value <= minG.min_value):
            minG.x1 = minTemp.x1 
            minG.y1 = minTemp.y1
            minG.z1 = minTemp.z1
            minG.x2 = minTemp.x2
            minG.y2 = minTemp.y2
            minG.z2 = minTemp.z2
            minG.min_value = minTemp.min_value
        return minG
start = time.time()
Answer = dccp_3d_three( 1, len(sortedZ))
end = time.time()

print("The answer is :", Answer.min_value)
print("Time:", end - start)