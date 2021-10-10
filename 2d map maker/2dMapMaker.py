# Imports
import pygame
import numpy as np
import loadImages
import arrangeMap
import validMapFormat

pygame.init()

# Window and Resolution
RES = (800, 600)
WIN = pygame.display.set_mode(RES)

# Title
pygame.display.set_caption("Map Maker")

# Icon
icon = pygame.image.load("MapIcon.png")
pygame.display.set_icon(icon)

# Clock
clock = pygame.time.Clock()

# Sounds
spraying = pygame.mixer.Sound("spraying.wav")
rattle = pygame.mixer.Sound("spray can rattle.wav")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
light_grey = (125, 125, 125)
light_light_grey = (180, 180, 180)
dark_grey = (50, 50, 50)
dark_dark_grey = (30, 30, 30)
orange = (150, 80, 0)

# Fonts and Texts
font0 = pygame.font.SysFont('Arial', 30)
font1 = pygame.font.SysFont('Arial', 27)
font2 = pygame.font.SysFont('Arial', 24)
font3 = pygame.font.SysFont('Papyrus', 30)

text_save = font0.render("Save Map", True, black)
text_clear = font1.render("Clear Canvas", True, black)
text_AddBG = font1.render("Background", True, black)
text_palette = font0.render("Palette", False, white)

# Images
images = loadImages.loadImages()
Palette_images = images[0]
pix = images[1]
empty = images[2][0]
bg = images[2][1]
frame = images[2][2]

# Index Arranging
display_index = (25, 275)
button_num = 0
button_indexes = []
for row in range(5):
    for column in range(4):
        button_indexes.append((button_num, display_index))
        button_num += 1
        display_index = (display_index[0] + 100, display_index[1])
    display_index = (25, display_index[1] + 100)

# Variables
selected_paint = 0
bg_mode = 1
bg_button_wait = 0

# Indexes
Button_Name = ("x index", "y index", "width", "length")
Clear_Button = (600, 515, 150, 70)
Save_Button = (200, 515, 150, 70)
AddBg_Button = (375, 515, 200, 70)

Canvas_Outer = (170, 20, 610, 460)
Canvas_Inner = (175, 25, 600, 450)

Line1_Start = (150, 0)
Line1_End = (150, 600)
Line2_Start = (150, 500)
Line2_End = (800, 500)

Palette_Index = []
Palette_Top_Left = [6, 42]

for i in range(2):
    for j in range(8):
        Palette_Index.append([Palette_Top_Left[0], Palette_Top_Left[1]])
        Palette_Top_Left = [Palette_Top_Left[0], Palette_Top_Left[1] + 69]
    Palette_Top_Left = [80, 42]

# Text Indexes
Save = (Save_Button[0], Save_Button[1])
Clear = (Clear_Button[0], Clear_Button[1])
AddBG = (AddBg_Button[0], AddBg_Button[1])
Palette = (75, 20)


# Scale Images
def Scale():
    global pix, bg
    scaled_pic_0 = pygame.transform.scale(pix[0], (bit_size, bit_size))
    scaled_pic_1 = pygame.transform.scale(pix[1], (bit_size, bit_size))
    scaled_pic_2 = pygame.transform.scale(pix[2], (bit_size, bit_size))
    scaled_pic_3 = pygame.transform.scale(pix[3], (bit_size, bit_size))
    scaled_pic_4 = pygame.transform.scale(pix[4], (bit_size, bit_size))
    scaled_pic_5 = pygame.transform.scale(pix[5], (bit_size, bit_size))
    scaled_pic_6 = pygame.transform.scale(pix[6], (bit_size, bit_size))
    scaled_pic_7 = pygame.transform.scale(pix[7], (bit_size, bit_size))
    scaled_pic_8 = pygame.transform.scale(pix[8], (bit_size, bit_size))
    scaled_pic_9 = pygame.transform.scale(pix[9], (bit_size, bit_size))
    scaled_pic_10 = pygame.transform.scale(pix[10], (bit_size, bit_size))
    scaled_pic_11 = pygame.transform.scale(pix[11], (bit_size, bit_size))
    scaled_pic_12 = pygame.transform.scale(pix[12], (bit_size, bit_size))
    scaled_pic_13 = pygame.transform.scale(pix[13], (bit_size, bit_size))
    scaled_pic_14 = pygame.transform.scale(pix[14], (bit_size, bit_size))
    scaled_pic_15 = pygame.transform.scale(pix[15], (bit_size, bit_size))
    scaled_bg = pygame.transform.scale(pix[16], (bit_size * Map_size[1], bit_size * Map_size[0]))

    pix = [scaled_pic_0, scaled_pic_1, scaled_pic_2, scaled_pic_3, scaled_pic_4, scaled_pic_5, scaled_pic_6,
           scaled_pic_7, scaled_pic_8, scaled_pic_9, scaled_pic_10, scaled_pic_11, scaled_pic_12, scaled_pic_13,
           scaled_pic_14, scaled_pic_15, scaled_bg]


def set_bits(size):
    global bit_index, bit_size
    bit_index = []
    row_index = []
    bit_size = 64
    if size[1] > 8 or size[0] > 6:
        bit_size = min(450//size[0], 600//size[1])
    length = bit_size * size[0]
    width = bit_size * size[1]
    top_left_index = ((475 - width / 2), (250 - length / 2))
    for one in range(0, size[1]):
        for zero in range(0, size[0]):
            row_index.append((int(top_left_index[0] + one * bit_size), int(top_left_index[1] + zero * bit_size)))
        bit_index.append(row_index)
        row_index = []

    return [bit_index, bit_size]


# Map Creator
def createNewMap(size):
    global new_map, bit_index, bit_size
    new_map = np.zeros(size)
    bit_index, bit_size = set_bits(size)[0], set_bits(size)[1]

    return [new_map, bit_index, bit_size]


# Load Map
def Load_map():
    global new_map, Map_size, bit_size, bit_index
    with open("storage.txt", 'r') as Read:
        File_name = Read.read()
    new_map = validMapFormat.repairMap(File_name)
    Map_size = (len(new_map), len(new_map[0]))
    bit_index, bit_size = set_bits(Map_size)[0], set_bits(Map_size)[1]

    return [new_map, bit_index, bit_size]


# Arrange Map
def showMap(my_map):
    if bg_mode == 1:
        WIN.blit(pix[-1], bit_index[0][0])
    rows = 0
    columns = 0
    for ith_row in my_map:
        for elem in ith_row:
            WIN.blit(pix[int(elem)], bit_index[columns][rows])
            columns += 1
        columns = 0
        rows += 1


def paint():
    if mouse_clicks[0]:
        for m in range(Map_size[1]):
            for n in range(Map_size[0]):
                if bit_index[m][n][0] < mouse_pos[0] < bit_index[m][n][0] + bit_size:
                    if bit_index[m][n][1] < mouse_pos[1] < bit_index[m][n][1] + bit_size:
                        new_map[n][m] = int(selected_paint)
                        spraying.play()


def choose_paint():
    global selected_paint
    if mouse_clicks[0]:
        for k in range(16):
            if Palette_Index[k][0] < mouse_pos[0] < Palette_Index[k][0] + 64:
                if Palette_Index[k][1] < mouse_pos[1] < Palette_Index[k][1] + 64:
                    selected_paint = str(k)
                    rattle.stop()
                    rattle.play()


# Draw Game Window
def redrawGameWindow():
    WIN.fill(black),

    pygame.draw.rect(WIN, light_light_grey, Save_Button)
    pygame.draw.rect(WIN, light_light_grey, AddBg_Button)
    pygame.draw.rect(WIN, light_light_grey, Clear_Button)
    pygame.draw.rect(WIN, light_grey, Canvas_Outer)
    pygame.draw.rect(WIN, light_light_grey, Canvas_Inner)

    pygame.draw.line(WIN, light_grey, Line1_Start, Line1_End, 3)
    pygame.draw.line(WIN, light_grey, Line2_Start, Line2_End, 3)

    for k in range(16):
        WIN.blit(Palette_images[k], Palette_Index[k])

    WIN.blit(frame, Palette_Index[int(selected_paint)])

    WIN.blit(text_save, (Save[0] - text_save.get_width() / 2 + 75, (Save[1] - text_save.get_height() / 2 + 35)))
    WIN.blit(text_clear, (Clear[0] - text_clear.get_width() / 2 + 75, (Clear[1] - text_clear.get_height() / 2 + 35)))
    WIN.blit(text_AddBG, (AddBG[0] - text_AddBG.get_width() / 2 + 100, (AddBG[1] - text_AddBG.get_height() / 2 + 35)))
    WIN.blit(text_palette, (Palette[0] - text_palette.get_width() / 2, (Palette[1] - text_palette.get_height() / 2)))

    showMap(new_map)

    pygame.display.update()


with open("size.txt", 'r') as read_size:
    sizes = read_size.read().split()
    Map_size = [int(sizes[0]), int(sizes[1])]

# Before The Loop
try:
    new_map = Load_map()[0]
    bit_index = Load_map()[1]
    bit_size = Load_map()[2]
except FileNotFoundError:
    print("Creating New Map!!")
    new_map = createNewMap(Map_size)[0]
    bit_index = createNewMap(Map_size)[1]
    bit_size = createNewMap(Map_size)[2]

Scale()

# Main Loop
run = True
while run:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Mouse and Keyboard
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicks = pygame.mouse.get_pressed(3)

    # Pressing
    if mouse_clicks[0]:
        if ((Clear_Button[0] < mouse_pos[0] < Clear_Button[0] + Clear_Button[2]) and
                (Clear_Button[1] < mouse_pos[1] < Clear_Button[1] + Clear_Button[3])):
            new_map = np.zeros(Map_size)
        elif ((Save_Button[0] < mouse_pos[0] < Save_Button[0] + Save_Button[2]) and
              (Save_Button[1] < mouse_pos[1] < Save_Button[1] + Save_Button[3])):
            import saveFile
            saveFile.root.mainloop()
            with open("storage.txt", 'r') as storage:
                file_name = storage.read()
            if file_name != "":
                with open(file_name, 'w'):
                    pass
                with open(file_name, 'a') as write:
                    for i in range(len(new_map)):
                        if i == len(new_map):
                            write.write(str(new_map[i]))
                        else:
                            write.write(str(new_map[i]) + "\n")
            break

        elif ((AddBg_Button[0] < mouse_pos[0] < AddBg_Button[0] + AddBg_Button[2]) and
              (AddBg_Button[1] < mouse_pos[1] < AddBg_Button[1] + AddBg_Button[3])):
            if bg_button_wait == 0:
                bg_button_wait = 1
                bg_mode = abs(bg_mode - 1)

    if not mouse_clicks[0]:
        bg_button_wait = 0

    redrawGameWindow()
    choose_paint()
    paint()

pygame.quit()
