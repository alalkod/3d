class Transform:
    def translate(self, vector, x, y, z):
        return [vector[0] + x, vector[1] + y, vector[2] + z]
    
    def rotate(self, vector, x: list, y: list, z: list):
        pass