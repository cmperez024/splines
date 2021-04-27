# BASED OFF STACK EXCHANGE, but refactored to make it much cleaner:
# Had to refernce other code because the math was very hard to wrap my head around
# https://computergraphics.stackexchange.com/questions/7627/b-spline-curve-generation-in-python


# An advantage of B-splines is that, unlike Bezier curves, the degree of an individual spline is not tied to
# the number of control points given. However, it is more computationally expensive to evaluate B-splines.

# First generate sequence of knots given n and k
# n + 1 is the number of control points, k is the degree
def knots(n, k):
    T = np.zeros(n + k + 1)

    for i in range(n + k + 1):
        if i < k:
            T[i] = 0
        elif i <= n:
            T[i] = i - k + 1 
        else:
            T[i] = n - k + 2 

  # Return the values
    return T


# https://cran.r-project.org/web/packages/crs/vignettes/spline_primer.pdf page 5

def alpha(i, k, x, T): #coefficients for Cox-de Boor recursive formula, with avoidance of division by 0
    if T[i+k] != T[i]:
        return (x - T[i]) / (T[i+k] - T[i])
    else:
        return 0

def spline_basis(i, k, x, T):
  # For first degree, simple case
    if k == 1:
        return (1.0 if (T[i] <= x < T[i+1]) else 0.0)

  # For other degrees, compute more complex recursion formula
    else:
        B1 = alpha(i, k-1, x, T)*spline_basis(i, k-1, x, T)
        B2 = (1 - alpha( i+1, k-1, x, T))*spline_basis(i+1, k-1, x, T)

        return B1 + B2
  
    
# need control points
def spline_combination(n, k, P):
  # P is a vector of control points
  
    # Get the knot values
    T = knots(n, k)
    # print(T)
    # print(len(T))
    # print(k + n + 1)
    # Specify range
    u = np.arange(T[k - 1], T[n + 1], 0.01)
    # Try replacing it with equivalent:
    #u = np.linspace(T[k-1], T[n+1], 500). Why does horizontal line segment appear?

    Bx = np.zeros(len(u))
    By = np.zeros(len(u))
    # print(u)
    # print(len(Bx))
    # print(len(By))
    # print(n+1)
    # print(len(u))
    for i in range(n + 1):
        for j in range(len(u)):
            
            N = spline_basis(i, k, u[j], T)
            
            Bx[j] += N * P[i].x()
            By[j] += N * P[i].y()
            
            # print(f"{(i,j)}: ", Bx[j], By[j])          
            # if i == j == 1:
            #     print(b1)
            #     print(b2)
            #     print(P[i].x())
            #     print(P[i].y())
        
    
    #sub = Bx[0:10]
    #subb = By[0:10]
    #print(sub)
    #print(subb)
    return (Bx, By)
            

# EXAMPLE 
    
# Pk = []
# ctrl_x = np.array([0, 1, 2, 3, 4, 5, 6])
# ctrl_y = np.sin(ctrl_x) * np.cos(ctrl_x)


# for i in range(len(ctrl_x)):
    # Pk.append(CtrlPoint(ctrl_x[i], ctrl_y[i]))


# n = number of points - 1
# k cannot exceed the number of control points
# k <= len(P)
# k = 3
# x, y = spline_combination(len(ctrl_x) - 1, k, Pk)

# plt.clf() 
# plt.grid()
# plt.plot(x, y)


# for i in range(len(Pk)):
  # plt.plot(Pk[i].x(), Pk[i].y(), 'bo')
  # plt.text(Pk[i].x() + 0.1, Pk[i].y(), str(i), fontsize = 14)
