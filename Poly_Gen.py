import math
import random

""""
Number Generation

The numbers in front of x will range from (1 - 9) 
The powers will range from (2-4) as >= 5 degree polynomials have no solution

////////////////////////////////////////////////////////////////////////////////////

Formatting

output -> x^4 + 3x^3 + 2x^2 + x + 1 = 0

Random allocation of array size ranging from (3 - 5) exluding symbols 

Example - [0,0,0]

The x components will then be created and will populate the spaces in the array

Example - [x^4, 2x^2, 1]

Array containing ['+', '-']

Final output - return f" {a1} + {random sign},,, {an} = 0"

"""

def poly_gen():

    # Set inital size of array
    array_size = random.randrange(2, 5)
    #print('array_size', array_size)

    constant = str(random.randrange(1, 26))

    # Initalise where coefficients will be stored
    coefficient_array = []

    # List of powers that can be used for each x
    power_array = list(range(1, 5))
    #print('power_array', power_array)

    # Operation symbols generated as required for the equation 
    signs = ["+", "-"]
    signs_array = [random.choice(signs) for i in range(array_size-1)]

    # Selects a random power in power_array, assigns it to the x component and removes it from the list
    for i in range(array_size ):
        power = random.choice(power_array)
        power_array.remove(power)
        #print('power_array', power_array)

        x_coefficient = f"{random.randrange(1,10)}x^{power}"
        coefficient_array.append(x_coefficient)
        #print('x_coefficient', x_coefficient)

    #print('coefficient_array', coefficient_array)

    # Arranges coefficients array based on the power of x 
    coefficient_array.sort(reverse=True, key=lambda x: x[3])

    equals = "= 0"
    polynomial = ''

    # Dynamically builds the polynomial equation randomly selecting a sign from the signs array
    for j in coefficient_array:
        construct = ' ' + j + " " + f"{random.choice(signs_array)}"
        #print('construct', construct)
        polynomial += construct

    #polynomial = polynomial[:-1]
    polynomial += " " + constant + " " + equals
    
    print('polynomial', polynomial)

    return polynomial

poly_gen() 


