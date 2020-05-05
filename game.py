from functionality import *


LENGTH = 10
table = [[' - '] * LENGTH for _ in range(LENGTH)]
pool = []
added = got = False
LINE = []


def line(point, grp, direction):
    global LINE
    LINE.append(point)
    next_point = Point(point.x + direction[0], point.y + direction[1])
    while next_point in grp:
        px = next_point.x
        py = next_point.y
        LINE.append(Point(px, py))
        if len(LINE) == 4:
            return True
        next_point.x += direction[0]
        next_point.y += direction[1]
    LINE = []
    return False


def find_line(grp):
    for point in grp:
        if line(point, grp, (0, 1)):
            return True
        if line(point, grp, (1, 0)):
            return True
        if line(point, grp, (1, 1)):
            return True
        if line(point, grp, (0, -1)):
            return True
        if line(point, grp, (-1, 0)):
            return True
        if line(point, grp, (-1, -1)):
            return True
        if line(point, grp, (-1, 1)):
            return True
        if line(point, grp, (1, -1)):
            return True
    return False


def launch_app():
    global LINE, LENGTH, table, got, pool, added
    while not got:
        show(table)
        x = int(input("Give me X: "))
        y = int(input("Give me Y: "))
        table[y][x] = ' + '
        if len(pool):
            for group in pool:
                for pt in group:
                    if close(Point(x, y), pt):
                        group.add(Point(x, y))
                        added = True
                        break
            if added:
                merge_groups(pool)
                added = False
            else:
                pool.append({Point(x, y)})
            for group in pool:
                tmp = [(p.x, p.y) for p in group]
                if find_line(group):
                    got = True
                    break
        else:
            pool.append({Point(x, y)})

    for pt in LINE:
        table[pt.y][pt.x] = ' 0 '

    show(table)


if __name__ == '__main__':
    launch_app()
