# minzhou@bu.edu

# Compute the distance between two points (x1, y1, z1), (x2, y2, z2)
def distance(x1, y1, z1, x2, y2, z2):
    return ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5


def nearestPoints(points):
    # p1 and p2 are the indexes in the points list 
    p1, p2, p3 = 0, 1, 2# Initial two points

    shortestDistance = distance(points[p1][0], points[p1][1], points[p1][2],points[p2][0], points[p2][1], points[p2][2]) # Initialize shortestDistance
    # Compute distance between every two points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1], points[i][2], points[j][0], points[j][1], points[j][2]) # Find distance
            if shortestDistance > d:
                p1, p2 = i, j # Update p1, p2 
                shortestDistance = d # New shortestDistance
    return p1, p2


def main():
    points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1], [2, 0.5, 9], [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2], [5.5, 4, -0.5]]
    print(nearestPoints(points))


main()