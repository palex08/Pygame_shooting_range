import pygame
import random
import time

pygame.init()
pygame.mixer.init()
pygame.font.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
SCORE = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Range")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)
color_screen = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

target_img = pygame.image.load("img/target.png")
target_img = pygame.transform.scale(target_img, (120, 150))
target_x = random.randint(0, SCREEN_WIDTH - 120)
target_y = random.randint(100, SCREEN_HEIGHT - 150)

cursor_img = pygame.image.load("img/cursor.png")
pygame.mouse.set_visible(False)

sound_shot = pygame.mixer.Sound("sounds/shot.mp3")
sound_refill = pygame.mixer.Sound("sounds/refill.mp3")

font = pygame.font.Font(None, 36)
text_x = 600
text_y = 25


message_color = (255, 0, 0)
message_position = [120, 580]  # Стартовая позиция внизу экрана
message_active = False
message_timer = 0

running = True
while running:
    screen.fill(color_screen)
    screen.blit(target_img, (target_x, target_y))
    mouse_pos = pygame.mouse.get_pos()
    cursor_pos = (mouse_pos[0] - cursor_img.get_width() / 2, mouse_pos[1] - cursor_img.get_height() / 2)
    screen.blit(cursor_img, cursor_pos)
    score_text = font.render(f'Score: {SCORE}', True, (255, 255, 255))
    screen.blit(score_text, (text_x, text_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            sound_shot.play()
            time.sleep(0.3)
            sound_refill.play()

            if target_x + 33 < event.pos[0] < target_x + 87 and target_y + 45 < event.pos[1] < target_y + 115:
                target_x = random.randint(0, SCREEN_WIDTH - 120)
                target_y = random.randint(100, SCREEN_HEIGHT - 150)
                SCORE += 1
                message = "+ 1 point"
                message_active = True
                message_timer = 600
            elif target_x + 50 < event.pos[0] < target_x + 73 and target_y + 5 < event.pos[1] < target_y + 37:
                target_x = random.randint(0, SCREEN_WIDTH - 120)
                target_y = random.randint(100, SCREEN_HEIGHT - 150)
                SCORE += 2
                message = "Head shot + 2 points"
                message_active = True
                message_timer = 600



    if message_active:
        # Рендерим текст
        rendered_message = font.render(message, True, message_color)
        # Отображаем текст на экране
        screen.blit(rendered_message, message_position)
        # Обновляем позицию сообщения для эффекта вылета
        message_position[1] -= 0.2  # Поднимаем сообщение вверх
        # Обновляем таймер
        message_timer -= 0.5
        if message_timer <= 0:
            message_active = False
            message_position[1] = 580  # Возвращаем на исходную позицию


    pygame.display.update()
pygame.quit()
