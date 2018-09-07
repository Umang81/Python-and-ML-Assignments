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
    data = np.genfromtxt(path, dtype = "|S100", skip_header=1, delimiter = ",", usecols = np.arange(0,23))
    return data

data = read_csv_data_to_ndarray('./ipl_matches_small.csv')
print (data)

#exercise 5
def get_unique_matches_count(data):
    match_code = data[:,0]
    print (match_code)
    unique_matches = set(match_code)
    count_unique_matches = len(unique_matches)
    return count_unique_matches

unique_match_count = get_unique_matches_count(data)
print (unique_match_count)

#exercise 6
def get_unique_teams_set(data):
    team1_list = list(set(data[:,3]))
    team2_list = list(set(data[:,4]))
    team_list = list(set(team1_list + team2_list))
    print (team1_list)
    print (team2_list)
    return team_list

unique_teams = get_unique_teams_set(data)
print (unique_teams)

#exercise 7
def get_total_extras(data):
    extras = list((data[:,17]))
    print (extras)
    total_extras = 0
    for i in range(0,len(extras)):
        total_extras += int(extras[i])
    return (total_extras)


total_extras = get_total_extras(data)
print (total_extras)
