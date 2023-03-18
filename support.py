import pygame

def draw_tile(tile_pos, tilesize, color):

    screen = pygame.display.get_surface()

    rect = pygame.Rect(tile_pos[0] * tilesize, tile_pos[1] * tilesize, tilesize, tilesize)
    pygame.draw.rect(screen, color, rect)

def debug_by_click(tilesize):
    m_keys = pygame.mouse.get_pressed()

    if m_keys[0]:
        pos = pygame.mouse.get_pos()[0] // tilesize, pygame.mouse.get_pos()[1] // tilesize
        print(pos)

def draw_text(screen, text, font, color, pos):
    text_img = font.render(f'{text}', True, color).convert_alpha()
    text_rect = text_img.get_rect(center=pos)
    screen.blit(text_img, text_rect)

