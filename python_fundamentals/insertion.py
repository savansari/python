def insertion_sort(x):
    for i in range(1,len(x)):
        key=x[i]
        j=i-1
        while j>-1 and x[j]>key:
            x[j],x[j+1]=x[j+1],x[j]
            j-=1
        
        x[j+1]=key
    return x
print (insertion_sort([]))
print(insertion_sort([]))
print(insertion_sort([1,2,3,4]))
print(insertion_sort([4,3,2,1]))
print(insertion_sort([1,8,3,9,3,0,4,8]))
print(insertion_sort([1,1,1,1,1,1]))