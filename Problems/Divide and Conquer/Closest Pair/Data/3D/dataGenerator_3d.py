import random
from random import seed

seed(1)
f = open("dataGenerator3D.txt","w+")
f.write("%d" %(100000))
for i in range(100000):
    x1 = random.randint(-600,100000)
    x2 = random.randint(-600,100000)
    x3 = random.randint(-600,100000)
    f.write("\n%d %d %d" %(x1,x2,x3))