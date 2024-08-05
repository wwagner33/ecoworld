import pygame
import pygame_gui
from pygame_gui.elements.ui_image import UIImage
from pygame_gui.elements.ui_panel import UIPanel
from pygame_gui.core import ObjectID

from pygame_gui.elements import UIButton
from SimulatorThings.Gui.Gui import Gui
from SimulatorThings.Gui.height_pop_up_gui import HeightPopUpGui 


class MapMakerGui(Gui):
    def __init__(self, screen, images) -> None:
        super().__init__(screen=screen)
        self.painel = UIPanel(relative_rect=pygame.Rect((0, 0),(200, 640)), manager=self.manager)
        self.tiles_images = images
        self.mouse_editing = False
        self.mouse_image = None
        self.tileset = self.__init_tileset()
        self.buttons = self.__init_buttons()
        
    

    def __init_tileset(self):
        tileset = []
        temp_x = 10 # Todo refactore that
        temp_y = 10
        for i, tile in enumerate(self.tiles_images):
            temp_x = 10 + i * 65
            if temp_x > 140:
                temp_y += 70
                temp_x = 10
              
            tileset.append(TilesetOption(self.manager ,temp_x,temp_y,tile,self.painel, i))
        
        return tileset
        


    def __init_buttons(self):
        buttons = []
        buttons.append(UIButton(relative_rect=pygame.Rect((30, 590), (70, 50)),
                                             text='Apagar',
                                             container=self.painel,
                                             object_id=ObjectID(f'#mouse_changer_R'),
                                             manager= self.manager
                                             ))
        buttons.append(UIButton(relative_rect=pygame.Rect((105, 590), (80, 50)),
                                             text='Salvar',
                                             container=self.painel,
                                             object_id=ObjectID(f'#save_current_map'),
                                             manager= self.manager
                                             ))
        return buttons


    def __get_image_by_id(self, id):
        return self.tiles_images[int(id)]
    
    
    def __change_mouse_curser(self, image, active):
        if active:
            pygame.mouse.set_visible(False)
            self.mouse_editing = True
            self.mouse_image = image
        else:
            pygame.mouse.set_visible(True)
            self.mouse_editing = False
            self.mouse_image = None
            return
    
    
    def send_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if 'mouse_changer' in str(event.ui_object_id):
                if event.ui_object_id[-1] == 'R':
                    self.__change_mouse_curser(None, False)
                    return
                id = event.ui_object_id[-1]
                self.__change_mouse_curser(self.__get_image_by_id(id),True)
    
    
    def render(self,delta_time):
        super().render(delta_time)
        pos = pygame.mouse.get_pos()
        if self.mouse_editing:
            self.screen.blit(self.mouse_image, pos)


    def show_height_popup(self, x, y):
        return HeightPopUpGui(self.screen, self.manager, x, y)


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
        
   