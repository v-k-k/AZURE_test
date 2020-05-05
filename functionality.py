from point import Point


def show(tab):
    print('Table 10x10:')
    print('   0  1  2  3  4  5  6  7  8  9')
    row = 0
    for i in tab:
        print(row, ''.join(i))
        print()
        row += 1


def close(p1, p2):
    check = abs(p1.y - p2.y) + abs(p1.x - p2.x)
    if check == 0:
        raise ValueError("Wrong point!!!")
    elif check == 1 or (p1.y != p2.y and p1.x != p2.x and check == 2):
        return True
    else:
        return False


def merge_groups(pl):
    if len(pl) > 1:
        start = len(pl) - 2
        while start != -1:
            for current in range(len(pl) - 1, start, -1):
                if pl[start].intersection(pl[current]):
                    pl[start] = pl[start].union(pl[current])
                    pl.pop(current)
            start -= 1
