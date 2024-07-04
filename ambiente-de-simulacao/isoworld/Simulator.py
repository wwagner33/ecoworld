import sys
import json
import pygame
from pygame.locals import *
from ImageManager import ImageManager
from World import World
from Agent import Agent
from Config import Config


class Simulator:
    def __init__(self, simulation_map:str=None):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), DOUBLEBUF)
        pygame.display.set_caption('Mundo dos Agentes')
        self.clock = pygame.time.Clock()
        self.images = ImageManager()
        self.agents = []
        self.world = self._load_world(simulation_map)


    def _load_world(self, path: str):

        # Pegar as inforações do mapa/ tamanho e dimensões, e quem sabe a visualização -> E atualiza as variaveis do Config.py
        # Coloca o mapa de alguma forma no World.py
        map = {
                'terrain': [],
                'height': []
            }
            
        with open(path) as json_file:
            x = json.loads(json_file.read())["world_dimensions"]
            Config.WORLD_WIDTH, Config.WORLD_HEIGHT = x["wid"], x["hei"]
            Config.VIEW_WIDTH, Config.VIEW_HEIGHT = x["view_wid"], x["view_hei"]
            
            
            with open(x['terrain_map']) as map_file:
                data = map_file.read().splitlines()

                for index, l in enumerate(data):
                    if index < Config.WORLD_WIDTH:
                        map["terrain"].append([int(x) for x in l.split(' ')])
                    elif index > Config.WORLD_WIDTH:
                        map["height"].append([int(x) for x in l.split(' ')])
         

        
        return World(map)


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
