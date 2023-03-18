# Importing frameworks
import pygame

# Initialization of pygame tools
pygame.init()

# Define fonts
menu_font = pygame.font.Font('Content/PublicPixel.ttf', 128)
button_font = pygame.font.Font('Content/PublicPixel.ttf', 30)


class Button:
    def __init__(self, pos, size, name):

        self.name = name
        self.size = size

        self.button_hitbox = pygame.Rect(pos, size)

        self.click = False
        self.clack = False

        self.simple_button_texture = f"Content/Simple_button.png"
        self.pressed_button_texture = f"Content/Pressed_button.png"

        self.screen = pygame.display.get_surface()

        self.h_text = button_font.render(f'{self.name}', True, 'yellow')
        self.s_text = button_font.render(f'{self.name}', True, 'black')

        self.x = self.button_hitbox.x + ((self.button_hitbox.w - self.h_text.get_rect().w) // 2)
        self.y = self.button_hitbox.y + ((self.button_hitbox.h - self.h_text.get_rect().h) // 2)


    def clicked(self):

        action = False
        state = 'simple'

        cursor_pos = pygame.mouse.get_pos()
        mouse_key = pygame.mouse.get_pressed()

        if self.button_hitbox.collidepoint(cursor_pos):
            state = 'highlighted'

            # Click-clack effect
            if mouse_key[0]:
                state = 'clicked'
                if not self.click:
                    self.click = True

            if self.click and not mouse_key[0]:
                self.clack = True
            if self.click and self.clack:
                action = True
                self.click = False
                self.clack = False
        else:
            if not mouse_key[0]:
                self.click = False
                state = 'simple'


        if state == 'highlighted':
            button = pygame.image.load(self.simple_button_texture)
            self.screen.blit(button, (self.button_hitbox.x, self.button_hitbox.y))
            self.screen.blit(self.h_text, (self.x, self.y))
        elif state == 'clicked':
            button = pygame.image.load(self.pressed_button_texture)
            self.screen.blit(button, (self.button_hitbox.x, self.button_hitbox.y))
            self.screen.blit(self.h_text, (self.x, self.y + 4))
        else:
            button = pygame.image.load(self.simple_button_texture)
            self.screen.blit(button, (self.button_hitbox.x, self.button_hitbox.y))
            self.screen.blit(self.s_text, (self.x, self.y))

        return action