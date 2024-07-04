import random
from Agent import Agent
from Config import Config

class World:
    def __init__(self, map=None):
        self.map = map # Colocar as deais condições para a simulação?
        self.terrain_map = [[0] * Config.WORLD_WIDTH for _ in range(Config.WORLD_HEIGHT)] # Legal
        self.height_map = map["height"] or [[0] * Config.WORLD_WIDTH for _ in range(Config.WORLD_HEIGHT)]
        self.object_map = [[[0] * Config.WORLD_WIDTH for _ in range(Config.WORLD_HEIGHT)] for _ in range(Config.OBJECT_MAP_LEVELS)]
        self.agent_map = [[None] * Config.WORLD_WIDTH for _ in range(Config.WORLD_HEIGHT)]

    
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
    

    def update(self): 
        # Regular update method to handle game logic
        self.current_cycle += 1
        if self.current_cycle % self.update_weather_every_n_cycles == 0:
            self.change_weather()


    def render(self, screen):
        for y in range(Config.VIEW_HEIGHT):
            for x in range(Config.VIEW_WIDTH):
                tile_index = self.terrain_map[y][x]
                tile_image = self.tile_images[tile_index]

                x_offset = 450 # Provavelmente devá ser passado para outro lugar
                y_offset = 100
                xScreen = x_offset + x * tile_image.get_width() / 2 - y * tile_image.get_width() / 2
                yScreen = y_offset + y * tile_image.get_height() / 4 + x * tile_image.get_height() / 4

                # if x == 3 :
                #     yScreen -= 15

                screen.blit(tile_image, (xScreen ,yScreen - (tile_image.get_height() / 2)* (self.height_map[y][x])))

                for level in range(Config.OBJECT_MAP_LEVELS):
                    obj_index = self.object_map[level][y][x]
                    if obj_index > 0:
                        obj_image = self.object_images[obj_index]

                        xScreen = x_offset + x * obj_image.get_width() / 2 - y * obj_image.get_width() / 2
                        yScreen = y_offset + y * obj_image.get_height() / 4 + x * obj_image.get_height() / 4
                        screen.blit(obj_image, (xScreen, yScreen - (obj_image.get_height() / 2)* (level+1)))

                agent = self.agent_map[y][x]
                if agent:
                    screen.blit(agent.image, (agent.x * agent.image.get_width(), agent.y * agent.image.get_height()))


    def load_images(self, tile_images, object_images, agent_images):
        self.tile_images = tile_images
        self.object_images = object_images
        self.agent_images = agent_images


    def initialize_agents(self):
        # Example: Place agents at strategic locations or random positions
        starting_positions = [(10, 10), (20, 20), (30, 30)]  # Preset or generated positions
        for pos in starting_positions:
            agent = Agent(pos[0], pos[1], self.get_random_agent_image())
            self.agent_map[pos[1]][pos[0]] = agent  # Assuming self.agent_map stores agent references


    def setup_environmental_factors(self):
        # Example: Initialize weather, lighting, or other environmental factors
        self.weather = "Sunny"  # Default weather
        self.update_weather_every_n_cycles = 100  # Change weather every 100 cycles
        self.current_cycle = 0


    def get_random_agent_image(self):
        # Example: Return a random image from loaded agent images
        import random
        return random.choice(self.agent_images)


    def change_weather(self):
        # Example method to change weather conditions randomly
        import random
        weather_conditions = ["Sunny", "Rainy", "Cloudy", "Stormy"]
        self.weather = random.choice(weather_conditions)
        print(f"Weather changed to: {self.weather}")    