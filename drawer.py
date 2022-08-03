import tkinter as tk

ROWS = 12
COLUMNS = 10
HEIGHT = int(297 * 2.5)
WIDTH = int(210 * 2.5)


def draw_minecraft(define_color):
    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    mainframe = tk.Frame(root)

    mainframe.pack(fill=tk.BOTH)

    for row in range(ROWS):
        for column in range(COLUMNS):
            cell = tk.Frame(mainframe, width=WIDTH // COLUMNS,
                            height=HEIGHT // ROWS, bg=define_color(row, column))
            cell.grid(row=row, column=column)
            cell.configure(highlightthickness=0)

    root.mainloop()
