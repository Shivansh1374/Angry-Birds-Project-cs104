import math
from assets import bird_images

gravity = 0.3

class Bird:
    def __init__(self, x, y, bird_type):
        self.x = x
        self.y = y
        self.radius = 15
        self.type = bird_type
        self.vel_x = 0
        self.vel_y = 0
        self.launched = False
        self.special_used = False
        self.last_hit_block = None

    def draw(self, screen):
        img = bird_images[self.type]
        rect = img.get_rect(center=(int(self.x), int(self.y)))
        screen.blit(img, rect)

    def update(self):
        if self.launched:
            self.x += self.vel_x
            self.y += self.vel_y
            self.vel_y += gravity

    def use_special(self, blocks):
        split_birds = []
        if self.type == "blue" and not self.special_used:
            for offset in [-1, 0, 1]:
                new_bird = Bird(self.x + offset * 10, self.y, "blue")
                new_bird.vel_x = self.vel_x + offset * 2
                new_bird.vel_y = self.vel_y
                new_bird.launched = True
                new_bird.special_used = True
                split_birds.append(new_bird)
            self.special_used = True
            return split_birds
        elif self.type == "black" and not self.special_used:
            for block in blocks:
                dist = math.hypot(self.x - (block.x + block.width/2), self.y - (block.y + block.height/2))
                if dist < 100:
                    block.health -= 50
            self.special_used = True
        elif self.type == "yellow" and not self.special_used:
            self.vel_x *= 1.5
            self.special_used = True
        return []
