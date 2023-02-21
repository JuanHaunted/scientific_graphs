#Calculamos refraction index
from functions import *

#n_violet = get_refraction_angle(48.53)
#n_green = get_refraction_angle(47.55)
#n_yellow = get_refraction_angle(46.68)
#n_red = get_refraction_angle(46.13)

n_violet = get_refraction_angle(56.537)
n_green = get_refraction_angle(55.553)
n_yellow = get_refraction_angle(54.687)
n_red = get_refraction_angle(54.137)


print(n_violet, n_green, n_yellow, n_red)

#443,755
n_arr = [n_violet, n_yellow, n_red]

cauchy_aproximation = get_cauchy_aprox(443.755, 587.562, 667.815, n_arr)
cauchy_constants = get_cauchy_constants(443.755, 587.562, 667.815, n_arr)

print(f"Cauchy Constants: {cauchy_constants}")

n_d = cauchy_aproximation(587.6)
n_F = cauchy_aproximation(486.1)
n_C = cauchy_aproximation(656.3)

print(n_d, n_F, n_C)


abbe_number = calc_abbe_number(n_d, n_F, n_C)
print(abbe_number)


