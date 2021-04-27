def getPoints3d(anchorX,anchorY,anchorZ):
    # Create dummy variables so params aren't modified
    # We need to keep the original list of anchors in tact
    xvals = anchorX[:]
    yvals = anchorY[:]
    zvals = anchorZ[:]

    pointnumber = len(xvals)
    n = pointnumber - 1
    index = 2
    while index <= len(xvals)-1:
        xvals.insert(index, 0)
        yvals.insert(index, 0)
        zvals.insert(index, 0)
        index+= 2
    for i in range(1,len(xvals)-1):
        xvals[i] *=2
        yvals[i] *=2
        zvals[i] *=2
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
    zcontrols = np.linalg.solve(bigmatrix(pointnumber),zvals)

    controls = []
    for i in range(len(xcontrols)):
      controls.append(CtrlPoint3D(xcontrols[i], ycontrols[i],zcontrols[i]))

    return controls

def spliner3d(anchorX, anchorY, anchorZ, C, t):

  # C contains the intermediate control points that are inbetween the anchors
  # t contains the t values of the spline, should be [0,1]
  splines = []
  c_index = 0

  # given n anchors, there are n - 1 splines
  for i in range(len(anchorX) - 1):


    Bx = anchorX[i] * (1-t)**3 + 3 * C[c_index].x() * t * (1-t)**2 + 3*C[c_index + 1].x() * (t**2) * (1 - t) + anchorX[i + 1]*t**3
    By = anchorY[i] * (1-t)**3 + 3 * C[c_index].y() * t * (1-t)**2 + 3*C[c_index + 1].y() * (t**2) * (1 - t) + anchorY[i + 1]*t**3
    Bz = anchorZ[i] * (1-t)**3 + 3 * C[c_index].z() * t * (1-t)**2 + 3*C[c_index + 1].z() * (t**2) * (1 - t) + anchorZ[i + 1]*t**3
    c_index = c_index + 2

    # Add the x and y points for a single spline as a tuple
    splines.append( (Bx, By, Bz) )

  return splines 


# Example 
  
# controls = getPoints3d(anchorX, anchorY, anchorZ)
# t = np.linspace(0, 1, 100)
# splines = spliner3d(anchorX, anchorY, anchorZ, controls, t)
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# for i in range(len(splines)):
#   Bix, Biy, Biz = splines[i]
#   plt.plot(Bix, Biy, Biz)