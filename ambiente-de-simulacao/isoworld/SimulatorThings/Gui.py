import pygame
import pygame_gui
import pygame_gui.elements.ui_image
from pygame_gui.elements.ui_panel import UIPanel 


class Gui(object):
    """
    Classe responsavel por elementos gráficos para Usuário
    """
    
    def __init__(self, screen) -> None:
        self.screen = screen
        self.manager = pygame_gui.UIManager((970, 640), theme_path="themes.json") # Números mágicos
        
        
    
    def render(self, delta_time):
        self.manager.update(delta_time)
        self.manager.draw_ui(self.screen)
        self.manager.set_visual_debug_mode(False)


