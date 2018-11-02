# Hosein Kangavar Nazari - IASBS 30 October 2018
# Closest pair problem in 2D - Brute force method
# Compelexity O(n^2)

from math import floor
import time
# CPtool: i put some common functions and classes which used in 2D Methods
from CPtool import _distance , minimum



# reading from file
points = []
file_open = open("./Data/2D/dataGenerator.txt", "r")
data = file_open.read()
points = data.split("\n")

DS_standard = []
for i in range(1, len(points)):
    temp = points[i].split(" ")
    DS_standard.append([float(temp[0]), float(temp[1])])



def dccp_2d_one(sortedX, start, end):
    #assign positive infinity to minG
    minG = minimum(0,0,0,0,1000) 
    #brute force method for each point
    for i in range (start,end):
        for j in range (i+1,end):
            #comparing distance for each pair of nodes
            minTemp = _distance(sortedX[i],sortedX[j])
            # we can use just < insted of <= here 
            if (minTemp <= minG.min_value):
                minG.x1 = sortedX[i][0]
                minG.y1 = sortedX[i][1]
                minG.x2 = sortedX[j][0]
                minG.y2 = sortedX[j][1]
                minG.min_value = minTemp
    return minG

start = time.time()
Answer = dccp_2d_one(DS_standard,0,len(DS_standard))
end = time.time()
print("The answer is :", Answer.min_value)


print( "Time:", end - start)