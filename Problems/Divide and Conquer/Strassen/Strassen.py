#Hosein Kangavar Nazari
#Strassen Algorithm O(n^2.81)

from matrix import matrix
import time

def strassen(MA, MB):
    if(MA.size == MB.size and MB.size > 2):
        a00, a01, a10, a11 = MA.split()
        b00, b01, b10, b11 = MB.split()
        if(MA.size >= 512):
            m1 = strassen((a00+a11), (b00+b11))
            m2 = strassen((a10+a11), b00)
            m3 = strassen(a00, (b01-b11))
            m4 = strassen(a11, (b10-b00))
            m5 = strassen((a00+a01), b11)
            m6 = strassen((a10-a00), (b00+b01))
            m7 = strassen((a01-a11), (b10+b11))
            topLeft = m1+m4-m5+m7
            topRight = m3+m5
            downLeft = m2+m4
            downRight = m1+m3-m2+m6
            Answer = matrix(MA.size)
            Answer.combine(topLeft,topRight,downLeft,downRight)
            return Answer
        else:
            return MA*MB
    else:
        print("can't multiply this and that")


# b = matrix(8)
# b.set_matrix([[1, 1, 1, 1, 2, 2, 2, 2],
#               [1, 1, 1, 1, 2, 2, 2, 2],
#               [1, 1, 1, 1, 2, 2, 2, 2],
#               [1, 1, 1, 1, 2, 2, 2, 2],
#               [3, 3, 3, 3, 4, 4, 4, 4],
#               [3, 3, 3, 3, 4, 4, 4, 4],
#               [3, 3, 3, 3, 4, 4, 4, 4],
#               [3, 3, 3, 3, 4, 4, 4, 4]])

# a = matrix(8)
# a.set_matrix([[1, 1, 1, 1, 1, 1, 1, 1],
#               [2, 2, 2, 2, 2, 2, 2, 2],
#               [3, 3, 3, 3, 3, 3, 3, 3],
#               [4, 4, 4, 4, 4, 4, 4, 4],
#               [5, 5, 5, 5, 5, 5, 5, 5],

#               [6, 6, 6, 6, 6, 6, 6, 6],
#               [7, 7, 7, 7, 7, 7, 7, 7],
#               [8, 8, 8, 8, 8, 8, 8, 8]])

# c = strassen(a, b)
# d =  a * b

a = matrix(2**9)
a.random_variable() 
b = matrix(2**9)
b.random_variable()
start = time.time()
c = strassen(a, b)
end = time.time() 
print( "Time:", end - start)

# d =  a * b
