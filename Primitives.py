class Triangle:
    def __init__(self, vectors: list[list[float]]):
        self.vectors = vectors


class Mesh:
    def __init__(self, triangles: list):
        self.triangles = triangles
        self.projected_mesh = self