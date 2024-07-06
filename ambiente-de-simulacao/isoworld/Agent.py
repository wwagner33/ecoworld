import random

from Config import Config

class Agent:
    def __init__(self, x, y, image=None):
        self.x = x
        self.y = y
        self.image = image
        self.world_width = Config.WORLD_WIDTH
        self.world_height = Config.WORLD_HEIGHT
        # self.x_offset = 450
        # # self.y_offset= 100


    def update(self):
        direction = random.choice(['left', 'right', 'up', 'down'])
        if direction == 'left':
            self.x = (self.x - 1) % self.world_width
        elif direction == 'right':
            self.x = (self.x + 1) % self.world_width
        elif direction == 'up':
            self.y = (self.y - 1) % self.world_height
        elif direction == 'down':
            self.y = (self.y + 1) % self.world_height

    def render(self, screen):
        xScreen = self.x_offset + self.x * 55 / 2 - self.y * 55 / 2
        yScreen = self.y_offset + self.y * 64 / 4 + self.x * 64 / 4


        if self.image:
            # screen.blit(self.image, (self.x * self.image.get_width() + self.x_offset, self.y * self.image.get_height() + self.y_offset))
            screen.blit(self.image, (xScreen, yScreen))

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        return self.x, self.y