import pygame
import os

# Make sure this points to your asset folder
ASSET_FOLDER = "assets"

bird_images = {}
color_map = {
    "red": "red_bird.png",
    "yellow": "yellow_bird.png",
    "blue": "blue_bird.png",
    "black": "black_bird.png"
}

for color, filename in color_map.items():
    path = os.path.join(ASSET_FOLDER, filename)
    bird_images[color] = pygame.image.load(path).convert_alpha()

background_img = pygame.image.load(os.path.join(ASSET_FOLDER, "background.png")).convert()