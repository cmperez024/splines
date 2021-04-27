# Requires BSpline2D

def spline_combination_3D(n, k, P):
  # P is a vector of control points
  
    # Get the knot values
    T = knots(n, k)
    #print(len(P), len(T))
    #print(T)
    # Specify range
    u = np.arange(T[k-1], T[n+1], 0.01)

    Bx = np.zeros(len(u))
    By = np.zeros(len(u))
    Bz = np.zeros(len(u))

    for i in range(n+1):
        for j in range(len(u)):
            b = spline_basis(i, k, u[j], T)
            Bx[j] += b * P[i].x()
            By[j] += b * P[i].y()
            Bz[j] += b * P[i].z()
        
    return (Bx, By, Bz)


# Example 
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

    
# n = number of points - 1
# n = len(P) - 1
# k = 6
# Bx, By, Bz = spline_combination_3D(n, k, P)

# 3D plotting requires use of figure objects
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')

#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
# ax.scatter(x_p, y_p, z_p, c=z_p, cmap='rainbow', linewidth=0.5);

# plt.plot(Bx, By, Bz)