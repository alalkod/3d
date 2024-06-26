# 3D

import pygame

import Transforms
import Draw
import Projection

pygame.init()


class Engine:
    def __init__(self, screen_size: tuple, caption: str, background_color, fps: int = 60, fov: float = 90):
        self.screen_size = screen_size
        self.aspect_ratio = self.screen_size[1] / self.screen_size[0]

        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.fov = fov

        self.camera = [0, 0, 0]

        self.dt = None

        self.background_color = background_color
        
        self.running = False

        pygame.display.set_caption(caption)

    
    def setup(self):
        # Ran once before rendering

        # Set up projection
        self.projection = Projection.Projection(screen_size=self.screen_size, aspect_ratio=self.aspect_ratio, fov=self.fov)

        # Set up draw
        self.draw = Draw.Draw(self.screen, self.camera)

        # Set up transforms
        self.transformer = Transforms.Transform()
    
    def update(self):
        pass
    
    def render(self):
        pass

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