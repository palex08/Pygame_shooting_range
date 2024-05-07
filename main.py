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
target_img = pygame.transform.scale(target_img, (120, 150))
target_x = random.randint(0, SCREEN_WIDTH - 120)
target_y = random.randint(0, SCREEN_HEIGHT - 150)

cursor_img = pygame.image.load("img/cursor.png")
pygame.mouse.set_visible(False)


running = True
while running:
    screen.fill(color_screen)
    screen.blit(target_img, (target_x, target_y))
    mouse_pos = pygame.mouse.get_pos()
    cursor_pos = (mouse_pos[0] - cursor_img.get_width() / 2, mouse_pos[1] - cursor_img.get_height() / 2)
    screen.blit(cursor_img, cursor_pos)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if target_x + 33 < event.pos[0] < target_x + 87 and target_y + 45 < event.pos[1] < target_y + 115:
                target_x = random.randint(0, SCREEN_WIDTH - 120)
                target_y = random.randint(0, SCREEN_HEIGHT - 150)
            elif target_x + 50 < event.pos[0] < target_x + 73 and target_y + 5 < event.pos[1] < target_y + 37:
                target_x = random.randint(0, SCREEN_WIDTH - 120)
                target_y = random.randint(0, SCREEN_HEIGHT - 150)
pygame.quit()
