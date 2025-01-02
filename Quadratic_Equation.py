import math

"""
Quadratic Equation

Definition -  A quadratic equation is an equation of the general form ax2 + bx + c = 0, 
              where a≠0 a ≠ 0 where x is a variable and a,b and c are constants.

Equation - x = (-b ± √(b^2 - 4ac)) / 2a

input -> Polynomial x^2 + x - 6 = 0
output -> Roots x = 2, x = -3

///////////////////////////////////////////////////
Plan

- define variables a, b, c
- calculate the discriminant
- examine if roots are real or complex 
- calculate the roots using the quadratic equation 


"""

def quadratic_equation(polynomial):

    print(polynomial)
    polynomial = polynomial.split()
    
    
    # general form ax^2 + bx + c = 0 
    a, b, c =  polynomial[0][0], polynomial[2], polynomial[3] + polynomial[4]

    format_array = [a, b, c]

    determinant_array = []

    for i in format_array:
        if i == 'x':
            determinant_array.append(1)
        else:
            determinant_array.append(int(i))

    #print('determinant_array', determinant_array)

    determinant = (determinant_array[1]**2) - 4 * (determinant_array[0]) * (determinant_array[2])
    print(determinant)

    if determinant < 0 :
        print(f'Determinant {determinant} < 0 therefore roots are complex')
    else:
        print(f'Determinant {determinant} > 0 therefore has real roots')

    # Equation - x = (-b ± √(b^2 - 4ac)) / 2a

    b = -determinant_array[1]
    
    two_a = 2 * determinant_array[0]

    roots = []

    root_1 = (b + math.sqrt(determinant)) / two_a
    root_2 = (b - math.sqrt(determinant)) / two_a

    roots.append(root_1)
    roots.append(root_2)
    print('roots', roots)

polynomial = "x^2 + x - 6 = 0" #poly_gen

quadratic_equation(polynomial)