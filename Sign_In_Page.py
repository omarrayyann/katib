import pygame
import InputBox

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = pygame.display.get_surface().get_size()

background = pygame.image.load("Background_Home_Page.png")

run = True

# Start Button
start_button_width = 592
start_button_height = 76
start_button_x = 503
start_button_y = 679
start_button_color = (255, 195, 0)
start_button_text_color = (0, 0, 0)
font = pygame.font.Font('Futura-Bold.otf', 36)
start_text = font.render("START", True, start_button_text_color)
text_rect = pygame.Rect(screen_width/2 - start_text.get_width()/2,
                        start_button_y+start_text.get_height()/2, 0, 0)
screen.blit(start_text, text_rect)
start_rect = pygame.Rect(start_button_x, start_button_y,
                         start_button_width, start_button_height)

# Username Field
username_field_width = 592
username_field_height = 76
username_field_x = 503
username_field_y = 424
username_field = InputBox.InputBox(
    username_field_x, username_field_y, username_field_width, username_field_height)

password_field_width = 592
password_field_height = 76
password_field_x = 503
password_field_y = 526
password_field = InputBox.InputBox(
    password_field_x, password_field_y, password_field_width, password_field_height)


def setup_screen():
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, start_button_color, start_rect,
                     0, int(start_button_height/2))
    pygame.draw.rect(screen, (0, 0, 0), start_rect,
                     2, int(start_button_height/2))
    username_field.draw(screen)
    password_field.draw(screen)
    screen.blit(start_text, text_rect)
    # placeholders
    if password_field.get_text() == "":
        font = pygame.font.Font('Futura-Medium.otf', 30)
        password_placeholder_text = font.render(
            "Password", True, (150, 150, 150))
        password_placeholder_text_rect = pygame.Rect(screen_width/2 - password_placeholder_text.get_width(
        )/2, password_field_y + password_placeholder_text.get_height()/2, 0, 0)
        screen.blit(password_placeholder_text, password_placeholder_text_rect)
    if username_field.get_text() == "":
        font = pygame.font.Font('Futura-Medium.otf', 30)
        username_placeholder_text = font.render(
            "Username", True, (150, 150, 150))
        username_placeholder_text_rect = pygame.Rect(screen_width/2 - username_placeholder_text.get_width(
        )/2, username_field_y + username_placeholder_text.get_height()/2, 0, 0)
        screen.blit(username_placeholder_text, username_placeholder_text_rect)


def clicked_start():
    print("clicked_start")


print(screen_height, screen_width)

while run:
    setup_screen()
    for e in pygame.event.get():
        username_field.handle_event(e)
        password_field.handle_event(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                run = False
        if e.type == pygame.MOUSEBUTTONDOWN and start_rect.collidepoint(e.pos):
            clicked_start()
        if start_rect.collidepoint(pygame.mouse.get_pos()):
            start_button_color = (0, 0, 0)
            start_button_text_color = (255, 195, 0)
            start_text = font.render("START", True, start_button_text_color)

        else:
            start_button_color = (255, 195, 0)
            start_button_text_color = (0, 0, 0)
            start_text = font.render("START", True, start_button_text_color)

    pygame.display.flip()
pygame.quit()
