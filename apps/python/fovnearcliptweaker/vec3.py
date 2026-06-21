import math

class vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, a):
        return vec3(self.x + a.x, self.y + a.y, self.z + a.z)
    
    def __sub__(self, a):
        return vec3(self.x - a.x, self.y - a.y, self.z - a.z)

    def __mul__(self, a):
        return vec3(self.x * a.x, self.y * a.y, self.z * a.z)

    def __idiv__(self, a):
        self.x /= a.x
        self.y /= a.y
        self.z /= a.z

    def __iadd__(self, a):
        self.x += a.x
        self.y += a.y
        self.z += a.z

    def distance(self, a):
        d = self - a
        distance = math.sqrt(d.x * d.x + d.y * d.y + d.z * d.z)
        return distance
