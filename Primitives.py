import math

class Triangle:
    def __init__(self, vectors: list[list[float]]):
        self.vectors = vectors

    def normal(self):
        ### Gets the normal line of the triangle

        # Define the normal vector (return value), and the two lines used to calculate it
        normal = line1 = line2 = [None] * 3

        line1 = [self.vectors[1][i] - self.vectors[0][i] for i in range(3)]
        line2 = [self.vectors[2][i] - self.vectors[0][i] for i in range(3)]

        normal[0] = line1[1] * line2[2] - line1[2] * line2[1]
        normal[1] = line1[2] * line2[0] - line1[0] * line2[2]
        normal[2] = line1[0] * line2[1] - line1[1] * line2[0]

        ## Normalize the normal (...) to a unit vector

        # Calculate length of vector by Pythagorean theorem
        length = math.sqrt(normal[0] ** 2 + normal[1] ** 2 + normal[2] ** 2)
        
        # Divide individual components of vector by length (for a vector with magnitude 1)
        normal[0] /= length
        normal[1] /= length
        normal[2] /= length

        return normal


class Mesh:
    def __init__(self, triangles: list):
        self.triangles = triangles
        self.projected_mesh = self