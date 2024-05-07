import pygame
import random

pygame.init()

# infoObject = pygame.display.Info()
# SCREEN_WIDTH = infoObject.current_w
# SCREEN_HEIGHT = infoObject.current_h

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Range")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)
color_screen = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

target_img = pygame.image.load("img/target.png")
target_img = pygame.transform.scale(target_img, (50, 100))
target_x = random.randint(0, SCREEN_WIDTH - 50)
target_y = random.randint(0, SCREEN_HEIGHT - 100)

running = True
while running:
    pass

pygame.quit()
