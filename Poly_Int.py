import math
from Poly_Gen import poly_gen

"""
Integration 

Definition -  A method of adding or summing up the parts to find the whole. 
              It is a reverse process of differentiation, where we reduce the functions into parts.

Equation - ∫x^n dx = (x^n+1) / (n + 1)

This function will integrate polynomials generated by the poly_gen function

input -> Polynomial 1x^4 + 3x^3 + 2x^2 + x + 1 = 0

output -> 1/5x^5 + 3/4x^4 + 2/3x^3 + 1/2x^2 + x + c = 0


//////////////////////////////////////////////////////////////////
Plan

- Collect all coefficients, powers and signs into an array
- The new coefficients will be calculated by multiplying the powers with thier respective coefficients
- The new powers will be calculated by subtracting 1 from the current power
- The integrated polynomial will then constructed from the new powers and coefficients 
- Constant terms will go to x 
- Plus c will be added to the end of the integral
"""

def poly_int(polynomial):
    print('polynomial', polynomial)

    # Splits the inital polynomial string into seperate strings
    polynomial = polynomial.split()
    #print('polynomial', polynomial)

    # Collects all the coefficients into an array
    coefficients = [x[0] for x in polynomial if len(x) == 4]
    #print('coefficients', coefficients)

    # Collects all powers into an array
    powers = [x[3] for x in polynomial if len(x) == 4]
    #print('powers', powers)

    # Collects all signs in equation
    signs = [x for x in polynomial if x == '+' or x == '-']
    #print('signs', signs)

    new_powers = [str(int(x) + 1) for x in powers]
    #print('new_powers', new_powers)

    new_coefficients = []

    # Creates and store the new coefficient values 
    for i in range(len(coefficients)):
        new_co = coefficients[i] + "/" + new_powers[i]
        new_coefficients.append(new_co)

    # Handles edge cases such as single x terms 
    for i in polynomial:
        if i == 'x':
            new_coefficients.append("1/2")
            new_powers.append('2')
        elif i.isnumeric() and i != '0':
            new_coefficients.append('x')

    #print('new_coefficients', new_coefficients)

    inter = ''

    # Generates the x terms of the intergral 
    for i in range(len(new_coefficients) - 1):
        
        co_add = f"{str(new_coefficients[i])}" + 'x'
        #print('co_add', co_add)

        # Removes first two elements if they are the same eg 2/2x^2 -> x^2
        if co_add[0] == co_add[2]:
            co_add = co_add[3:]

        power_add = f"{str(new_powers[i])}"
        #print('power_add', power_add)

        inter += ' ' + co_add + "^" + power_add

    # Adds a x term to the constant term
    for i in polynomial:
        if i.isnumeric() and i != '0':
            inter += ' ' + ' ' + f'{i}x' + ' ' + '+' + ' ' + 'c'

    inter = inter.split()

    #print('inter', inter)

    intergrand = ''

    # Constructs the integral of the polynomial
    for i in range(len(inter)):
        try:
            term = inter[i] + " " + signs[i]
            intergrand +=  " " + term
        except(IndexError):
             intergrand +=  " " + inter[i]


    intergrand += " = 0"

    print('intergrand', intergrand)


polynomial = poly_gen()
poly_int(polynomial)