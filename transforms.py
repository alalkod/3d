import math
import numpy as np

class Transform:
    def translate(self, vector, x, y, z):
        return [vector[0] + x, vector[1] + y, vector[2] + z]
    
    def rotate(self, vector, theta_x, theta_y, theta_z):
        # Rotation matrices to multiply individual vectors by
        x_rotation = np.array(
            [
                [1, 0,                                  0],
                [0, math.cos(theta_x), -math.sin(theta_x)],
                [0, math.sin(theta_x),  math.cos(theta_x)]
            ]
        )
        y_rotation = np.array(
            [
                [math.cos(theta_y),  0, math.sin(theta_y)],
                [0,                  1,                 0],
                [-math.sin(theta_y), 0, math.cos(theta_y)]
            ]
        )
        z_rotation = np.array(
            [
                [math.cos(theta_z), -math.sin(theta_z), 0],
                [math.sin(theta_z),  math.cos(theta_z), 0],
                [0,                  0,                 1]
            ]
        )

        # Return the vector multiplied by all rotation matrixes (to account for rotation along multiple axis)
        return vector @ x_rotation @ y_rotation @ z_rotation