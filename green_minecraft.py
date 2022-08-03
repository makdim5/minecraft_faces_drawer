from drawer import draw_minecraft

BLACK_CELLS = [(3, 2), (3, 3), (4, 2), (4, 3),
               (3, 6), (3, 7), (4, 6), (4, 7),
               (5, 4), (5, 5),
               (6, 3), (6, 4), (6, 5), (6, 6),
               (7, 3), (7, 4), (7, 5), (7, 6),
               (8, 3), (8, 6),
               ]

DARK_GREEN_CELLS = [
    (2, 0), (11, 0), (11, 1), (8, 2), (11, 4),
    (11, 9), (12, 8), (10, 7), (7, 7), (3, 9), (1, 9), (0, 5), (0, 7)

]

LIGHT_GREEN_CELLS = [
    (2, 8), (3, 8), (3, 4), (5, 1), (5, 3),
    (5, 6), (6, 1), (8, 5)

]


def define_color(row: int, column: int) -> str:
    color = "#80D05F"
    if (row, column) in BLACK_CELLS:
        color = "black"
    elif (row, column) in DARK_GREEN_CELLS:
        color = "#3F8B51"
    elif (row, column) in LIGHT_GREEN_CELLS:
        color = "#A3D78E"
    return color


draw_minecraft(define_color)
