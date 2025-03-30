def get_slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        return None  # Vertical line
    elif x1 == x2 and y1 == y2:
        return None # Same point given twice
    else:
        return (y2 - y1) / (x2 - x1)