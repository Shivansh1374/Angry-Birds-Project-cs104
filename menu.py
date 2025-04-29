import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = (135, 206, 235)

font = pygame.font.SysFont("arial", 32)

def run_menu(screen, clock):
    input_rects = [pygame.Rect(600, 150, 300, 40), pygame.Rect(600, 250, 300, 40)]
    players = ["", ""]
    active_input = 0

    while True:
        clock.tick(60)
        screen.fill(BG_COLOR)
        title = font.render("Enter Player Names", True, BLACK)
        screen.blit(title, (600 - title.get_width() // 2, 50))

        for i in range(2):
            label = font.render(f"Player {i+1} Name:", True, BLACK)
            screen.blit(label, (400, 150 + i * 100))

            color = (255, 0, 0) if i == active_input else BLACK
            pygame.draw.rect(screen, color, input_rects[i], 2)

            name_surface = font.render(players[i], True, BLACK)
            screen.blit(name_surface, (input_rects[i].x + 10, input_rects[i].y + 5))

        if all(players):
            start_text = font.render("Press ENTER to Start", True, BLACK)
            screen.blit(start_text, (600 - start_text.get_width() // 2, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    active_input = (active_input + 1) % 2
                elif event.key == pygame.K_RETURN:
                    if all(players):
                        return players
                elif event.key == pygame.K_BACKSPACE:
                    players[active_input] = players[active_input][:-1]
                else:
                    players[active_input] += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(input_rects):
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        active_input = i

        pygame.display.update()
