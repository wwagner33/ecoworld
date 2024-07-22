import pygame
import pygame_gui
from pygame_gui.elements.ui_panel import UIPanel 


class Gui(object):
    """
    Classe responsavel por elementos gráficos para Usuário
    """
    
    def __init__(self, screen) -> None:
        self.screen = screen
        self.manager = pygame_gui.UIManager((970, 640), theme_path="themes.json")
        self.painel = UIPanel(relative_rect=pygame.Rect((0, 0),(200, 640)))
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=self.manager)
    
    def render(self, delta_time):
        self.manager.update(delta_time)
        self.manager.draw_ui(self.screen)
        self.manager.set_visual_debug_mode(True)


