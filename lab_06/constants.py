MAIN_COLOUR = "#d1d1d1"
MAIN_FRAME_COLOR = "white"
MAIN_COLOUR_LABEL_BG = "#d7d7d7"
MAIN_COLOUR_LABEL_TEXT = "black"
CANVAS_COLOUR = "white"
BORDER_COLOUR = "#000000"
FILL_COLOUR = "#ffff00"

COLUMNS = 27

WINDOW_WIDTH = 1900
WINDOW_HEIGHT = 1000

DATA_SITUATION = 1/4
BORDERS_SPACE = 10

DATA_FRAME_WIGHT = WINDOW_WIDTH * DATA_SITUATION - BORDERS_SPACE
DATA_FRAME_HEIGHT = WINDOW_HEIGHT - 2 * BORDERS_SPACE

LIST_FRAME = 0.6 * DATA_SITUATION
LIST_FRAME_WIGHT = WINDOW_WIDTH * LIST_FRAME - BORDERS_SPACE
LIST_FRAME_HEIGHT = DATA_FRAME_HEIGHT

CANVAS_SITUATION = 1 - DATA_SITUATION - LIST_FRAME
CANVAS_WIDTH = int(WINDOW_WIDTH * CANVAS_SITUATION - 2 * BORDERS_SPACE)
CANVAS_HEIGHT = int(WINDOW_HEIGHT - 2 * BORDERS_SPACE)