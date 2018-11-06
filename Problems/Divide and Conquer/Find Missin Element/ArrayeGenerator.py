import random
from random import seed
from math import floor

MaxSize = 10000000
# seed(10)
f = open("Array.txt","w+")
f.write("%d" %(MaxSize))

rand_number = floor(random.randint(1,MaxSize))
for i in range(1,MaxSize+1):
    if(i==rand_number):
        continue
    f.write(' '+"%d" %(i))
    