import sys
def point_position(cx, cy, r, x, y):
    dist_sq = (x - cx) ** 2 + (y - cy) ** 2
    r_sq = r ** 2
    eps = 1e-12
    if abs(dist_sq - r_sq) < eps:
        return 0  # на окружности
    elif dist_sq < r_sq:
        return 1  # внутри
    else:
        return 2  # снаружи
def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py circle_file points_file")
        return
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    with open(circle_file, 'r', encoding='utf-8') as f:
        line1 = f.readline().strip()
        cx, cy = map(float, line1.split())
        r = float(f.readline().strip())
    with open(points_file, 'r', encoding='utf-8') as f:
        points = [line.strip() for line in f if line.strip()]
    for p in points:
        x, y = map(float, p.split())
        pos = point_position(cx, cy, r, x, y)
        print(pos)
if __name__ == "__main__":
    main()




