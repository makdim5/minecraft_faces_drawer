from drawer import draw_minecraft, ROWS, COLUMNS

RED_CELLS = [(i, j) for i in range(ROWS) for j in (1, 4, 7)]

DARK_RED_CELLS = [(i, j) for i in range(ROWS) for j in (2, 5, 8)]

LIGHT_CELLS = [(i, j) for i in range(3, 7) for j in range(COLUMNS)]


def define_color(row: int, column: int) -> str:
    color = "#E98585"
    if (row, column) in RED_CELLS:
        color = "red"
    elif (row, column) in DARK_RED_CELLS:
        color = "#A01111"
    if (row, column) in LIGHT_CELLS:
        color = "white"
    return color


draw_minecraft(define_color)
