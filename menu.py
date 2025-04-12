import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def get_player_names():
    player1_name = ""
    player2_name = ""
    
    input_active1 = False
    input_active2 = False

    input_box1 = pygame.Rect(250, 200, 300, 50)
    input_box2 = pygame.Rect(250, 300, 300, 50)
    
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color1 = color_inactive
    color2 = color_inactive

    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        
        draw_text("Enter Player 1 Name:", font, BLACK, screen, 250, 170)
        draw_text("Enter Player 2 Name:", font, BLACK, screen, 250, 270)

        # Draw input boxes
        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)

        # Render the current text
        draw_text(player1_name, font, BLACK, screen, input_box1.x + 5, input_box1.y + 10)
        draw_text(player2_name, font, BLACK, screen, input_box2.x + 5, input_box2.y + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the click is inside input boxes
                if input_box1.collidepoint(event.pos):
                    input_active1 = True
                    input_active2 = False
                elif input_box2.collidepoint(event.pos):
                    input_active2 = True
                    input_active1 = False
                else:
                    input_active1 = False
                    input_active2 = False

            if event.type == pygame.KEYDOWN:
                if input_active1:
                    if event.key == pygame.K_BACKSPACE:
                        player1_name = player1_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        input_active1 = False
                    else:
                        player1_name += event.unicode

                elif input_active2:
                    if event.key == pygame.K_BACKSPACE:
                        player2_name = player2_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        input_active2 = False
                    else:
                        player2_name += event.unicode

                if event.key == pygame.K_TAB:
                    # Switch between input fields using Tab
                    input_active1, input_active2 = input_active2, input_active1

                if event.key == pygame.K_RETURN:
                    if player1_name.strip() != "" and player2_name.strip() != "":
                        return player1_name, player2_name

        pygame.display.update()
        clock.tick(30)

def main_menu():
    player1, player2 = get_player_names()
    print(f"Player 1: {player1}, Player 2: {player2}")
    return player1, player2

if __name__ == "__main__":
    main_menu()
