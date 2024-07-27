
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


        py.draw.rect(self.screen, (py.Color(100, 100, 100)), rect, 1)

        if self.type == 0:
            py.draw.rect(self.screen, (py.Color(100, 100, 100)), rect, 1)
            py.draw.circle(self.screen, (py.Color(100, 100, 100)), (self.x *self.size + gui_painel_width + self.size/2, self.y*self.size+ self.size/2), 5, 5)
        
        elif self.type == 1:
            py.draw.rect(self.screen, (py.Color(100, 0, 255)), rect)
            self.screen.blit(self.my_font.render('1', False, (0, 0, 0)), (self.x *self.size + gui_painel_width + self.size/2-5, self.y*self.size+15))
            
            # py.draw.circle(self.screen, (py.Color(100, 100, 100)), (x *blockSize + gui_painel_width + blockSize/2, y*blockSize+ blockSize/2), 5, 5)

    

    def change_tile(self, tile):
        self.type = tile


    def has_been_clicked(self, pos):
        gui_painel_width = 200 # Maybe replace after
        x, y = pos

        return self.x* self.size + gui_painel_width <= x and x < self.x * self.size + gui_painel_width + self.size  and \
                self.y* self.size <= y and y < self.y  * self.size + self.size
            

