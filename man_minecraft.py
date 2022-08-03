from drawer import draw_minecraft

LIGHT_CELLS = [
    (i, j) for i in range(2, 6) for j in range(2, 8)
]
BLACK_CELLS = [
    (4, 3), (4, 6)
]
WHITE_CELLS = [
    (4, 2), (4, 7)
]

BROWN_CELLS = [
    (0, 0), (0, 9), (1, 0), (1, 9),
    (4, 9), (5, 0), (5, 4), (5, 5),
    (5, 8), (6, 0),
    (6, 9), (7, 0), (7, 1), (7, 2), (7, 9),
    (8, 1), (8, 2), (8, 7), (8, 8), (8, 9), (9, 0),
    (9, 4), (9, 5), (9, 8), (10, 1),
    (10, 2), (10, 7), (10, 8), (10, 9),
]
SUPER_BROWN_CELLS = [
                        (2, 0), (2, 1), (2, 8), (2, 9),
                        (6, 3), (6, 6),
                        (7, 3), (7, 4), (7, 5), (7, 6)
                    ] + [(i, j) for i in range(2) for j in range(1, 9)]


def define_color(row: int, column: int) -> str:
    color = "#B77A4B"
    if (row, column) in LIGHT_CELLS:
        color = "#D7A680"
    if (row, column) in BLACK_CELLS:
        color = "black"
    elif (row, column) in WHITE_CELLS:
        color = "white"
    elif (row, column) in [(6, 4), (6, 5)]:
        color = "brown"
    elif (row, column) in BROWN_CELLS:
        color = "#875A37"
    elif (row, column) in SUPER_BROWN_CELLS:
        color = "#48301E"
    return color


draw_minecraft(define_color)
