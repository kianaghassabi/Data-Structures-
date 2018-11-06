#Hosein kangavar nazari 
# finding missing element - Binary searchMethod 
# O(logn)

from math import ceil,floor
import time 
array = []
# reading from file
file_open = open("array.txt", "r")
data = file_open.read()
points = data.split(" ")
flag = 0 

start = 1 
end = len(points)

startTime = time.time()

while True:
    if(start==end):
        break

    elif (end-start == 1):
        if (int(points[end])!=end):
            mid = end 
            break
        else:
            mid = start 
            break

    mid = floor((start+end)/2)
    if (int(points[mid])==mid):
        start = mid
    else:
        end=mid

print ("The answer is : ",mid)

endTime = time.time()

print("Time: " , endTime - startTime)