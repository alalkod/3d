# 3D 

import math
import numpy as np

import pygame

pygame.init()

SCREEN_SIZE = (800, 600)
CAPTION = "3D"
BACKGROUND_COLOR = "black"
FPS = 60

class Triangle:
    def __init__(self, vectors: list[list[float]]):
        self.vectors = vectors


class Mesh:
    def __init__(self, triangles: list):
        self.triangles = triangles

class Engine:
    def __init__(self, screen_size: tuple, caption: str, background_color, fps: int, fov: float):
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.background_color = background_color
        
        self.running = False

        pygame.display.set_caption(caption)

        # For rendering
        self.triangles = [
            # South
            Triangle([ [0, 0, 0], [0, 1, 0], [1, 1, 0] ]),
            Triangle([ [0, 0, 0], [1, 1, 0], [1, 0, 0] ]),

            # East
            Triangle([ [1, 0, 0], [1, 1, 0], [1, 1, 1] ]),
            Triangle([ [1, 0, 0], [1, 1, 1], [1, 0, 1] ]),

            # North
            Triangle([ [1, 0, 1], [1, 1, 1], [0, 1, 1] ]),
            Triangle([ [1, 0, 1], [0, 1, 1], [0, 0, 1] ]),

            # West
            Triangle([ [0, 0, 1], [0, 1, 1], [0, 1, 0] ]),
            Triangle([ [0, 1, 1], [0, 1, 0], [0, 0, 0] ]),

            # Top
            Triangle([ [0, 1, 0], [0, 1, 1], [1, 1, 1] ]),
            Triangle([ [0, 1, 0], [1, 1, 1], [1, 1, 0] ]),

            # Bottom
            Triangle([ [0, 0, 0], [0, 0, 1], [1, 0, 1] ]),
            Triangle([ [0, 0, 0], [1, 0, 1], [1, 0, 0] ])
        ]

        self.mesh_cube = Mesh(self.triangles)
        
        # Projection
        self.z_near = 0.1
        self.z_far = 1000
        self.fov = 90
        self.aspect_ratio = self.screen_size[1] / self.screen_size[0]
        self.fov_radians = 1 / math.tan( (self.fov * 0.5) / (180 * math.pi) )

        self.projection_matrix = np.array([ [ [0] * 4 ] * 4 ])

        self.projection_matrix[0][0] = self.aspect_ratio * self.fov_radians
        self.projection_matrix[1][1] = self.fov_radians
        self.projection_matrix[2][2] = self.z_far / (self.z_far - self.z_near)
        self.projection_matrix[3][2] = (-self.z_far * self.z_near) / (self.z_far - self.z_near)
        self.projection_matrix[2][3] = 1

    def render(self):
        for triangle in self.mesh_cube.triangles:
            continue
        # TODO: create Projection class to handle 3D projection to 2D space

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def start(self):
        self.running = True

        while self.running:
            self.event()

            self.screen.fill(self.background_color)
            self.render()

            pygame.display.update()

            self.clock.tick(self.fps)

        pygame.quit()

if __name__ == "__main__":
    engine = Engine(SCREEN_SIZE, CAPTION, BACKGROUND_COLOR, FPS)
    engine.start()
