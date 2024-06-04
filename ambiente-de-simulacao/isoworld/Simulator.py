import sys
import pygame
from pygame.locals import *
from ImageManager import ImageManager
from World import World
from Agent import Agent
from Config import Config


class Simulator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), DOUBLEBUF)
        pygame.display.set_caption('Mundo dos Agentes')
        self.clock = pygame.time.Clock()
        self.images = ImageManager()
        self.world = World()
        self.agents = []

    def run(self):
        self.load_all_images()
        self.display_welcome_message()
        self.init_world()
        self.main_loop()

    def load_all_images(self):
        self.images.load_images()
        if not self.images.tile_images:
            print("Error: Tile images are not loaded.")
        else:
            print("Tile images loaded successfully.")

    def display_welcome_message(self):
        print("Bem-vindo to Mundo dos Agentes!")
        print(f"Versão: {pygame.version.ver}")
        print(f"Resolução da Tela: {Config.SCREEN_WIDTH} x {Config.SCREEN_HEIGHT}")
        print(f"Dimensões do Mundo: {Config.WORLD_WIDTH} x {Config.WORLD_HEIGHT}")
        print("Pressione ESC para sair.")

    def init_world(self):
        if not self.images.tile_images:
            raise ValueError("Tile images must be loaded before initializing terrain.")
        self.world.load_images(self.images.tile_images, self.images.object_images, self.images.agent_images)
        self.world.initialize_terrain()
        self.world.initialize_objects()
        self.world.setup_environmental_factors()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.shutdown()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.shutdown()

            self.update_game_state()
            self.render_game()
            pygame.display.flip()
            self.clock.tick(Config.MAX_FPS)

    def update_game_state(self):
        self.world.update()
        for agent in self.agents:
            agent.update()

    def render_game(self):
        self.screen.fill((0, 0, 0))
        self.world.render(self.screen)
        for agent in self.agents:
            agent.render(self.screen)

    def shutdown(self):
        print("Shutting down...")
        pygame.quit()
        sys.exit()