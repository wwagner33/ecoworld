import sys
import json
import pygame
import pygame_gui
from pygame.locals import *
from ImageManager import ImageManager
from PlayerAgent import PlayerAgent
# from SimulatorThings.Gui.Gui import Gui
from SimulatorThings.Gui.map_maker_gui import MapMakerGui
from World import World
from Agent import Agent
from Config import Config

"""Classe responsável pelas mecânicas de cada simulação"""
class Simulator:
    def __init__(self, simulation_map:str=None):
        pygame.init()

        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), DOUBLEBUF)
        pygame.display.set_caption('Mundo dos Agentes')
        self.images = ImageManager()
        self.clock = pygame.time.Clock()
        self.gui = MapMakerGui(self.screen, self.images.tile_images)
        self.player = PlayerAgent(x=0, y=0, image=self.images.object_images[2])
        self.world = self._load_world(simulation_map, self.player)
        self.agents = [self.player]


    def _load_world(self, path: str, player:Agent):

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
            
            # * Trocar arquivo de texto para json List []
            with open(x['terrain_map']) as map_file:

                map_json = json.loads(map_file.read())

                for line in map_json['map_texture']:
                    # print(line)
                    map['terrain'].append(line)

                for line in map_json['map_relevo']:
                    # print(line)
                    map['height'].append(line)



        return World(map, player)


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
                    elif event.key == pygame.K_w:
                        self.player.move(0,-1)
                    elif event.key == pygame.K_s:
                        self.player.move(0,1)
                    elif event.key == pygame.K_a:
                        self.player.move(-1,0)
                    elif event.key == pygame.K_d:
                        self.player.move(1,0)
                
                
                # Gui parte por enquanto
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if 'mouse_changer' in event.ui_object_id :
                        self.gui.send_event(event)
                        
                        
                        
                self.gui.manager.process_events(event)


            # TODO self.update_game_state()
            self.render_game()
            delta_time =self.clock.tick(Config.MAX_FPS) / 1000.0
            self.gui.render(delta_time)
            pygame.display.flip()

    # TODO
    # def update_game_state(self):
    #     self.world.update()
    #     for agent in self.agents:
    #         agent.update()


    def render_game(self):
        self.screen.fill((0, 0, 0))
        self.world.render(self.screen)
        for agent in self.agents:
            ...
            # TODO Teste agent.render(self.screen)


    def shutdown(self):
        print("Shutting down...")
        pygame.quit()
        sys.exit()
