
from Agent import Agent


class PlayerAgent(Agent):
    def __init__(self, x, y, image=None):
        super().__init__( x, y, image)
        # self.x_offset = 450
        # self.y_offset = 100



    def update(self):
        ...

    def move(self,xNew,yNew):
        self.x = ( self.x + xNew - self.world_height) % self.world_height
        # print(self.x)
        self.y = ( self.y + yNew - self.world_height) % self.world_height
        # super().setPosition( self.x, self.y)
       
       #TODO: Temos que continuar nisso, até dar certo

    #    if getObjectAt( (self.x+xNew+worldWidth)%worldWidth , (self.y+yNew+worldHeight)%worldHeight ) == 0: # dont move if collide with object (note that negative values means cell cannot be walked on)
    #         setAgentAt( self.x, self.y, noAgentId)