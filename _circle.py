class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius**2
        return area
    def circum(self):
        a=2*3.14*self.radius
        return a
    def diameters(self):
        d=2*self.radius
        return d

    
        