import sys
import json
import pygame
from pygame.locals import *
from ImageManager import ImageManager
from PlayerAgent import PlayerAgent
from SimulatorThings.Gui.simulation_gui import SimulationGui
from World import World
from Agent import Agent
from Config import Config

"""Classe responsável pelas mecânicas de cada simulação"""
class Simulator:
    def __init__(self, simulation_map:str=None):
        pygame.init()
        pygame.display.set_caption('Mundo dos Agentes')
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), DOUBLEBUF)
        self.images = ImageManager()
        self.clock = pygame.time.Clock()
        self.player = PlayerAgent(x=0, y=0, image=self.images.object_images[2])
        self.world = self._init_world(simulation_map, self.player)
        self.agents = [self.player]
        self.informations = {
                'Co2_level': 30.5, # talvez uma imagem para auxilar o entendimento
                'Oxigen_level': 50.5,
            }
        self.gui = SimulationGui(self.screen, self.informations)


    def _init_world(self, path: str, player:Agent=None):
        with open(path) as json_file:
            x = json.loads(json_file.read())["world_dimensions"]
            Config.WORLD_WIDTH, Config.WORLD_HEIGHT = x["wid"], x["hei"]
            Config.VIEW_WIDTH, Config.VIEW_HEIGHT = x["view_wid"], x["view_hei"]
            
        return self._load_world(x['terrain_map'], player)


    def _load_world(self, path: str, player:Agent=None):
        """Carrega o mundo (world) presente em um determinado caminho {path}-"""
        map = {
                'terrain': [],
                'height': []
            }
            
        with open(path) as map_file:
            map_json = json.loads(map_file.read())
            for line in map_json['map_texture']:
                map['terrain'].append(line)
            for line in map_json['map_relevo']:
                map['height'].append(line)

        return World(map, player)


    def run(self):
        self.load_all_images()
        self.display_welcome_message()
        self.init_world()
        self.main_loop()


    def load_all_images(self):
        """Carrega as imagens para o ambiente de simulação"""
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
        """Inicializa o mundo, carregando imagens, terreno, objetos e outras configurações do ambiente"""
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
                
                
                # pyg_gui
                # *Receptor de eventos do pygame_gui
                self.gui.send_event(event, self)
                self.gui.manager.process_events(event)


            # TODO self.update_game_state()
            self.render_game()
            delta_time =self.clock.tick(Config.MAX_FPS) / 1000.0
            self.gui.render(delta_time)
            pygame.display.flip()

    # TODO Implementar agentes dentro do ambiente
    # def update_game_state(self):
    #     self.world.update()
    #     for agent in self.agents:
    #         agent.update()


    def render_game(self):
        self.screen.fill((0, 0, 0))
        self.world.render(self.screen)
        # TODO Implementar agentes dentro do ambiente
        for agent in self.agents:
            ...
            # TODO Teste agent.render(self.screen)


    def shutdown(self):
        """Função responsável pelo desligamento seguro da aplicação"""
        print("Shutting down...")
        pygame.quit()
        sys.exit()
