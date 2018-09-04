import numpy as np

def array_zeros(number_of_zeros, dim1, dim2, dim3):
    mylist = [0]*24
    print (mylist)
    zeros_array = np.array(mylist).reshape(dim1,dim2,dim3)
    print (zeros_array)

array_zeros(24, 3, 4, 2)
