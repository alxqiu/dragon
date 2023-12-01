# from turtle import *
import math

ANGLE_DEG = -120
ANGLE_RAD = ANGLE_DEG * (math.pi / 180)

# 2d rotation matrix
MTX = [
        [math.cos(ANGLE_RAD), -math.sin(ANGLE_RAD)],
        [math.sin(ANGLE_RAD), math.cos(ANGLE_RAD)]
    ]
print(f"Rotation matrix:\n{MTX}")


"""
Because it is a fractal, it's going to require recursion

and some DP to perform memoization
"""
def rotatepts(pts : [[int, int]])->[[int, int]]:
    newpts = list(pts)

    for i in range(len(newpts)):
        pt = list(newpts[i])
        
        newpts[i] = [
            MTX[0][0]*pt[0] + MTX[0][1]*pt[1],
            MTX[1][0]*pt[0] + MTX[1][1]*pt[1]
        ]
    return newpts


def pointgen(n : int)->[[int, int]]:
    if (n < 0):
        raise Exception("Unsupported")
    
    if n == 0:
        return [[0, 0], [0, 1], [-(math.sqrt(3) / 2), 1 / 2]]
    else:
        oldpts = list(pointgen(n - 1))
        newpts = rotatepts(oldpts)

        lastold, lastnew = oldpts[-1], newpts[-1]

        delta = [
            lastold[0] - lastnew[0],
            lastold[1] - lastnew[1]
        ]

        # apply delta
        for i in range(len(newpts)):
            pt = list(newpts[i])
            newpts[i] = [
                pt[0] + delta[0],
                pt[1] + delta[1]
            ]
        newpts.reverse()
        
        oldpts.extend(newpts)
        
        return oldpts
            

        
