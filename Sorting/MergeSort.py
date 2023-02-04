#MergeSort

def merge(A,B,C):
    len1=len(B)
    len2=len(C)
    i,j,k=0,0,0
    while i<len1 and j<len2:
        if B[i]<C[j]:
            A[k]=B[i]
            i+=1
        else:
            A[k]=C[j]
            j+=1
        k+=1
    while i<len1:
        A[k]=B[i]
        i+=1
        k+=1
    while j<len2:
        A[k]=C[j]
        j+=1
        k+=1

def mergesort(A):
    n=len(A)
    if n<2:
        return
    mid=n//2
    B=A[0:mid]
    C=A[mid:n]
    mergesort(B)
    mergesort(C)
    merge(A,B,C)



num=[10,25,7,45,31,26,3,5,15,8,99]
print("Before sorting =",num)
mergesort(num)
print("After sorting =",num)







    
        
