# Arrays are represented using Lists. Being dynamic.

# Some operations using it

#Example

arr = [1, 23, 13, 46, 5]

#print(arr[0]) #output: 1

#modify elements
arr[2] = 10 
#print(arr) #output: 1, 2, 10, 4, 5

for num in arr: 
    print(arr, end=" ")
    
#get lenght of an array
x = len(arr)
print(x)

#get number of specific element
y = arr.count(2)
print(y)

#arrange the array
arr.sort()
print(arr)
