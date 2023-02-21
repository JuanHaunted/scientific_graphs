import numpy as np

def read_two_column_file(file_name):
    with open(file_name, 'r') as data:
        x = []
        y = []
        for line in data:
            p = line.split()
            x.append(p[0])
            y.append(p[1])

    return x, y

def replace_str_list(lst, to_be_replaced, replacement):
    modiefied_lst = []
    for element in lst:
        modiefied_lst.append(element.replace(to_be_replaced, replacement))

    return modiefied_lst

def process_data(file_name):
    x, y = read_two_column_file(f'data/{file_name}')
    mod_x = replace_str_list(x, ",", ".")
    mod_y= replace_str_list(y, ",", ".")
    float_x = [float(i) for i in mod_x]
    float_y = [float(i) for i in mod_y]

    return float_x, float_y

#

def get_cauchy_aprox(l1, l2, l3, n_array=[1, 1, 1]):
    A = np.array(([1, 1/(l1**2), 1/(l1**4)], [1, 1/(l2**2), 1/(l2**4)], [1, 1/(l3**2), 1/(l3**4)]))
    b = np.array((n_array)).reshape(3, 1)
    x = np.linalg.inv(A) @ b 

    return lambda lamb: x[0] + (x[1]/(lamb**2)) + (x[2]/(lamb**4))  


def get_cauchy_constants(l1, l2, l3, n_array=[1, 1, 1]):
    A = np.array(([1, 1/(l1**2), 1/(l1**4)], [1, 1/(l2**2), 1/(l2**4)], [1, 1/(l3**2), 1/(l3**4)]))
    b = np.array((n_array)).reshape(3, 1)
    x = np.linalg.inv(A) @ b 
    #lambda lamb: x[0] + (x[1]/(lamb**2)) + (x[2]/(lamb**4))  
    return x


def get_refraction_angle(min_deviation):
    alpha = np.deg2rad(60)
    min_deviation = np.deg2rad(min_deviation)
    return np.sin((min_deviation+alpha)/2)/np.sin(alpha/2)

def calc_abbe_number(n_d, n_F, n_C):
    return (n_d - 1) / (n_F - n_C)

