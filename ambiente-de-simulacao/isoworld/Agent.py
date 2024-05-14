import random

class Config:
    WORLD_WIDTH = 32
    WORLD_HEIGHT = 32

class Agent:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.world_width = Config.WORLD_WIDTH
        self.world_height = Config.WORLD_HEIGHT

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
        if self.image:
            screen.blit(self.image, (self.x * self.image.get_width(), self.y * self.image.get_height()))

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        return self.x, self.y