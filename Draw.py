import pygame

class Draw:
    def __init__(self, screen, camera):
        self.screen = screen
        self.camera = camera

    def triangle(self, triangle):
        pygame.draw.polygon(self.screen, 'white', (triangle.vectors[0], triangle.vectors[1], triangle.vectors[2]))
        # pygame.draw.line(self.screen, "white", (triangle.vectors[0][0], triangle.vectors[0][1]), (triangle.vectors[1][0], triangle.vectors[1][1]))
        # pygame.draw.line(self.screen, "white", (triangle.vectors[1][0], triangle.vectors[1][1]), (triangle.vectors[2][0], triangle.vectors[2][1]))
        # pygame.draw.line(self.screen, "white", (triangle.vectors[0][0], triangle.vectors[0][1]), (triangle.vectors[2][0], triangle.vectors[2][1]))
    
    def mesh(self, mesh):
        for triangle in mesh.projected_mesh.triangles:
            normal = triangle.normal()
            # In the case that the face of the mesh is behind another face, do not draw it.
            #if normal[2] <= 0:
            if normal[0] * (triangle.vectors[0][0] - self.camera[0]) + normal[1] * (triangle.vectors[0][1] - self.camera[1]) + normal[2] * (triangle.vectors[0][2] - self.camera[2]) < 0:
                continue
            self.triangle(triangle)