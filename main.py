import sys
from support import *
from button import Button
from bfs import BFS
from dijkstra import Dijkstra
from a_star import A_star

FPS = 30

class App:
    def __init__(self, screen_resolution, tilesize):

        # PYGAME SETUP
        pygame.init()
        pygame.display.set_caption('PathPlanning Algorithms')
        self.clock = pygame.time.Clock()

        self.tilesize = tilesize
        self.screen_resolution = screen_resolution

        self.screen = pygame.display.set_mode(self.screen_resolution)
        self.bg_img = pygame.image.load('Content/background.jpg').convert_alpha()

        # GUI Setup
        self.bfs_started = False
        self.dijkstra_strted = False
        self.a_star_started = False
        # GUI Buttons
        self.BFS_button = Button(pos=(350, 50), size=(300, 100), name='BFS')
        self.Dijkstra_button = Button(pos=(350, 250), size=(300, 100), name='Dijkstra')
        self.A_Star_button = Button(pos=(350, 450), size=(300, 100), name='A-Star')
        self.Exit_button = Button(pos=(350, 650), size=(300, 100), name='Exit')

        #Algorithms
        self.bfs_algorithm = BFS(screen_resolution=(1000, 800), tilesize=20, random_seed=100)
        self.dijkstra_algorithm = Dijkstra(screen_resolution=(1000, 800), tilesize=20, random_seed=100)
        self.a_star_algorithm = A_star(screen_resolution=(1000, 800), tilesize=20, random_seed=100)

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.blit(self.bg_img, (0, 0))

            if not (self.bfs_started and self.dijkstra_strted and self.a_star_started):
                if self.BFS_button.clicked():
                    self.bfs_started = True
                if self.Dijkstra_button.clicked():
                    self.dijkstra_strted = True
                if self.A_Star_button.clicked():
                    self.a_star_started = True
                if self.Exit_button.clicked():
                    pygame.quit()
                    sys.exit()

            if self.bfs_started:
                self.bfs_algorithm.run()
            elif self.dijkstra_strted:
                self.dijkstra_algorithm.run()
            elif self.a_star_started:
                self.a_star_algorithm.run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    app = App(screen_resolution=(1000, 800), tilesize=20)
    app.run()
