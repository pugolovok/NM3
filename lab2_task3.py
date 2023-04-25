import numpy as np
import sympy as smp
import math

x = smp.symbols('x')
f = smp.exp(x**3)
x1 = -0.5
f_ = f
sum = 0.0

for i in range(60):
    f_0 = f_.subs(x,0)
    x1_pow_i = x1**i
    i_fact = math.factorial(i)
    if f_0 != 0:
        ai = f_0 * x1_pow_i / i_fact
        sum += ai 
        print('i =', i, '    x_pow_i =', x1_pow_i, ',    f_0 =', f_0, ',   ai = ', ai, ',    sum = ', sum, ',   i! =', i_fact) 
    f_ = smp.diff(f_, x)
    
print('x = 0.2')
res_02_32bit = np.float32(0.0)
res_02_32bit = np.float32(1.0) + \
               np.float32(6.0) * np.float32(0.008000000000000002) / np.float32(6.0) + \
               np.float32(360.0) * np.float32(6.400000000000002e-05) / np.float32(720.0) + \
               np.float32(60480.0) * np.float32(5.120000000000002e-07) / np.float32(362880.0) + \
               np.float32(19958400.0) * np.float32(4.096000000000002e-09) / np.float32(479001600.0)
print('32bit: ', res_02_32bit)
res_02_64bit = np.float32(0.0)
res_02_64bit = np.float64(1.0) + \
               np.float64(6.0) * np.float64(0.008000000000000002) / np.float64(6.0) + \
               np.float64(360.0) * np.float64(6.400000000000002e-05) / np.float64(720.0) + \
               np.float64(60480.0) * np.float64(5.120000000000002e-07) / np.float64(362880.0) + \
               np.float64(19958400.0) * np.float64(4.096000000000002e-09) / np.float64(479001600.0)
print('64bit: ', res_02_64bit)
print('Точно: ', math.e**(0.2**3))


print('x = -0.2')
res_02minus_32bit = np.float32(0.0)
res_02minus_32bit = np.float32(1.0) + \
               np.float32(6.0) * np.float32(-0.008000000000000002) / np.float32(6.0) + \
               np.float32(360.0) * np.float32(6.400000000000002e-05) / np.float32(720.0) + \
               np.float32(60480.0) * np.float32(-5.120000000000002e-07) / np.float32(362880.0) + \
               np.float32(19958400.0) * np.float32(4.096000000000002e-09) / np.float32(479001600.0)
print('32bit: ', res_02minus_32bit)
res_02minus_64bit = np.float32(0.0)
res_02minus_64bit = np.float64(1.0) + \
               np.float64(6.0) * np.float64(-0.008000000000000002) / np.float64(6.0) + \
               np.float64(360.0) * np.float64(6.400000000000002e-05) / np.float64(720.0) + \
               np.float64(60480.0) * np.float64(-5.120000000000002e-07) / np.float64(362880.0) + \
               np.float64(19958400.0) * np.float64(4.096000000000002e-09) / np.float64(479001600.0)
print('64bit: ', res_02minus_64bit)
print('Точно: ', math.e**(-0.2**3))


print('x = 0.5')
res_05_32bit = np.float32(0.0)
res_05_32bit = np.float32(1.0) + \
               np.float32(6.0) * np.float32(0.125) / np.float32(6.0) + \
               np.float32(360.0) * np.float32(0.015625) / np.float32(720.0) + \
               np.float32(60480.0) * np.float32(0.001953125) / np.float32(362880.0) + \
               np.float32(19958400.0) * np.float32(0.000244140625) / np.float32(479001600.0)
print('32bit: ', res_05_32bit)
res_05_64bit = np.float32(0.0)
res_05_64bit = np.float64(1.0) + \
               np.float64(6.0) * np.float64(0.125) / np.float64(6.0) + \
               np.float64(360.0) * np.float64(0.015625) / np.float64(720.0) + \
               np.float64(60480.0) * np.float64(0.001953125) / np.float64(362880.0) + \
               np.float64(19958400.0) * np.float64(0.000244140625) / np.float64(479001600.0)
print('64bit: ', res_05_64bit)
print('Точно: ', math.e**(0.5**3))


print('x = -0.5')
res_05minus_32bit = np.float32(0.0)
res_05minus_32bit = np.float32(1.0) + \
               np.float32(6.0) * np.float32(-0.125) / np.float32(6.0) + \
               np.float32(360.0) * np.float32(0.015625) / np.float32(720.0) + \
               np.float32(60480.0) * np.float32(-0.001953125) / np.float32(362880.0) + \
               np.float32(19958400.0) * np.float32(0.000244140625) / np.float32(479001600.0)
print('32bit: ', res_05minus_32bit)
res_05minus_64bit = np.float32(0.0)
res_05minus_64bit = np.float64(1.0) + \
               np.float64(6.0) * np.float64(-0.125) / np.float64(6.0) + \
               np.float64(360.0) * np.float64(0.015625) / np.float64(720.0) + \
               np.float64(60480.0) * np.float64(-0.001953125) / np.float64(362880.0) + \
               np.float64(19958400.0) * np.float64(0.000244140625) / np.float64(479001600.0)
print('64bit: ', res_05minus_64bit)
print('Точно: ', math.e**(-0.5**3))
