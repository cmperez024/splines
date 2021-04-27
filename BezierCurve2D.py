def totalBezier(P, t):
    # First define the combination function
    def nCr(n, r):
        return factorial(n) / (factorial(r)*factorial(n-r))
    
    # Given control points P, the maximum degree is p - 1
    n = len(P) - 1
    
    # Generate the parametric expression
    u  = syp.symbols('u')
    Bx = 0
    By = 0
    # Given P control points, have degree from 0 to p - 1 = n
    for i in range(len(P)):
        Bx += nCr(n, i) * ((1 - u)**(n - i)) * (u**i) * P[i].x()
        By += nCr(n, i) * ((1 - u)**(n - i)) * (u**i) * P[i].y()
  
    # Now we have the expressions. convert each to a numpy-ready function
    Bx_func = lambdify(u, Bx, 'numpy')
    By_func = lambdify(u, By, 'numpy')
    
    # Evaluate the points given the linspace
    Bx_val = Bx_func(t)
    By_val = By_func(t)
    
    return (Bx_val, By_val)



# EXAMPLE
# MAKE SURE TO RUN:
# 1. The code cell installing sympy and nurbs
# 2. The code cell importing the modules
# 3. The CtrlPoint class cell
# 4. The cell above
# P = [CtrlPoint(0,0), CtrlPoint(-5,9), CtrlPoint(-5,-5), CtrlPoint(0,4)]
# t = np.linspace(0, 1, 25)

# Bx, By = totalBezier(P, t)

# plt.plot(Bx, By)

# for i in range(len(P)):
    # x = P[i].x()
    # y = P[i].y()
    # plt.plot(x, y, 'o')
    # plt.text(x, y + 0.3, str(i), fontsize = 16)

# plt.grid()