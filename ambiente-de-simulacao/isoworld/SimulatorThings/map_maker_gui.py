import pygame
import pygame_gui
from pygame_gui.elements.ui_image import UIImage
from pygame_gui.elements.ui_panel import UIPanel
from pygame_gui.core import ObjectID

from pygame_gui.elements import UIButton
from SimulatorThings.Gui import Gui 


class MapMakerGui(Gui):
    def __init__(self, screen, images) -> None:
        super().__init__(screen=screen)
        self.painel = UIPanel(relative_rect=pygame.Rect((0, 0),(200, 640)), manager=self.manager)
        self.tiles_images = images
        self.mouse_editing = False
        self.mouse_image = None
        # self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
        #                                      text='Say Hello',
        #                                      manager=self.manager,
        #                                      container=self.painel,
        #                                      object_id=ObjectID(class_id='@painel')
        #                                      )
        # self.imagem = pygame_gui.elements.ui_image.UIImage(relative_rect=pygame.Rect((10, 10),(55, 64)), 
        #                                                    image_surface=self.tiles_images[0], container=self.painel)
        self.tileset = []
        temp_x = 10
        temp_y = 10
        for i, tile in enumerate(self.tiles_images):
            temp_x = 10 + i * 65
            if temp_x > 140:
                temp_y += 70
                temp_x = 10
              
            self.tileset.append(TilesetOption(self.manager ,temp_x,temp_y,tile,self.painel, i))
    
    
    def __get_image_by_id(self, id):
        return self.tiles_images[int(id)]
    
    
    def __change_mouse_curser(self, image, active):
        if active:
            pos = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)
            self.mouse_editing = True
            self.mouse_image = image
            
        else:
            pygame.mouse.set_visible(True)
            return
    
    
    def send_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if 'mouse_changer' in str(event.ui_object_id):
                id = event.ui_object_id[-1]
                self.__change_mouse_curser(self.__get_image_by_id(id),True)
    
    
    def render(self,delta_time):
        super().render(delta_time)
        pos = pygame.mouse.get_pos()
        if self.mouse_editing:
            self.screen.blit(self.mouse_image, pos)


    
            


class TilesetOption:
    def __init__(self, manager, x, y, image, container, id) -> None:
        self.image = image
        self.uibutton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x-3, y-3), (60, 70)),
                                             text='',
                                             container=container,
                                             object_id=ObjectID(f'#mouse_changer_{id}'),
                                             manager= manager
                                             )
        self.ui_tile_image= UIImage(relative_rect=pygame.Rect((x, y),
                                                    (55, 64)), 
                                                    image_surface=image, container=container)
            
            
   