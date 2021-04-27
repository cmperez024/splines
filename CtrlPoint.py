class CtrlPoint:
    def __init__(self, x_i = 0, y_i = 0):
        self.x_i = x_i
        self.y_i = y_i
    def getPoint(self):
        return (self.x_i, self.y_i)
    def __str__(self):
        return str(self.getPoint())
    def x(self):
        return self.x_i
    def y(self):
        return self.y_i
    
class CtrlPoint3D:
    def __init__(self, xi = 0, yi = 0, zi = 0):
        self.xi = xi
        self.yi = yi
        self.zi = zi
    def getPoint(self):
        return (self.xi, self.yi, self.zi)
    def __str__(self):
        return str(self.getPoint())
    def x(self):
        return self.xi
    def y(self):
        return self.yi
    def z(self):
        return self.zi