import numpy as np
#exercise 1
def array_zeros(number_of_zeros, dim1, dim2, dim3):
    mylist = [0]* number_of_zeros
    zeros_array = np.array(mylist).reshape(dim1,dim2,dim3)
    return zeros_array

a = array_zeros(24, 3, 4, 2)
print (a)

#exercise 2
def array_reshape(array,dim1,dim2,dim3):
    a = array.reshape(dim1,dim2,dim3)
    return (a)

a = array_reshape(a,2,3,4)
print (a)

#exercise 3
def create_3d_array(dim1, dim2, dim3):
    number_of_elements = dim1 * dim2 * dim3
    ls = list(range(0,number_of_elements))
    a = np.array(ls).reshape(dim1,dim2,dim3)
    return a

a = create_3d_array(3,3,3)
print (a)

#exercise 4
def read_csv_data_to_ndarray(path):
    data = np.genfromtxt(path,dtype = "|S20", skip_header=1, delimiter = "\t", usecols = np.arange(0,13))
    print(data)

read_csv_data_to_ndarray('./ipl_matches_small.txt')
