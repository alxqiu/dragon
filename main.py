from pointgen import pointgen
from plot import graph_plot

ITERATIONS = 5

if __name__ == "__main__":

    pts = pointgen(ITERATIONS)
    x = []
    y = []
    
    print(f"Dragon points for iteration {ITERATIONS}")
    for pt in pts:
        print(pt)
        x.append(pt[0])
        y.append(pt[1])

    graph_plot(x, y)
    
    
