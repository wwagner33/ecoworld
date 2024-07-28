
import pygame as py


class EditiongTile:
    def __init__(self, x, y, size, screen, type=0) -> None:
        self.x = x
        self.my_font = py.font.SysFont('Comic Sans MS', 30)
        self.y = y
        self.size = size
        self.screen = screen
        self.type = type
    

    def render(self):
        gui_painel_width = 200 # Maybe replace after
        rect = py.Rect(self.x *self.size + gui_painel_width, self.y*self.size, self.size, self.size)
        # color = (0,0,0)
        

        if self.__is_mouse_inside():
            color = (100,100,100)
        else:
            color = (0,0,0)
            



        if self.type is None:
            color = (100, 100, 100)
            py.draw.rect(self.screen, color, rect, 1)
            py.draw.circle(self.screen, color, (self.x *self.size + gui_painel_width + self.size/2, self.y*self.size+ self.size/2), 5, 5)

        elif self.type == 0:
            color = self.__sum_tuples(color, (0, 150, 0))
            self.__draw_tile(color, rect)
        
        elif self.type == 1:
            color = self.__sum_tuples(color, (50, 0, 150))
            self.__draw_tile(color, rect)
        
        elif self.type == 2:
            color = self.__sum_tuples(color, (0, 50, 150))
            self.__draw_tile(color, rect)
        
        elif self.type == 3:
            color = self.__sum_tuples(color, (0, 150, 150))
            self.__draw_tile(color, rect)
            
            # py.draw.circle(self.screen, (py.Color(100, 100, 100)), (x *blockSize + gui_painel_width + blockSize/2, y*blockSize+ blockSize/2), 5, 5)

    
    def __draw_tile(self, color, rect):
        gui_painel_width = 200 # Maybe replace after
        py.draw.rect(self.screen, color, rect, 1)
        self.screen.blit(self.my_font.render(str(self.type), False, color), (self.x *self.size + gui_painel_width + self.size/2-5, self.y*self.size+15))


    def __sum_tuples(self, tuples1, tuples2):
        print(map(lambda x, y: x + y, tuples1, tuples2))
        return tuple(map(lambda x, y: x + y, tuples1, tuples2))



    def change_tile(self, tile):
        self.type = tile


    def __is_mouse_inside(self):
        return self.has_been_clicked(py.mouse.get_pos())


    def has_been_clicked(self, pos): # talvez trocar o nome
        gui_painel_width = 200 # Maybe replace after
        x, y = pos

        return self.x* self.size + gui_painel_width <= x and x < self.x * self.size + gui_painel_width + self.size  and \
                self.y* self.size <= y and y < self.y  * self.size + self.size
    



