import pygame
import pygame_gui
import pygame_gui.elements.ui_image
from pygame_gui.elements.ui_panel import UIPanel 


class Gui(object):
    """
    Classe responsavel por elementos gráficos para Usuário
    """
    
    def __init__(self, screen, images) -> None:
        self.screen = screen
        self.manager = pygame_gui.UIManager((970, 640), theme_path="themes.json")
        self.painel = UIPanel(relative_rect=pygame.Rect((0, 0),(200, 640)), manager=self.manager)
        
        self.imagens = images
        # self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
        #                                      text='Say Hello',
        #                                      manager=self.manager,
        #                                      container=self.painel)
        self.imagem = pygame_gui.elements.ui_image.UIImage(relative_rect=pygame.Rect((10, 10),(55, 64)), image_surface=self.imagens[0], container=self.painel)
        
    
    def render(self, delta_time):
        self.manager.update(delta_time)
        self.manager.draw_ui(self.screen)
        self.manager.set_visual_debug_mode(True)


