from pygame import Rect
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton
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
        self.bottuns : list = self.__init_select_map_buttom() # TODO botões para trocar de mapa ou fazer outras funcionalidades

    def __init_label_informations(self):
        informartions = []
        for info, value in self.informations.items():
            info_l = f'{info}: {value}'            
                       
            
            informartions.append(
                UILabel(
                    Rect((10, 20 * len(informartions)), (200, 50)),
                    text = info_l,
                    manager=self.manager, 
                    container=self.painel,
                    anchors={'right_target': self.painel}
                    # Colocar mais alinhamento
                    )
                )
        return informartions
    
    
    def __init_select_map_buttom(self):
        return [
            UIButton(
                relative_rect = Rect((30, 590), (100, 50)),
                text = "Mudar Mapa",
                container = self.painel,
                object_id = ObjectID("#select_map"),
                manager = self.manager,
            )
        ]
