#text adventure
import pygame
import sys

pygame.init()

screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text Adventure")

White = (255, 255, 255)
Blue = (0, 150, 255)

def get_font(size):
    return pygame.font.Font(None, size)

player_actions = "Status"
player_status_text = ["enemy's killed: ", "Capturers: ", "Lost: ", "Raids: "]
player_current_health = 100
gold = 0

#player current History
def player_status(screen, font, player_input, start_x, start_y):
    if player_input == "Status":
        status_text = [
            f"Player Health: {player_current_health}",
            f"gold: {gold}",
            "Status"
        ] + player_status_text
        render_multiline_text(screen, font, status_text, start_x, start_y)

#player actions
def render_multiline_text(screen, font, text_list, start_x, start_y):
    y_offset = start_y
    for line in text_list:
        text = font.render(line, True, White)
        screen.blit(text, (start_x, y_offset))
        y_offset += 40
        
    

def load_and_resize_image():
    image_path = "save_picture/sample_235442c08e932d0a60d2ebd5ef5cfce4.jpg"
    image = pygame.image.load(image_path)
    image_resize = pygame.transform.scale(image, (screen_width, screen_height))
    return image_resize

resize_image = load_and_resize_image()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            resize_image = pygame.transform.scale(resize_image, (screen_width, screen_height))
            
    dynamic_font_size = max(24, screen_height // 20)
    font = get_font(dynamic_font_size)
            
    screen.fill(Blue)
    
    screen.blit(resize_image, (0, 0))
    
    player_status(screen, font,  player_actions, 50, 50)
    
    pygame.display.flip()
    

pygame.quit()
sys.exit()
