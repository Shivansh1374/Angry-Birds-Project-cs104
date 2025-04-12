import pygame

# Initialize Pygame
pygame.init()

# Screen size and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Game")

# Game clock
clock = pygame.time.Clock()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image=pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

all_sprites = pygame.sprite.Group()

obstacle=Obstacle(100, 200, "images/wood.webp")
all_sprites.add(obstacle)

# Function to run the game (You can later add your game logic here)
def start_game(player1, player2):
    running = True
    while running:
        screen.fill(WHITE)
        
        
        all_sprites.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    from menu import main_menu
    player1, player2 = main_menu()  # Get player names from menu
    start_game(player1, player2)    # Start the actual game
