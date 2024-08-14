



from SimulatorThings.Gui.Gui import Gui


class SimulationGui(Gui):
    def __init__(self, screen) -> None:
        super().__init__(screen=screen)
        self.status_informations = [] # TODO espaço onde podemos colocar inforações que nos interessam
        self.bottuns = [] # TODO botões para trocar de mapa ou fazer outras funcionalidades
