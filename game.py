import pygame
import random
import math
from assets import bird_images, background_img
from utils.bird import Bird
from utils.block import Block

#defines some basic variables

WIDTH, HEIGHT = 1200, 700
BLOCK_WIDTH = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = (135, 206, 235)
gravity = 0.3

SLINGSHOT_OFFSET_X = 150
SLINGSHOT_BASE_Y = HEIGHT - 100
left_sling = (SLINGSHOT_OFFSET_X + 5, SLINGSHOT_BASE_Y - 100)
right_sling = (WIDTH - SLINGSHOT_OFFSET_X - 5, SLINGSHOT_BASE_Y - 100)

bird_types = ["red", "yellow", "blue", "black"]

font = pygame.font.SysFont("arial", 32)

#sets up the blocks

def setup_blocks(blocks):
    block_list = [random.choice(["wood", "ice", "stone"]) for _ in range(5)]
    for i in range(4, -1, -1):
        blocks.append(Block(WIDTH - 75 - BLOCK_WIDTH, HEIGHT - 170 - i * 65, block_list[i], owner=1))
    for i in range(4, -1, -1):
        blocks.append(Block(75, HEIGHT - 120 - i * 65, block_list[i], owner=0))

#draws a preditive launch arc

def draw_launch_arc(screen, start_pos, velocity):
    x, y = start_pos
    vx, vy = velocity
    points = []
    for t in range(0, 100):
        dt = t / 5.0
        px = x + vx * dt
        py = y + vy * dt + 0.5 * gravity * dt * dt
        points.append((int(px), int(py)))
    if len(points) > 1:
        pygame.draw.lines(screen, BLACK, False, points, 2)

#main function to run game

def run_game(screen, clock, players):
    current_player = 0
    birds = []
    blocks = []
    dragging = False
    current_drag_pos = (0, 0)
    bird_counts = [0, 0]
    winner = None

    setup_blocks(blocks)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            #if tab is closed
            if event.type == pygame.QUIT:
                return "quit"
            #while game is ongoing
            if winner is None:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragging = True
                    current_drag_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION and dragging:
                    current_drag_pos = pygame.mouse.get_pos()
                #launches bird
                if event.type == pygame.MOUSEBUTTONUP and dragging:
                    dragging = False
                    sling_point = left_sling if current_player == 0 else right_sling
                    dx = sling_point[0] - current_drag_pos[0]
                    dy = sling_point[1] - current_drag_pos[1]
                    strength = 0.13
                    max_speed = 20
                    vel_x = max(-max_speed, min(max_speed, dx * strength))
                    vel_y = max(-max_speed, min(max_speed, dy * strength))

                    bird = Bird(sling_point[0], sling_point[1], bird_types[bird_counts[current_player] % 4])
                    bird.vel_x = vel_x
                    bird.vel_y = vel_y
                    bird.launched = True
                    birds.append(bird)
                    bird_counts[current_player] += 1
                    current_player = (current_player + 1) % 2
                #to use bird special
                if event.type == pygame.KEYDOWN and birds:
                    special_birds = birds[-1].use_special(blocks)
                    birds.extend(special_birds)

        screen.blit(background_img, (0, 0))

        # Slingshots
        pygame.draw.line(screen, (150, 75, 0), (left_sling[0] - 5, left_sling[1] + 100), (left_sling[0] - 5, left_sling[1]), 10)
        pygame.draw.line(screen, (150, 75, 0), (right_sling[0] + 5, right_sling[1] + 100), (right_sling[0] + 5, right_sling[1]), 10)

        if dragging:
            sling_point = left_sling if current_player == 0 else right_sling
            pygame.draw.line(screen, BLACK, sling_point, current_drag_pos, 3)
            dx = sling_point[0] - current_drag_pos[0]
            dy = sling_point[1] - current_drag_pos[1]
            strength = 0.13
            vel_x = max(-20, min(20, dx * strength))
            vel_y = max(-20, min(20, dy * strength))
            draw_launch_arc(screen, sling_point, (vel_x, vel_y))

        for block in blocks:
            block.draw(screen)
        #checks colissions and damage
        for bird in birds:
            bird.update()
            bird.draw(screen)
            for block in blocks:
                if block.x < bird.x < block.x + block.width and block.y < bird.y < block.y + block.height and block.owner == current_player:
                    if block != bird.last_hit_block:
                        block.hit(bird)
                        bird.last_hit_block = block
                        if abs(bird.x - block.x) < bird.radius or abs(bird.x - (block.x + block.width)) < bird.radius:
                            scaling = -0.4 if not block.is_destroyed() else 0.4
                            bird.vel_x *= scaling
                        if abs(bird.y - block.y) < bird.radius or abs(bird.y - (block.y + block.height)) < bird.radius:
                            scaling = -0.4 if not block.is_destroyed() else 0.2
                            bird.vel_y *= scaling

        blocks[:] = [b for b in blocks if not b.is_destroyed()]
        birds[:] = [b for b in birds if b.x < WIDTH and b.y < HEIGHT]
        p0_blocks = [b for b in blocks if b.owner == 0]
        p1_blocks = [b for b in blocks if b.owner == 1]

        if not p0_blocks:
            winner = 1
        if not p1_blocks:
            winner = 0
        #displays winner
        if winner is not None:
            win_text = font.render(f"{players[winner]} Wins!", True, BLACK)
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))

        turn_text = font.render(f"{players[current_player]}'s Turn ({bird_types[bird_counts[current_player] % 4]})", True, BLACK)
        screen.blit(turn_text, (20, 20))

        pygame.display.update()
