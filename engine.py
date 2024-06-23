# 3D

import pygame

import Transforms
import Draw
import Projection
import Primitives

pygame.init()


class Engine:
    def __init__(self, screen_size: tuple, caption: str, background_color, fps: int = 60, fov: float = 90):
        self.screen_size = screen_size
        self.aspect_ratio = self.screen_size[1] / self.screen_size[0]

        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.fov = fov

        self.dt = None

        self.background_color = background_color
        
        self.running = False

        pygame.display.set_caption(caption)

        # Meshes
        self.triangles = [
            # South
            Primitives.Triangle([ [0, 0, 0], [0, 1, 0], [1, 1, 0] ]),
            Primitives.Triangle([ [0, 0, 0], [1, 1, 0], [1, 0, 0] ]),

            # East
            Primitives.Triangle([ [1, 0, 0], [1, 1, 0], [1, 1, 1] ]),
            Primitives.Triangle([ [1, 0, 0], [1, 1, 1], [1, 0, 1] ]),

            # North
            Primitives.Triangle([ [1, 0, 1], [1, 1, 1], [0, 1, 1] ]),
            Primitives.Triangle([ [1, 0, 1], [0, 1, 1], [0, 0, 1] ]),

            # West
            Primitives.Triangle([ [0, 0, 1], [0, 1, 1], [0, 1, 0] ]),
            Primitives.Triangle([ [0, 1, 1], [0, 1, 0], [0, 0, 0] ]),

            # Top
            Primitives.Triangle([ [0, 1, 0], [0, 1, 1], [1, 1, 1] ]),
            Primitives.Triangle([ [0, 1, 0], [1, 1, 1], [1, 1, 0] ]),

            # Bottom
            Primitives.Triangle([ [0, 0, 0], [0, 0, 1], [1, 0, 1] ]),
            Primitives.Triangle([ [0, 0, 0], [1, 0, 1], [1, 0, 0] ])
        ]
    
    def setup(self):
        # Ran once before rendering

        # Set up projection
        self.projection = Projection.Projection(screen_size=self.screen_size, aspect_ratio=self.aspect_ratio, fov=self.fov)

        # Set up draw
        self.draw = Draw.Draw(self.screen)

        # Set up transforms
        self.transformer = Transforms.Transform()

        # 3D objects go here

        # A cube
        self.mesh_cube = Primitives.Mesh(self.triangles)

        # To loop through all vectors in our mesh, and transform each of them
        for i in range(len(self.mesh_cube.triangles)):
            for j in range(len(self.mesh_cube.triangles[i].vectors)):
                self.mesh_cube.triangles[i].vectors[j] = self.transformer.translate(self.mesh_cube.triangles[i].vectors[j], 0, 0, 3)
    
    def update(self):
        # To loop through all vectors in our mesh, and transform each of them
        for i in range(len(self.mesh_cube.triangles)):
            for j in range(len(self.mesh_cube.triangles[i].vectors)):
                self.mesh_cube.triangles[i].vectors[j] = self.transformer.translate(self.mesh_cube.triangles[i].vectors[j], 0, 0, -3)
                self.mesh_cube.triangles[i].vectors[j] = self.transformer.rotate(self.mesh_cube.triangles[i].vectors[j], 0.5 * self.dt, 0, 1 * self.dt)
                self.mesh_cube.triangles[i].vectors[j] = self.transformer.translate(self.mesh_cube.triangles[i].vectors[j], 0, 0, 3)
    
    def render(self):
        # Project cube's coordinates from 3D space to a 2D screen
        self.mesh_cube.projected_mesh = self.projection.mesh(self.mesh_cube)
        self.draw.mesh(self.mesh_cube)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def start(self):
        self.running = True

        self.setup()

        while self.running:
            self.dt = self.clock.tick(self.fps) / 1000

            self.event()

            self.update()
            self.screen.fill(self.background_color)
            self.render()

            pygame.display.update()

        pygame.quit()