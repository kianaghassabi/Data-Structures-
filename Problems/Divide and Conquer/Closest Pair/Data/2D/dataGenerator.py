import random
from random import seed

seed(1)
f = open("dataGenerator.txt","w+")
f.write("%d\n" %(1000))
for i in range(1000):
    x1 = random.randint(-1000,1000)
    x2 = random.randint(-1000,1000)
    f.write("%d %d\n" %(x1,x2))