#binary search
def BS(a,k): #define function with array & key
    l,r=0,len(a)-1 #assign left as first index & right as last index
    while(l<=r): #while fn use till left is less or is to right 
        m=(l+r)//2 #mid is define with avg. of l&R
        if a[m]==k: #if array[index of mid] is to is to key
            return m #return mid value
        elif a[m]<k: #OrElse arr[mid index] is less than key value
            l=m+1 #reassign left to mid add 1
        else: #else means arr[mid index] is greater than key
            r=m-1 #reassign right to mid sub 1
    else: #else of while means left is greater than right 
        return -1 #return -1 means key not found to array
a=[2,4,6,8,12] # assign array
k=int(input("enter key value upto 20: "))#assign key can change value as ur want
print(BS(a,k))#print binary search index value
ans=BS(a,k)#assign binary search answer as ans 
if ans==-1:#if ans is to -1 then not found
    print(f"we not found key at array so it's {ans}")
else:#if ans is not -1 then found
    print(f"we found key at {ans} index array ")
#this is my knowledge about binary search
