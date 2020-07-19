import numpy

R1 = int(input("Enter the number of rows: "))

C1 = int(input("Enter the number of columns:"))

matrix1 = [] 
print("Enter the entries row wise: ")

for i in range(R1):          # A for loop for row entries 
    a =[] 
    for j in range(C1):      # A for loop for column entries 
         a.append(int(input())) 
    matrix1.append(a)

for i in range(R1): 
    for j in range(C1): 
        print(matrix1[i][j], end = " ") 
    print()

R2 = int(input("Enter the number of rows: "))

C2 = int(input("Enter the number of columns:"))

matrix2 = [] 
print("Enter the entries row wise: ")

for i in range(R2):          # A for loop for row entries 
    b =[] 
    for j in range(C2):      # A for loop for column entries 
         b.append(int(input())) 
    matrix2.append(b)

for i in range(R2): 
    for j in range(C2): 
        print(matrix2[i][j], end = " ") 
    print()

# Addition

sum=numpy.add(matrix1,matrix2)

print(sum)


# Multiplication

mul=numpy.multiply(matrix1,matrix2)

print(mul)


# Subtraction

dif=numpy.subtract(matrix1,matrix2)

print(dif)

# Division

div=numpy.divide(matrix1,matrix2)

print(div)

