import Engine
import Primitives

SCREEN_SIZE = (1400, 800)
CAPTION = "3D"
BACKGROUND_COLOR = "black"
FPS = 30
FOV = 90

class Main(Engine.Engine):
    def __init__(self, screen_size: tuple, caption: str, background_color, fps: int = 60, fov: float = 90):
        super().__init__(screen_size, caption, background_color, fps, fov)
    
    def setup(self):
        super().setup()

        # Triangles for a mesh
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
            Primitives.Triangle([ [0, 0, 1], [0, 1, 0], [0, 0, 0] ]),

            # Top
            Primitives.Triangle([ [0, 1, 0], [0, 1, 1], [1, 1, 1] ]),
            Primitives.Triangle([ [0, 1, 0], [1, 1, 1], [1, 1, 0] ]),

            # Bottom
            Primitives.Triangle([ [1, 0, 1], [0, 0, 1], [0, 0, 0] ]),
            Primitives.Triangle([ [1, 0, 1], [0, 0, 0], [1, 0, 0] ])
        ]

        # A cube mesh (uses the previously defined triangles)
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
                self.mesh_cube.triangles[i].vectors[j] = self.transformer.rotate(self.mesh_cube.triangles[i].vectors[j], 0.5 * self.dt, 0.75 * self.dt, 1 * self.dt)
                self.mesh_cube.triangles[i].vectors[j] = self.transformer.translate(self.mesh_cube.triangles[i].vectors[j], 0, 0, 3)
    
    def render(self):
        # Project cube's coordinates from 3D space to a 2D screen
        self.mesh_cube.projected_mesh = self.projection.mesh(self.mesh_cube)
        self.draw.mesh(self.mesh_cube)

if __name__ == "__main__":
    engine = Main(SCREEN_SIZE, CAPTION, BACKGROUND_COLOR, FPS, FOV)
    engine.start()