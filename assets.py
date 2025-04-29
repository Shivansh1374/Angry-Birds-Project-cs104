import pygame
import os
pygame.init()
# Make sure this points to your asset folder

bird_images = {}
color_map = {
    "red": "red_bird.png",
    "yellow": "yellow_bird.png",
    "blue": "blue_bird.png",
    "black": "black_bird.png"
}
background_img = pygame.image.load("assets/background.png")
for color, filename in color_map.items():
    path="assets/"+filename
    bird_images[color] = pygame.image.load(path).convert_alpha()

