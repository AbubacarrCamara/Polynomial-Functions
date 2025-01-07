"""
This is a function designed to graph the polynomials genereated by poly_gen
////////////////////////////////////////////////////////////////////////////////////

Feature 

Graphical display of generated polynomial 

plan
- New function that takes the output of polygen as its argument eg input -> x^4 + 3x^3 + 2x^2 + x + 1 = 0 outputs -> graph of polynomial

- The coeffiects and operation signs will be stored in there own respective arrays 

- An x - axis array ranging from (-10, 10) will be initalised 

- The values for x will be substituded into the x variable eg (-10)^4 + 3(-10)^3 + 2(-10)^2 + (-10) + 1 = 0

- A tuple containing the coefficent, the substituted x variable and the power eg  3(-10)^3 -> (3, -10, 3)

- These tuple values will be used to calculate the product of each substituded variable and stored in a new array eg (3, -10, 3) -> 3 * (-10)^^3 

- [(1, 0, 4), (3, 0, 3), (2, 0, 2), (1, 0, 1)] -> [10000, -3000, 200, -10]

- This new array containing the product of the subed variables is then summed based on the signs contained in the signs array to return the coresseponding y value for that x coordinate

- signs = [+, +, +, +]

- y_value = 10000 + (-3000) + 200 + (-10)

- The y values are then stored in a y_axis array

- The x and y axis arrays are then used to plot the polynomial through seaborn and matplotlib

"""
from Poly_Gen import poly_gen
import seaborn as sns
import matplotlib.pyplot as plt

def poly_plot(polynomial):
    
    print('polynomial', polynomial)

    # Extacts the signs from the polynomial
    signs = [x for x in polynomial.split() if x == '+' or x == '-']
    print('signs', signs)

    # Initialises the x_axis 
    x_axis = list(range(-5, 6))
    #print('x_axis', x_axis)

    # Initialises the array that will store the new polynomial with an x value substituted in 
    sub_structure = [polynomial.replace("x", f"({x_axis[0]})")]
    print('sub_structure', sub_structure)

    # Selects all values in the polynomial that are not constants 
    coefficients_structure = [x for x in sub_structure[0].split() if len(x) > 1]
    print('coefficients_structure', coefficients_structure)

    # Selects the coefficient infront of the x value
    mul = [int(x[0]) if x[0].isnumeric() else 1 for x in coefficients_structure]
    #print('mul', mul)

    # Selects the power behind the x value
    pow = [int(x[-1]) if x[-1].isnumeric() else 1 for x in coefficients_structure]
    #print('pow', pow)

    # Selects the constant within the polynomial 
    cons = [int(x) for x in polynomial.split() if x.isnumeric() and x != '0']
    print('cons', cons)

    # Initalises the array that will hold the tuple containing the general structure of our polynomial
    structure = []

    # Loops the length of coefficients_structure to ensure it creates the right number of tuples
    for i in range(len(coefficients_structure)):
        tup = (mul[i], 0, pow[i])
        structure.append(tup)
    print('structure', structure)

    product_array = []

    # Calculates the product values of our x value subbed monomial 
    for x in x_axis:
        ops = [(t[0], x, t[2]) for t in structure] # Subs a x value into the 2nd index of each tuple
        #print('ops', ops)

        function = [y[0] * (y[1] ** y[2]) for y in ops] # Calculates the product value of each tuple and appends it to the product array
        #print(function)
        product_array.append(function)

    #print('product_array', product_array)

    y_axis = []

    # Calculates y value for each value of x based on the signs in the signs array
    for p in product_array:
        total = p[0]

        for i in range(len(signs) - 1):
            if signs[i] == "+":
                total += p[i + 1]
            else:
                total -= p[i + 1]

        # Operation to include constant in y value
        if signs[-1] == "+":
            total += cons[0]
        else:
            total -= cons[0]

        y_axis.append(total)

    print('y_axis', y_axis)

    # Graphs function using x and y value coordinates 
    sns.set_theme(style='darkgrid')

    sns.lineplot(
        x= x_axis, 
        y= y_axis,
        )
    
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")

    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Horizontal line
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Vertical line

    plt.title(f'Graph of the Polynomial {polynomial}')
    
    plt.show()


polynomial = poly_gen()

poly_plot(polynomial)