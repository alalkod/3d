import math
import numpy as np

import Primitives

class Projection:
    def __init__(self, screen_size, aspect_ratio, z_near = 0.1, z_far = 1000, fov = 90):
        self.screen_size = screen_size
        self.aspect_ratio = aspect_ratio

        self.z_near = z_near
        self.z_far = z_far
        self.fov = fov
        self.fov_radians = 1 / math.tan(math.radians(self.fov) / 2)

        self.projection_matrix = [
            [self.aspect_ratio * self.fov_radians, 0,                0,                                                        0],
            [0,                                    self.fov_radians, 0,                                                        0],
            [0,                                    0,                self.z_far / (self.z_far - self.z_near),                  1],
            [0,                                    0,                (-self.z_far * self.z_near) / (self.z_far - self.z_near), 0]
        ]

    def multiply(self, vector):
        multiplied_vector = np.array(vector) @ np.array(self.projection_matrix)
        if multiplied_vector[3] != 0:
            multiplied_vector /= multiplied_vector[3]

        return multiplied_vector.tolist()
    
    def normalize(self, vector):
        return [(vector[0] + 1) * 0.5 * self.screen_size[0], (1 - vector[1]) * 0.5 * self.screen_size[1], vector[2]]
    
    def vector(self, vector):
        projected_vector = self.multiply([vector[0], vector[1], vector[2], 1])
        projected_vector = self.normalize(projected_vector)

        return projected_vector
    
    def triangle(self, triangle):
        vectors = []

        for vector in triangle.vectors:
            vector = self.vector(vector)
            vectors.append(vector)

        return Primitives.Triangle(vectors)

    def mesh(self, mesh):
        triangles = []

        for triangle in mesh.triangles:
            triangle = self.triangle(triangle)
            triangles.append(triangle)
        
        return Primitives.Mesh(triangles)