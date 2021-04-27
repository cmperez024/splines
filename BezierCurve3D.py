def totalBezier3D(P, t):
    # First define the combination function
    def nCr(n, r):
        return factorial(n) / (factorial(r)*factorial(n-r))
    
    # Given control points P, the maximum degree is p - 1
    n = len(P) - 1
    
    # Generate the parametric expression
    u  = syp.symbols('u')
    Bx = 0
    By = 0
    Bz = 0
    # Given P control points, have degree from 0 to p - 1 = n
    for i in range(len(P)):
        Bx += nCr(n, i) * ((1-u)**(n-i)) * (u**i) * P[i].x()
        By += nCr(n, i) * ((1-u)**(n-i)) * (u**i) * P[i].y()
        Bz += nCr(n, i) * ((1-u)**(n-i)) * (u**i) * P[i].z()
  
    # Now we have the expressions. convert each to a numpy-ready function
    Bx_func = lambdify(u, Bx, 'numpy')
    By_func = lambdify(u, By, 'numpy')
    Bz_func = lambdify(u, Bz, 'numpy')
    
    # Evaluate the points given the linspace
    Bx_val = Bx_func(t)
    By_val = By_func(t)
    Bz_val = Bz_func(t)
    
    return (Bx_val, By_val, Bz_val)



# Example
    
# https://mathworld.wolfram.com/Helix.html

# control points in helix form
# P_space = np.linspace(0, 6*np.pi, 30)

# create control points
# r = 1
# c = 1
# x_p = r * np.cos(P_space)
# y_p = r * np.sin(P_space)
# z_p = c * P_space

# P = []
# for i in range(len(P_space)):
    # P.append(CtrlPoint3D(x_p[i], y_p[i], z_p[i]))


# t = np.linspace(0, 1, 1000)
# Bx, By, Bz = totalBezier3D(P, t)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')

# https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
# ax.scatter(x_p, y_p, z_p, c=z_p, cmap='rainbow', linewidth=0.5);

# plt.plot(Bx, By, Bz)