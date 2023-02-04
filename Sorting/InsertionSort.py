#Insertion Sort

def insertionSort(A):
    n=len(A)
    for i in range(1,n):
        pos=A[i]
        for j in range(i,-1,-1):
            if pos<A[j-1]:
                A[j]=A[j-1]
            else:
                break
        A[j]=pos




num=[10,25,7,45,31,26,3,5,15,8,99]
print("Before sorting =",num)
insertionSort(num)
print("After sorting =",num)       
