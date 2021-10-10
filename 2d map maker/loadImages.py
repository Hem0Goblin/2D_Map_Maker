# Imports
import pygame
from tkinter import messagebox


# Image Load Function
def loadImages():
    try:
        empty = pygame.image.load("empty.png")
    except FileNotFoundError:
        messagebox.showerror("Missing Images", "'empty.png' image file must exist")
        return False

    try:
        pic_0 = pygame.image.load("0.png")
    except FileNotFoundError:
        pic_0 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'0.png' image file must exist")

    try:
        pic_1 = pygame.image.load("1.png")
    except FileNotFoundError:
        pic_1 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'1.png' image file must exist")

    try:
        pic_2 = pygame.image.load("2.png")
    except FileNotFoundError:
        pic_2 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'2.png' image file must exist")

    try:
        pic_3 = pygame.image.load("3.png")
    except FileNotFoundError:
        pic_3 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'3.png' image file must exist")

    try:
        pic_4 = pygame.image.load("4.png")
    except FileNotFoundError:
        pic_4 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'4.png' image file must exist")

    try:
        pic_5 = pygame.image.load("5.png")
    except FileNotFoundError:
        pic_5 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'5.png' image file must exist")

    try:
        pic_6 = pygame.image.load("6.png")
    except FileNotFoundError:
        pic_6 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'6.png' image file must exist")

    try:
        pic_7 = pygame.image.load("7.png")
    except FileNotFoundError:
        pic_7 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'7.png' image file must exist")

    try:
        pic_8 = pygame.image.load("8.png")
    except FileNotFoundError:
        pic_8 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'8.png' image file must exist")

    try:
        pic_9 = pygame.image.load("9.png")
    except FileNotFoundError:
        pic_9 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'9.png' image file must exist")

    try:
        pic_10 = pygame.image.load("10.png")
    except FileNotFoundError:
        pic_10 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'10.png' image file must exist")

    try:
        pic_11 = pygame.image.load("11.png")
    except FileNotFoundError:
        pic_11 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'11.png' image file must exist")

    try:
        pic_12 = pygame.image.load("12.png")
    except FileNotFoundError:
        pic_12 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'12.png' image file must exist")

    try:
        pic_13 = pygame.image.load("13.png")
    except FileNotFoundError:
        pic_13 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'13.png' image file must exist")

    try:
        pic_14 = pygame.image.load("14.png")
    except FileNotFoundError:
        pic_14 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'14.png' image file must exist")

    try:
        pic_15 = pygame.image.load("15.png")
    except FileNotFoundError:
        pic_15 = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'15.png' image file must exist")

    try:
        bg = pygame.image.load("bg.png")
    except FileNotFoundError:
        bg = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'bg.png' image file must exist")

    try:
        frame = pygame.image.load("frame.png")
    except FileNotFoundError:
        frame = pygame.image.load("empty.png")
        messagebox.showerror("Missing Images", "'frame.png' image file must exist")

    pic_0 = pygame.transform.scale(pic_0, (64, 64))
    pic_1 = pygame.transform.scale(pic_1, (64, 64))
    pic_2 = pygame.transform.scale(pic_2, (64, 64))
    pic_3 = pygame.transform.scale(pic_3, (64, 64))
    pic_4 = pygame.transform.scale(pic_4, (64, 64))
    pic_5 = pygame.transform.scale(pic_5, (64, 64))
    pic_6 = pygame.transform.scale(pic_6, (64, 64))
    pic_7 = pygame.transform.scale(pic_7, (64, 64))
    pic_8 = pygame.transform.scale(pic_8, (64, 64))
    pic_9 = pygame.transform.scale(pic_9, (64, 64))
    pic_10 = pygame.transform.scale(pic_10, (64, 64))
    pic_11 = pygame.transform.scale(pic_11, (64, 64))
    pic_12 = pygame.transform.scale(pic_12, (64, 64))
    pic_13 = pygame.transform.scale(pic_13, (64, 64))
    pic_14 = pygame.transform.scale(pic_14, (64, 64))
    pic_15 = pygame.transform.scale(pic_15, (64, 64))

    Palette_images = [pic_0, pic_1, pic_2, pic_3, pic_4, pic_5, pic_6, pic_7,
                      pic_8, pic_9, pic_10, pic_11, pic_12, pic_13, pic_14, pic_15]
    pix = [pic_0, pic_1, pic_2, pic_3, pic_4, pic_5, pic_6, pic_7,
           pic_8, pic_9, pic_10, pic_11, pic_12, pic_13, pic_14, pic_15, bg]
    other = [empty, bg, frame]

    return [Palette_images, pix, other]
