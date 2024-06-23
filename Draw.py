import pygame

class Draw:
    def __init__(self, screen):
        self.screen = screen

    def triangle(self, triangle):
        pygame.draw.line(self.screen, "white", (triangle.vectors[0][0], triangle.vectors[0][1]), (triangle.vectors[1][0], triangle.vectors[1][1]))
        pygame.draw.line(self.screen, "white", (triangle.vectors[1][0], triangle.vectors[1][1]), (triangle.vectors[2][0], triangle.vectors[2][1]))
        pygame.draw.line(self.screen, "white", (triangle.vectors[0][0], triangle.vectors[0][1]), (triangle.vectors[2][0], triangle.vectors[2][1]))
    
    def mesh(self, mesh):
        for triangle in mesh.projected_mesh.triangles:
            normal = triangle.normal()
            if normal[2] <= 0:
                continue
            self.triangle(triangle)