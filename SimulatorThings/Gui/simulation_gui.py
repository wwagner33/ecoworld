from pygame import Rect
from pygame_gui.elements.ui_panel import UIPanel
from pygame_gui.elements.ui_label import UILabel
from SimulatorThings.Gui.Gui import Gui


class SimulationGui(Gui):
    def __init__(self, screen, informations) -> None:
        super().__init__(screen=screen)
        self.informations : dict = informations
        self.painel = UIPanel(
            relative_rect = Rect((0, 0), (200, 640)), manager=self.manager
        )
        
        self.status_informations : dict = self.__init_label_informations() # TODO espaço onde podemos colocar inforações que nos interessam
        self.bottuns = [] # TODO botões para trocar de mapa ou fazer outras funcionalidades

    def __init_label_informations(self):
        informartions = []
        for info, value in self.informations.items():
            info_l = f'{info}: {value}'            
            
            informartions.append(
                UILabel(
                    Rect((20, 20 * len(informartions)), (200, 50)), 
                    text=info_l,
                    manager=self.manager, 
                    container=self.painel,
                    # Colocar mais alinhamento
                    )
                )
        return informartions
    
