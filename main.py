from matplotlib import pyplot as plt

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

def plot_beautiful_results(x, y, name_x, name_y, title):
    pass


x, y = read_two_column_file('data/nofilter.txt')

mod_x = replace_str_list(x, ",", ".")
float_x = [float(i) for i in mod_x]

mod_y= replace_str_list(y, ",", ".")
float_y = [float(i) for i in mod_y]


plt.plot(float_x, float_y)
plt.show()


