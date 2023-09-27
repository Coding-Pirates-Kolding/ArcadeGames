import os
import pygame
#from graphics import blitz
#from graphics import brunaffald
#from graphics import eksplosion
#from graphics import miniscrap2
#from graphics import mimiscrap1
#from graphics import rumskib
#from graphics import rumskibmørkt
#from graphics import scrap1
#from graphics import scrap2
#from graphics import skraldebunke
#from graphics import skraldespand
#from graphics import stjernehimmel

pygame.init()
WINDOW_SIZE = (1280, 720)
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

font = pygame.font.SysFont(None, 48)
pygame.display.set_caption("Not Astroids")

# Ensure the file path is correct
background_image = pygame.image.load(os.path.join('graphics/stjernehimmel.png')).convert()
background_image = pygame.transform.scale(background_image, WINDOW_SIZE)

def create_button(position, size, color, text, text_color):
    button = pygame.Surface(size)
    button.fill(color)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=button.get_rect().center)
    button.blit(text_surf, text_rect)
    button_rect = button.get_rect(center=position)
    return button, button_rect

button_size = (200, 100)
button_y = screen.get_height() // 2 - button_size[1] // 2
button_positions = [
    (screen.get_width() // 4, button_y),
    (screen.get_width() * 3 // 4, button_y),
]
buttons = [
    {"id": 1, "color": (255, 255, 255), "text": "start", "text_color": (0, 0, 0)},
    {"id": 2, "color": (255, 0, 0), "text": "Exit", "text_color": (255, 255, 255)},
]
button_surfaces = []
for i, button in enumerate(buttons):
    button_surface, button_rect = create_button(button_positions[i], button_size, button["color"], button["text"], button["text_color"])
    button["rect"] = button_rect
    button_surfaces.append(button_surface)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button["rect"].collidepoint(event.pos) and button["id"] == 1:
                    # Define Player, astroids, and play function
                    # play(Player, astroids)
                    pass
                elif button["rect"].collidepoint(event.pos) and button["id"] == 2:
                    pygame.quit()
                    quit()

    screen.blit(background_image, (0, 0))  # Blit the background image
    for i, button_surface in enumerate(button_surfaces):
        screen.blit(button_surface, buttons[i]["rect"])
    pygame.display.update()