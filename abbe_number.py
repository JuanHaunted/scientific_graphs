#Calculamos refraction index
from functions import *

n_violet = get_refraction_angle(48.53)
n_green = get_refraction_angle(47.55)
n_yellow = get_refraction_angle(46.68)
n_red = get_refraction_angle(46.13)

print(n_violet, n_green, n_yellow, n_red)

n_arr = [n_green, n_yellow, n_red]

cauchy_aproximation = get_cauchy_aprox(501.567, 587.562, 667.815, n_arr)

n_d = cauchy_aproximation(466.814)
n_F = cauchy_aproximation(486.134)
n_C = cauchy_aproximation(656.281)

abbe_number = calc_abbe_number(n_d, n_F, n_C)
print(abbe_number)