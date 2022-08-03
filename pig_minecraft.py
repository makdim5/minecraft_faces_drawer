from drawer import draw_minecraft

BLACK_CELLS = [
    (4, 1), (4, 8)
]
WHITE_CELLS = [
    (4, 2), (4, 7)
]

BROWN_CELLS = [
    (6, 3), (6, 6)
]
SUPER_LIGHT_CELLS = [
    (7, 3), (7, 4), (7, 5),
    (5, 6), (5, 4), (5, 5),
]


def define_color(row: int, column: int) -> str:
    color = "#F9B5B5"
    if (row + column) % 2 == 1:
        color = "#FFBABA"
    if (row, column) in BLACK_CELLS:
        color = "black"
    elif (row, column) in WHITE_CELLS:
        color = "white"
    elif (row, column) in BROWN_CELLS:
        color = "brown"
    elif (row, column) in SUPER_LIGHT_CELLS:
        color = "#FFDFDF"
    elif (row, column) in [(5,3), (7,6)]:
        color = "#E1CECE"
    return color


draw_minecraft(define_color)
