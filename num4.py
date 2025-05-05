import numpy as np


### Numpy array OPERATIONS

# arr= np.arange(11)
# print(arr)

# print(arr[2:7])
# print(arr[2:11:2])
# print(arr[-1])

arr_2d=np.array([[7,2,3],
                 [6,5,4],
                 [8,6,4]])
    
# print(arr_2d[2,2])

# print(arr_2d[:,2])  #column target




########################################
#  SORTING


# unsorted=np.array([4,5,6,8,2,9,3,5,1])

# print(np.sort(unsorted))
# print(np.sort(arr_2d,axis=0) ) #column sort
# print(np.sort(arr_2d,axis=1) ) #row sort



### FILTER
# print(unsorted[unsorted%2==0]) #conditiona

# mask= unsorted>5
# print(mask)

# indx=np.where(unsorted>5)
# print(indx)
# print(unsorted[indx])


arr=np.array([4,5,6,8,2])
arr2=np.array([2,9,3,5,1])

arr3=np.concatenate((arr,arr2))

print(arr3)


#compatibility
print(arr.shape==arr2.shape)

print(np.delete(arr3,2))












