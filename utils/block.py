import pygame

BLOCK_WIDTH = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WOOD_COLOR = (139, 69, 19)
ICE_COLOR = (173, 216, 230)
STONE_COLOR = (128, 128, 128)

class Block:
    def __init__(self, x, y, block_type, owner):
        self.x = x
        self.y = y
        self.width = BLOCK_WIDTH
        self.height = 60
        self.type = block_type
        self.color = {"wood": WOOD_COLOR, "ice": ICE_COLOR, "stone": STONE_COLOR}[block_type]
        self.health = 100
        self.owner = owner

    def draw(self, screen):
        block_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, block_rect)
        pygame.draw.rect(screen, BLACK, block_rect, 2)
        health_width = self.width * max(0, self.health / 100)
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 10, health_width, 5))

    def hit(self, bird):
        damage = 30
        if bird.type == "red":
            damage = 50
        if bird.type == "yellow" and self.type == "wood":
            damage = 70
        if bird.type == "blue" and self.type == "ice":
            damage = 70
        if bird.type == "black" and self.type == "stone":
            damage = 70
        self.health -= damage

    def is_destroyed(self):
        return self.health <= 0
