import pygame
# import pygame_gui
from pygame_gui.elements.ui_panel import UIPanel
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIButton
from SimulatorThings.Gui.Gui import Gui 


class HeightPopUpGui(UIWindow):
    def __init__(self, screen, manager, x, y) -> None: # Refactore and remove bolcksize
        self.manager = manager
        self.painel = UIPanel(relative_rect=pygame.Rect((x , y ),(100, 50)), manager=manager)
        self.buttons = self.__init_buttons()


    

    def __init_buttons(self):
        buttons = []
        buttons.append(UIButton(relative_rect=pygame.Rect((10, 7), (35, 35)),
                                             text='+',
                                             container=self.painel,
                                             object_id=ObjectID(f'#Plus_height'),
                                             manager= self.manager
                                             ))
        buttons.append(UIButton(relative_rect=pygame.Rect((55, 7), (35, 35)),
                                             text='-',
                                             container=self.painel,
                                             object_id=ObjectID(f'#Minus_height'),
                                             manager= self.manager
                                             ))
        return buttons
    

    