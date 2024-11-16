from sympy import sympify, lambdify, Symbol, diff
import time

def is_valid_func(input):
    #Checks if the users input function is a valid math function
    try:
        #uses 'eval' so its unsafe but it doesn't matter here.
        sympify(input)
    except Exception as e:
        return False

def help_menu():
    print("---------")
    print("HELP MENU.")
    print("input syntax and important tips :)")
    print("---------")
    print("Function variable must be 'x'")
    print("---------")
    print("2x -> 2*x")
    print("x^5 -> x**5")
    print("e -> E")
    print("---------")
    time.sleep(3)
    return

def newton(input_function, initial_x, iterations):
    #Test to see if function is valid
    test_valid = is_valid_func(input_function)
    if test_valid is False:
        print("Function is INVALID, please check your input.")
        return
    #Perform function parsing and take the derivative
    x = Symbol('x')
    derivative = diff(input_function, x)
    func = lambdify(x, input_function)
    deriv_f = lambdify(x, derivative)
    value = initial_x
    print("x0 =", value)

    for i in range(iterations):
        result_y = func(value)
        result_dy = deriv_f(value)
        if result_dy == 0:
            print("Cannot divide by 0, sorry.")
            break
        value = value - (result_y / result_dy)
        index = i+1
        print(f"x{index} = {value:.5f}", )

def launch_newton():
    #Newton active while loop for accepting repetitive inputs
    print("Please input the function.")
    the_function = input()
    if the_function.lower() == 'help':
        help_menu()
        return
    print("Please input the initial x value.")
    try:
        initial_x = float(input())
    except Exception as e:
        print("Please make initial x value an integer or decimal.")
        time.sleep(1)
        return
    
    print("Please input the number of newton iterations.")
    try:
        iterations = int(input())
    except Exception as e:
        print("Please input number of iterations as positive integer.")
        time.sleep(1)
        return
    
    print("Performing calculation")
    time.sleep(1)
    newton(the_function, initial_x, iterations)
    time.sleep(2)

#leave while loop, checks user input if they want to do more functions.
#leave = true means user wants to stop
def run_program():
    print("type 'help' for input info")
    leave = False
    while leave is False:
        leave = False
        ask_again = True
        launch_newton()
        while ask_again:
            print("Would you like to do another? (Y/N)")
            response = input()
            if response.lower() == 'n':
                ask_again = False
                leave = True
                print("See you later.")              

            elif response.lower() == 'help':
                help_menu()
            
            elif response.lower() != 'y':
                print("I am lazy I only accept Y or N.")
                time.sleep(1)
            
            else:
                ask_again = False

run_program()
   
            