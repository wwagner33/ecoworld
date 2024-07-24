import pygame
import pygame_gui
from pygame_gui.elements.ui_image import UIImage
from pygame_gui.elements.ui_panel import UIPanel
from SimulatorThings.Gui import Gui 


class MapMakerGui(Gui):
    def __init__(self, screen, images) -> None:
        super().__init__(screen=screen)
        self.painel = UIPanel(relative_rect=pygame.Rect((0, 0),(200, 640)), manager=self.manager)
        self.tiles_images = images
        # self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
        #                                      text='Say Hello',
        #                                      manager=self.manager,
        #                                      container=self.painel)
        # self.imagem = pygame_gui.elements.ui_image.UIImage(relative_rect=pygame.Rect((10, 10),(55, 64)), 
        #                                                    image_surface=self.tiles_images[0], container=self.painel)
        self.tileset = []
        temp_x = 10
        temp_y = 10
        for i, tile in enumerate(self.tiles_images):
            temp_x = 10 + i * 60
            if temp_x > 140 : # TODO terminar isso aqui
                temp_y += 70
                temp_x = 10
              
            self.tileset.append(UIImage(relative_rect=pygame.Rect((temp_x, temp_y),
                                                                  (55, 64)), 
                                                                   image_surface=tile, container=self.painel))
            
            
            
            
            
        