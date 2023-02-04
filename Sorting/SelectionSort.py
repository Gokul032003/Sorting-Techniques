#Selection Sort

def SelectionSort(A):
    n=len(A)
    for i in range(0,n):
        mini=i
        for j in range(i+1,n):
            if A[mini]>A[j]:
                A[mini],A[j]=A[j],A[mini]


num=[10,25,7,45,31,26,3,5,15,8,99]
print("Before sorting =",num)
SelectionSort(num)
print("After sorting =",num)
