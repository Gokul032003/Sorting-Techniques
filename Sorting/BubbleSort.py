#Bubble Sort

def bubbleSort(A):
    n=len(A)
    for i in range(0,n):
        for j in range(n-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]


num=[10,25,7,45,31,26,3,5,15,8,99]
print("Before sorting =",num)
bubbleSort(num)
print("After sorting =",num)
