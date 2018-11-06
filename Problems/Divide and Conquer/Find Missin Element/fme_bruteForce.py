#Hosein kangavar nazari 
# finding missing element - Brute force method 
# O(n)

import time
array = []
# reading from file
file_open = open("array.txt", "r")
data = file_open.read()
points = data.split(" ")
flag = 0 

startTime = time.time()

for i in range(1, len(points)):
    if(i != int(points[i])):
        flag = 1
        print ("The answer is : ",i)
        break

#  in case we didn't find any missing element in array
if (flag == 0):
    print ("All element were there!")
endTime = time.time()
print("Time: " , endTime - startTime)