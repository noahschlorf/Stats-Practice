from cmath import sqrt
import random
from sympy import symbols, integrate

x, y = symbols('x y')
x_val = None
y_val = None

lowerbound = 0
upperbound = None


if lowerbound is None:
    lowerbound = random.randint(-5, 0)

lowerbound_x = lowerbound
lowerbound_y = lowerbound

if upperbound is None:
    upperbound = random.randint(lowerbound, 5)

upperbound_y = upperbound
upperbound_x = upperbound

if x_val is None:
    x_val = random.randint(-5, 5)

if y_val is None:
    y_val = random.randint(-5, 5)

f = x * x_val + y * y_val

f_x = integrate(f, (y, lowerbound_y, upperbound_y))

F_X = integrate(f_x, (x, lowerbound_x, x))

E_X = integrate(x * f_x, (x, lowerbound_x, upperbound_x))

E_X2 = integrate(x * x  * f_x, (x, lowerbound_x, upperbound_x))

Var_X = integrate(x ** 2 * f_x, (x, lowerbound_x, upperbound_x)) - E_X ** 2

f_y = integrate(f, (x, lowerbound_x, upperbound_x))

F_Y = integrate(f_y, (y, lowerbound_y, y))

E_Y = integrate(y * f_y, (y, lowerbound_y, upperbound_y))

E_Y2 = integrate(y * y * f_y, (y, lowerbound_y, upperbound_y))

Var_Y = integrate(y ** 2 * f_y, (y, lowerbound_y, upperbound_y)) - E_Y ** 2

Cov_XY = integrate(x * y * f, (x, lowerbound_x, upperbound_x), (y, lowerbound_y, upperbound_y)) - E_X * E_Y

E_XY = integrate(x * y * f, (x, lowerbound_x, upperbound_x), (y, lowerbound_y, upperbound_y))

Independence = 'Yes' if Cov_XY == 0 else 'No'

Corr_XY = Cov_XY / sqrt(Var_X * Var_Y)


print("f(x,y) =", x_val,"x + ",y_val,"y")
print(lowerbound_x,"<x<",upperbound_x)
print(lowerbound_y,"<y<", upperbound_y)
print("Enter all numbers as decimals. You need to be extremely percisce.")
print("If you give up on a given problem enter 'stop' to quit")

"""
print("x_val:", x_val)
print("y_val:", y_val)
print("lowerbound_x:", lowerbound_x)
print("upperbound_x:", upperbound_x)
print("lowerbound_y:", lowerbound_y)
print("upperbound_y:", upperbound_y)
print("E(X):", E_X)
print("E(x^2):", E_X2)
print("Var(X):", Var_X)
print("E(Y):", E_Y)
print("Var(Y):", Var_Y)
print("E(y^2):", E_Y2)
print("Cov(X,Y):", Cov_XY)
print("E(X,Y):", E_XY)
print("Independence:", Independence)
"""

tolerance = 0.01

# Loop for E_X
User_EX = None
# use f_x * x and integrate over x
while User_EX != "stop":
    User_EX = input("Enter in the expected value of x, E(X): ")
    try:
        User_EX = float(User_EX)
        if abs(User_EX - E_X) < tolerance:
            print("E_X is correct!")
            break
        else:
            print("E_X is incorrect. Try again.")
    except ValueError:
        if User_EX == "stop":
            print("E(X):", E_X)
            break
        else:
            print("Invalid input. Enter a numeric value or 'stop'.")

# Loop for E_X2
# use f_x * x^2 and integrate over x
User_EX2 = None
while User_EX2 != "stop":
    User_EX2 = input("Enter in the expected value of x^2, E(X^2): ")
    try:
        User_EX2 = float(User_EX2)
        if abs(User_EX2 - E_X2) < tolerance:
            print("E(X^2) is correct!")
            break
        else:
            print("E(X^2) is incorrect. Try again.")
    except ValueError:
        if User_EX2 == "stop":
            print("E(X^2):", E_X2)
            break
        else:
            print("Invalid input. Enter a numeric value or 'stop'.")

# Loop for Var_X
# Var x = E(x^2) - E(x)^2
User_VarX = None
while User_VarX != "stop":
    User_VarX = input("Enter in the variance of x, Var(X): ")
    try:
        User_VarX = float(User_VarX)
        if abs(User_VarX - Var_X) < tolerance:
            print("Var(X) is correct!")
            break
        else:
            print("Var(X) is incorrect. Try again.")
    except ValueError:
        if User_VarX == "stop":
            print("Var(X):", Var_X)
            break
        else:
            print("Invalid input. Enter a numeric value or 'stop'.")


# Loop for E_Y
# use f_y * y and integrate over y
User_EY = None
while User_EY != "stop":
    User_EY = input("Enter in the expected value of y, E(Y): ")
    try:
        User_EY = float(User_EY)
        if abs(User_EY - E_Y) < tolerance:
            print("E(Y) is correct!")
            break
        else:
            print("E(Y) is incorrect. Try again.")
    except ValueError:
        if User_EY == "stop":
            print("E(Y):", E_Y)
            break
        else:
            print("Invalid input. Enter a numeric value or 'stop'.")
# use f_y * y^2 and integrate over y
# Loop for E_Y2
User_EY2 = None
while User_EY2 != "stop":
    User_EY2 = input("Enter in the expected value of y^2, E(Y^2): ")
    try:
        User_EY2 = float(User_EY2)
        if abs(User_EY2 - E_Y2) < tolerance:
            print("E(Y^2) is correct!")
            break
        else:
            print("E(Y^2) is incorrect. Try again.")
    except ValueError:
        if User_EY2 == "stop":
            print("E(Y^2):", E_Y2)
            break
        else:
            print("Invalid input. Enter a numeric value or 'stop'.")

#Loop for Var_Y
# Var y = E(y^2) - E(y)^2
User_VarY = None
while User_VarY != "stop":
    User_VarY = input("Enter in the variance of y, Var(Y): ")
    try:
        User_VarY = float(User_VarY)
        if abs(User_VarY - Var_Y) < tolerance:
            print("Var(Y) is correct!")
            break
        else:
            print("Var(Y) is incorrect. Try again.")
    except ValueError:
        if User_VarY == "stop":
            print("Var(Y):", Var_Y)
            break
        else:
            print("Invalid input. Enter a numeric value or 'stop'.")

# Loop for E_XY
# E(XY) = x*y f(x,y) integral over x and y
User_EXY = None
while User_EXY != "stop":
    User_EXY = input("Enter in the expected value of x*y E(X,Y): ")
    try:
        User_EXY = float(User_EXY)
        if abs(User_EXY - E_XY) < tolerance:
            print("E(XY) is correct!")
            break
        else:
            print("E(XY) is incorrect. Try again.")
    except ValueError:
        if User_EXY == "stop":
            print("E(XY):", E_XY)
            break
        else:
            print("Invalid input. Enter a numeric value or 'stop'.")

#Cov (XY) = E(XY) - E(X)E(Y)
# Loop for Cov_XY
User_CovXY = None
while User_CovXY != "stop":
    User_CovXY = input("Enter in the covariance of x and y Cov(X,Y): ")
    try:
        User_CovXY = float(User_CovXY)
        if abs(User_CovXY - Cov_XY) < tolerance:
            print("Cov(X,Y) is correct!")
            break
        else:
            print("Cov(X,Y) is incorrect. Try again.")
    except ValueError:
        if User_CovXY == "stop":
            print("Cov(X,Y):", Cov_XY)
            break
        else:
            print("Invalid input. Enter a numeric value or 'stop'.")

# if Cov = 0 then independent
Independence = None
while Independence != "stop":
    Independence = input("Are X and Y independent? (Yes/No): ").strip().lower()
    if Independence == "yes" and Cov_XY == 0:
        print("Independence is correct!")
        break
    elif Independence == "no" and Cov_XY != 0:
        print("Independence is correct!")
        break
    elif Independence == "stop":
        print("Independence:", Independence)
        break
    else:
        print("Independence is incorrect. Try again (Yes/No or 'stop').")

# corr(x,y) = Cov(x,y)/sqrt(var(x)*(var(y)))
User_Corr_XY = None
while User_Corr_XY != 'stop':
    User_Corr_XY = input("Enter in the Correlation, Corr(X,Y)")
    try:
        User_Corr_XY = float(User_Corr_XY)
        if abs(User_Corr_XY - Corr_XY) < tolerance:
            print("Corr(X,Y is correct!")
            break
        else:
            print("Corr(X,Y) is incorrect. Try again.")
    except ValueError:
        if User_Corr_XY == "stop":
            print("Corr(X,Y)", Corr_XY)
            break
        else: 
             print("Invalid input. Enter a numeric value or 'stop'.")
        