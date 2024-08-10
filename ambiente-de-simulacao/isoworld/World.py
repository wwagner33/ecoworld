import random

import pygame
from Agent import Agent
from Config import Config


"""Ficará Responsavel por 'Redenrizar' os elementos"""
class World:
    def __init__(self, map=None, player_agent: Agent=None):
        self.map = map # Colocar as deais condições para a simulação?
        self.terrain_map = [[0] * Config.WORLD_WIDTH for _ in range(Config.WORLD_HEIGHT)] # Legal
        self.height_map = map["height"] or [[0] * Config.WORLD_WIDTH for _ in range(Config.WORLD_HEIGHT)]
        self.object_map = [[[0] * Config.WORLD_WIDTH for _ in range(Config.WORLD_HEIGHT)] for _ in range(Config.OBJECT_MAP_LEVELS)]
        self.agent_map = [[None] * Config.WORLD_WIDTH for _ in range(Config.WORLD_HEIGHT)]
        self.player = player_agent
        # TODO Depois Colocar em um lugar melhor
        self.x_offset = 450
        self.y_offset = 200
        self.tile_wid = None
        self.tile_hei = None

    
    def initialize_world(self):
        self.initialize_terrain()
        self.initialize_objects()
        self.initialize_agents()
        self.setup_environmental_factors()


    def initialize_terrain(self):
        if not self.tile_images:
            print("Warning: No tile images available for terrain initialization.")
            return
        for y in range(Config.WORLD_HEIGHT):
            for x in range(Config.WORLD_WIDTH):
                self.terrain_map[y][x] = self.map['terrain'][y][x] or 0 #random.randint(0, len(self.tile_images) - 1)


    def initialize_objects(self):
        for y in range(0, Config.WORLD_HEIGHT, 5):
            for x in range(0, Config.WORLD_WIDTH, 5):
                level =  0 #random.randint(0, Config.OBJECT_MAP_LEVELS - 1)
                self.object_map[level][y][x] = random.randint(1, len(self.object_images) - 1)
    
    # TODO
    # def update(self): 
    #     # Regular update method to handle game logic
    #     self.current_cycle += 1
    #     if self.current_cycle % self.update_weather_every_n_cycles == 0:
    #         self.change_weather()


    """Função que redencia as imagens dentro da tela{screen}"""
    def render(self, screen):
        self.tile_wid = self.tile_images[1].get_width()
        self.tile_hei = self.tile_images[1].get_height()

        for y in range(Config.VIEW_HEIGHT):
            for x in range(Config.VIEW_WIDTH):
                tile_index = self.terrain_map[y][x]
                if tile_index is None:
                    continue
                tile_image = self.tile_images[tile_index]
                xScreen, yScreen = self.__posicionar_na_grid(x,y,self.height_map[y][x])  # Subistituir esses xyScreen?

                # TODO Colocar em algum lugar a informação -> Para elevar algum elemento tudo que é necessário é diminuir seu valor de y

                screen.blit(tile_image, (xScreen ,yScreen))

                for level in range(Config.OBJECT_MAP_LEVELS):
                    obj_index = self.object_map[level][y][x]
                    if obj_index > 0:
                        obj_image = self.object_images[obj_index]

                        xScreen, yScreen = self.__posicionar_na_grid(x,y,level + 1)
                        screen.blit(obj_image, (xScreen, yScreen))


        # Lógica de redenrização do Player
        player_nivel = self.height_map[self.player.x][self.player.y] + 1
        player_x_Screen, player_y_Screen = self.__posicionar_na_grid(self.player.x,self.player.y,player_nivel)

        screen.blit(self.player.image, (player_x_Screen, player_y_Screen))
        pygame.draw.circle(screen, 255, self.__centraliza_tile((player_x_Screen, player_y_Screen), (self.tile_wid, self.tile_hei)) , 10,2)


    # TODO Substituir de lugar
    def __centraliza_tile(self, object_pos, tile_sizes ) -> tuple:
        x, y = object_pos
        w, h = tile_sizes
        return (x + w / 2, y + h / 2)
    

    def __posicionar_na_grid(self, x, y, height) -> tuple[tuple]:
        xScreen, yScreen = ((self.x_offset + x * self.tile_wid / 2 - y * self.tile_wid / 2), \
                             (self.y_offset + y * self.tile_hei / 4 + x * self.tile_hei / 4 - (self.tile_hei / 2) * (height + 1)))
        return (xScreen, yScreen)
    
    # FAzer um um novo modo que vai ser só pra editar, com grid plana, e numeros para a altura
    
    # def __
    # """ Pega o x e y  """    

    def load_images(self, tile_images, object_images, agent_images):
        self.tile_images = tile_images
        self.object_images = object_images
        self.agent_images = agent_images


    """inicializa os agentes no Mundo"""
    def initialize_agents(self):
        # Example: Place agents at strategic locations or random positions
        starting_positions = [(10, 10), (20, 20), (30, 30)]  # Preset or generated positions
        for pos in starting_positions:
            agent = Agent(pos[0], pos[1], self.get_random_agent_image())
            self.agent_map[pos[1]][pos[0]] = agent  # Assuming self.agent_map stores agent references


    #TODO
    def setup_environmental_factors(self):
        # Example: Initialize weather, lighting, or other environmental factors
        self.weather = "Sunny"  # Default weather
        self.update_weather_every_n_cycles = 100  # Change weather every 100 cycles
        self.current_cycle = 0


    def get_random_agent_image(self):
        # Example: Return a random image from loaded agent images
        import random
        return random.choice(self.agent_images)

    #TODO
    # def change_weather(self):
    #     # Example method to change weather conditions randomly
    #     import random
    #     weather_conditions = ["Sunny", "Rainy", "Cloudy", "Stormy"]
    #     self.weather = random.choice(weather_conditions)
    #     print(f"Weather changed to: {self.weather}")    