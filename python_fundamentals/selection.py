
def selection_sort(x):
    
    for i in range(len(x)):
        key=x[i]
        for j in range(i+1,len(x)):
            if x[j]<key :
                x[j],key = key,x[j]               
        x[i]=key
    return x

print(selection_sort([]))
print(selection_sort([1,2,3,4]))
print(selection_sort([4,3,2,1]))
print(selection_sort([1,8,3,9,3,0,4,8]))
print(selection_sort([1,1,1,1,1,1]))