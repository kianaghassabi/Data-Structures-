# Hosein Kangavar Nazari - IASBS 30 October 2018
# Closest pair problem in 3D - Brute force method
# Compelexity O(n^2)

# CPtool: i put some common functions and classes which used in 3D Methods
from CPtool3D import _distance ,minimum

from math import floor
import time


# reading file
points = []
file_open = open("./Data/3D/dataGenerator3d.txt", "r")
# file_open = open("./Data/3D/iasbs12_3d.txt", "r")
#file_open = open("./Data/3D/input9.txt", "r")
data = file_open.read()

points = data.split("\n")
DS_standard = []

for i in range(1, len(points)):
    temp = points[i].split(" ")
    DS_standard.append([float(temp[0]), float(temp[1]), float(temp[2])])


def dccp_3d_one(sortedX, start, end):
    # assign positive infinity to minG
    minG = minimum(0, 0, 0, 0, 0, 0, 100000)


    for i in range(start, end):
        for j in range(i+1, end):
            #comparing distance for each pair of nodes
            minTemp = _distance(sortedX[i], sortedX[j])
            # we can use just <= insted of < here 
            if (minTemp < minG.min_value):
                minG.x1 = sortedX[i][0]
                minG.y1 = sortedX[i][1]
                minG.z1 = sortedX[i][2]
                minG.x2 = sortedX[j][0]
                minG.y2 = sortedX[j][1]
                minG.z2 = sortedX[j][2]
                minG.min_value = minTemp
    return minG

start = time.time()
Answer = dccp_3d_one(DS_standard, 0, len(DS_standard))
end = time.time()

print("The answer is :", Answer.min_value)
print( "Time:", end - start)