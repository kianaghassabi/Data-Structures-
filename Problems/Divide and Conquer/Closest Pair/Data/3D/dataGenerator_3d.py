import random
from random import seed

seed(1)
f = open("dataGenerator3D.txt","w+")
f.write("%d" %(300))
for i in range(300):
    x1 = random.randint(-1000,1000)
    x2 = random.randint(-1000,1000)
    x3 = random.randint(-1000,1000)
    f.write("\n%d %d %d" %(x1,x2,x3))