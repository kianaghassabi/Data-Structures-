# Hosein Kangavar Nazari - IASBS 30 October 2018
# Closest pair problem in 2D -  [ x sorted ]
# Time Compelexity:  O(nlog^2(n))


# CPtool: i put some common functions and classes which used in 2D Methods
from CPtool import _distance , minimum , min_of_minimums , binary_search , subset_by_range

from operator import itemgetter
from math import floor
import time


# reading from file
points = []
# file_open = open("./Data/2D/data.txt", "r")
file_open = open("./Data/2D/dataGenerator.txt", "r")
data = file_open.read()
points = data.split("\n")

DS_standard = []
for i in range(1, len(points)):
    temp = points[i].split(" ")
    DS_standard.append([float(temp[0]), float(temp[1])])


## sorting data
sortedByX=[]
sortedByX = sorted(DS_standard, key=itemgetter(0))
#assigning a null value as first member of list 
# [used for simpilisity in  indexing problems]
sortedByX.insert(0,[-10000,-10000])



def dccp_two(sortedX, start, end):
    #assign positive infinity to minG
    minG = minimum(0,0,0,0,1000.0)
    #if there is less than 4 point use brute force 
    if(end - start <= 2):
        for i in range (start,end):
            for j in range (i+1,end+1):
                minTemp = _distance(sortedX[i],sortedX[j])
                if (minTemp <= minG.min_value):
                    minG.x1 = sortedX[i][0]
                    minG.y1 = sortedX[i][1]
                    minG.x2 = sortedX[j][0]
                    minG.y2 = sortedX[j][1]
                    minG.min_value = minTemp
        return minG

    else:
        minL = dccp_two(sortedX, start, floor((end+start-1)/2))
        minR = dccp_two(sortedX, floor((end+start-1)/2)+1, end)
        minG = min_of_minimums(minL, minR)

        #rightest member of left , leftest member of right
        middle = (sortedX[floor((end+start-1)/2)][0] + sortedX[floor((end+start-1)/2)+1][0])/2
        lowerBoundX = middle - minG.min_value
        upperBoundX = middle + minG.min_value
        # floor or ceil for halfsorted, that the question
        strip = subset_by_range(sortedX,lowerBoundX,upperBoundX,0)
        strip = sorted(strip, key=itemgetter(1))
        for i in range(0,len(strip)):
            for j in range(i+1,len(strip)):
                if(abs(strip[i][1]-strip[j][1]) > minG.min_value):
                    break
                minTemp = _distance(strip[i],strip[j])
                if (minTemp < minG.min_value):
                    minG.x1 = strip[i][0]
                    minG.y1 = strip[i][1]
                    minG.x2 = strip[j][0]
                    minG.y2 = strip[j][1]
                    minG.min_value = minTemp
        # if the result is zero its because  we putted a point in two side or two point in data set are the same
        return minG
 

start = time.time()
Answer = dccp_two(sortedByX,1,len(sortedByX)-1)
end = time.time()

print("The answer is :", Answer.min_value)


print( "Time:", end - start)