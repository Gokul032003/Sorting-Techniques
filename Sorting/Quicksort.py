#Quick sort

def quicksort(A,left,right):
    if left>=right:
        return
    p=A[left]
    i=left+1
    j=right
    
    while i<=j:
        while i<=j and A[i]<p:
            i=i+1
        while i<=j and A[j]>p:
            j=j-1
    
        if i<j:
            A[i],A[j]=A[j],A[i]
        else:
            break
    A[left],A[j]=A[j],A[left]
    quicksort(A,left,j-1)
    quicksort(A,j+1,right)


num=[10,25,7,45,31,26,3,5,15,8,99]
print("Before sorting =",num)
quicksort(num,0,len(num)-1)
print("After sorting =",num)
        
    
