from support import *
from random import random, randint, seed
from collections import deque

class BFS:
    def __init__(self, screen_resolution, tilesize, random_seed):

        seed(random_seed)

        # PYGAME SETUP
        pygame.init()
        pygame.display.set_caption('PathPlanning Algorithms')
        self.clock = pygame.time.Clock()

        self.tilesize = tilesize
        self.screen_resolution = screen_resolution

        self.screen = pygame.display.set_mode(self.screen_resolution)

        self.cols = self.screen.get_width() // self.tilesize  # x
        self.rows = self.screen.get_height() // self.tilesize  # y

        self.created_map = self.create_map(filling=0.2)
        self.obstacles = self.get_obstacles()

        self.start_pos, self.goal_pos = self.set_start_and_goal_positions()

        self.graph = self.create_graph()

        self.queue = deque([self.start_pos])
        self.visited = {self.start_pos: None}
        self.cur_node = self.start_pos

        self.path_segment = self.cur_node


    def create_map(self, filling):

        created_map = []

        for x in range(self.cols):
            row = []
            for y in range(self.rows):
                if random() < filling:
                    row.append(1)
                else:
                    row.append(0)

            created_map.append(row)

        return created_map

    def get_obstacles(self):

        obstacles = []

        for x in range(self.cols):
            for y in range(self.rows):
                if self.created_map[x][y] == 1:
                    obstacles.append((x, y))

        return obstacles

    def set_start_and_goal_positions(self):

        self.start_pos = (randint(0, self.cols - 1), randint(0, self.rows - 1))
        self.goal_pos = (randint(0, self.cols - 1), randint(0, self.rows - 1))

        while self.start_pos in self.obstacles:
            self.start_pos = (randint(0, self.cols - 1), randint(0, self.rows - 1))

        while self.goal_pos in self.obstacles:
            self.goal_pos = (randint(0, self.cols - 1), randint(0, self.rows - 1))

        return self.start_pos, self.goal_pos

    def get_neighboring_nodes(self, pos):

        neighboring_nodes = []

        # right, left, up, down
        ways = [1, 0], [-1, 0], [0, -1], [0, 1]

        for motion in ways:

            node_x = pos[0] + motion[0]
            node_y = pos[1] + motion[1]
            node_pos = (node_x, node_y)

            if 0 <= node_x < self.cols and 0 <= node_y < self.rows and node_pos not in self.obstacles:
                neighboring_nodes.append(node_pos)

        return neighboring_nodes

    def bfs(self):

        if self.cur_node != self.goal_pos:
            if self.queue:
                self.cur_node = self.queue.popleft()
                next_nodes = self.graph[self.cur_node]
                for next_node in next_nodes:
                    if next_node not in self.visited:
                        self.queue.append(next_node)
                        self.visited[next_node] = self.cur_node

    def create_graph(self):

        graph = {}

        for x in range(self.cols):
            for y in range(self.rows):
                pos = (x, y)
                if pos not in self.obstacles:
                    graph[pos] = self.get_neighboring_nodes(pos)

        return graph

    def draw_background(self):

        self.screen.fill('gray')

        for x in range(self.cols):
            if x % 2 == 0:
                for y in range(0, self.rows, 2):
                    draw_tile((x, y), self.tilesize, 'light gray')
            else:
                for y in range(1, self.rows, 2):
                    draw_tile((x, y), self.tilesize, 'light gray')

    def draw_obstacles(self):

        for obstacle_pos in self.obstacles:
            draw_tile(obstacle_pos, self.tilesize, 'blue')

    def draw_start_anf_goal_posititons(self):

        draw_tile(self.start_pos, self.tilesize, 'red')
        draw_tile(self.goal_pos, self.tilesize, 'green')

    def draw_bfs(self):

        for x, y in self.visited:
            pos = (x, y)
            draw_tile(pos, self.tilesize, 'forestgreen')

        for x, y in self.queue:
            pos = (x, y)
            draw_tile(pos, self.tilesize, 'darkslategray')

    def get_and_draw_path_to_current_node(self):

        self.path_segment = self.cur_node
        while not self.path_segment is None:
            draw_tile(self.path_segment, self.tilesize, 'orange')
            self.path_segment = self.visited[self.path_segment]

    def run(self):

        self.draw_background()
        self.draw_obstacles()
        self.draw_bfs()
        self.get_and_draw_path_to_current_node()
        self.draw_start_anf_goal_posititons()

        debug_by_click(self.tilesize)

        self.bfs()
