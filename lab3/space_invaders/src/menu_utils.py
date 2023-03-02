import os

import pygame_menu
from pygame_menu import sound

mytheme = pygame_menu.themes.THEME_DARK.copy()

font = pygame_menu.font.FONT_MUNRO
myimage = pygame_menu.baseimage.BaseImage(
    image_path= os.path.realpath(os.path.dirname(__file__)) + '/../sprites/backgrounds/menu_bg2.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
color = (0,0,0)


mytheme.background_color = myimage
mytheme.widget_font = font
mytheme.widget_font_size = 50
mytheme.widget_font_color = color
mytheme.selection_color = color
mytheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE