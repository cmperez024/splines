def generatePoints(x0, y0, x1, y1, x2, y2, x3, y3):  
    t = np.linspace(0, 1, 100)
    Pk = [CtrlPoint(x0, y0), CtrlPoint(x1, y1), CtrlPoint(x2, y2), CtrlPoint(x3, y3)]
    
    x = Pk[0].x() * (1-t)**3 + 3 * Pk[1].x() * t *(1-t)**2 + 3*Pk[2].x() * (t**2) * (1 - t) + Pk[3].x()*t**3
    y = Pk[0].y() * (1-t)**3 + 3 * Pk[1].y() * t *(1-t)**2 + 3*Pk[2].y() * (t**2) * (1 - t) + Pk[3].y()*t**3 
    
   
    
    for i in range(len(Pk)):
        plt.plot(Pk[i].x(), Pk[i].y(), "bo")
        plt.text(Pk[i].x() + 0.2, Pk[i].y() - 0.2, str(i), fontsize = 16.0)
    plt.grid()
    return plt.plot(x,y)

#Example
#generatePoints(0, 0, 1, 2, 2, 1, 3, 4)


def polyInter(xvals,yvals):
    matrix = np.zeros((len(xvals),len(xvals)))
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row,column] = xvals[row]**column
    coefficients = np.linalg.solve(matrix,yvals)
    return coefficients



# Modded version to work with controlpoint class
def getPointsMod(anchorX,anchorY):
    # Create dummy variables so params aren't modified
    # We need to keep the original list of anchors in tact
    xvals = anchorX[:]
    yvals = anchorY[:]

    pointnumber = len(xvals)
    n = pointnumber - 1
    index = 2
    while index <= len(xvals)-1:
        xvals.insert(index, 0)
        yvals.insert(index, 0)
        index+= 2
    for i in range(1,len(xvals)-1):
        xvals[i] *=2
        yvals[i] *=2
    def bigmatrix(pointnumber):
        n = pointnumber -1
        matrix = np.zeros((2*n,2*n))
        matrix[0,0:2] = [2,-1]
        matrix[-1,2*n-2], matrix[-1, 2*n-1] = -1, 2
        c1coefficients = [1, 1]
        c2coefficients = [1, -2, 2, -1]
        c1columnstart = 1
        rows = 1
        while rows in range(1,2*n-2):
            matrix[rows, c1columnstart:c1columnstart + 2] = c1coefficients
            c1columnstart += 2
            rows += 2
        morerows = 2
        c2columnstart = 0
        while morerows in range(2,2*n-1):
            matrix[morerows, c2columnstart:c2columnstart+4] = c2coefficients
            c2columnstart += 2
            morerows +=2
        return matrix
    xcontrols = np.linalg.solve(bigmatrix(pointnumber),xvals)
    ycontrols = np.linalg.solve(bigmatrix(pointnumber),yvals)

    controls = []
    for i in range(len(xcontrols)):
        controls.append(CtrlPoint(xcontrols[i], ycontrols[i]))

    return controls


# Given a set of control points and t range, compute spline points
# We are creating an array of splines. each spline is represented by a tuple containing x and y points
def spliner(anchorX, anchorY, C, t):

  # Anchor X has x-coordinated for the anchor points etc.
  # C contains the intermediate control points that are inbetween the anchors
  # t contains the t values of the spline, should be [0,1]
    splines = []
    c_index = 0

  # given n anchors, there are n - 1 splines
  for i in range(len(anchorX) - 1):
    
    # Spline i needs anchor[i] and anchor[i+1] as beginning and end.
    # Spline i needs C[c_index] and C[c_index + 1] as internal control points

    Bx = anchorX[i] * (1-t)**3 + 3 * C[c_index].x() * t * (1-t)**2 + 3*C[c_index + 1].x() * (t**2) * (1 - t) + anchorX[i + 1]*t**3
    By = anchorY[i] * (1-t)**3 + 3 * C[c_index].y() * t * (1-t)**2 + 3*C[c_index + 1].y() * (t**2) * (1 - t) + anchorY[i + 1]*t**3
    c_index = c_index + 2

    # Add the x and y points for a single spline as a tuple
    splines.append( (Bx, By) )

    return splines


#Example

# anchorX = [0, -5, -5, 0]
# anchorY = [0, 9, -5, 4]

# t = np.linspace(0, 1, 100)

# controls = getPointsMod(anchorX, anchorY)
# splines = spliner(anchorX, anchorY, controls, t)

# for i in range(len(splines)):
#     Bix, Biy = splines[i]
#     plt.plot(Bix, Biy)



# for i in range(len(controls)):
#     plt.plot(controls[i].x(), controls[i].y(), 'bo')
#     plt.text(controls[i].x() + 0.25, controls[i].y(), "ctrl" + str(i), fontsize = 16)

# for i in range(len(anchorX)):
#     plt.plot(anchorX[i], anchorY[i], 'ro')
#     plt.text(anchorX[i] - 0.1, anchorY[i] + 1, "a" + str(i), fontsize = 14)