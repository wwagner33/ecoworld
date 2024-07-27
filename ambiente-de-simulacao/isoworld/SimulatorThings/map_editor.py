import sys
import json
import pygame as py
import pygame_gui
from pygame.locals import *
from ImageManager import ImageManager
from PlayerAgent import PlayerAgent
from SimulatorThings.Gui import Gui
from SimulatorThings.map_maker_gui import MapMakerGui
from World import World
from Agent import Agent
from Config import Config

class MapMaker:

    def __init__(self, map=None) -> None:
        """ Inicializa o Editor """
        py.init()
        self.screen = py.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), DOUBLEBUF)
        self.images = ImageManager()
        py.display.set_caption('Criador de mapas interface')
        self.clock = py.time.Clock()
        self.map = map
        self.gui = MapMakerGui(self.screen, self.images.tile_images)
    

    def _load_map(self):
        ...


    def run(self):
        self.load_all_images()

        self.main_loop()    
    

    def render_editor(self):
        self.screen.fill((0, 0, 0))
        self.drawGrid()
    

    def drawGrid(self):
        blockSize = int(60 * Config.SCALE_MULTIPLIER)  #Set the size of the grid block
        for x in range(0, Config.SCREEN_WIDTH, blockSize):
            for y in range(0, Config.SCREEN_HEIGHT, blockSize):
                rect = py.Rect(x, y, blockSize, blockSize)
                py.draw.rect(self.screen, (py.Color(100, 100, 100, a=20)), rect, 1)
        

    def load_all_images(self):
        self.images.load_images()
        if not self.images.tile_images:
            print("Error: Tile images are not loaded.")
        else:
            print("Tile images loaded successfully.")
    

    def main_loop(self):
        while True:
            for event in py.event.get():
                if event.type == QUIT:
                    self.shutdown()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.shutdown()
                    elif event.key == py.K_w:
                        self.player.move(0,-1)
                    elif event.key == py.K_s:
                        self.player.move(0,1)
                    elif event.key == py.K_a:
                        self.player.move(-1,0)
                    elif event.key == py.K_d:
                        self.player.move(1,0)
                
                
                # Gui parte por enquanto
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if 'mouse_changer' in event.ui_object_id :
                        self.gui.send_event(event)
                        
                        
                        
                self.gui.manager.process_events(event)


            # self.update_game_state()
            self.render_editor()
            delta_time =self.clock.tick(Config.MAX_FPS) / 1000.0
            self.gui.render(delta_time)
            py.display.flip()

    
    def shutdown(self):
        print("Shutting down...")
        py.quit()
        sys.exit()
        