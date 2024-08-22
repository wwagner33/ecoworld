from pygame import Rect
from pygame import error
from pygame_gui import UI_BUTTON_PRESSED, UI_FILE_DIALOG_PATH_PICKED, UI_WINDOW_CLOSE
from pygame_gui.core import ObjectID
from pygame_gui.core.utility import create_resource_path
from pygame_gui.elements import UIButton
from pygame_gui.elements.ui_panel import UIPanel
from pygame_gui.elements.ui_label import UILabel
from pygame_gui.windows import UIFileDialog

from SimulatorThings.Gui.Gui import Gui


class SimulationGui(Gui):
    def __init__(self, screen, informations) -> None:
        super().__init__(screen=screen)
        self.informations: dict = informations
        self.painel = UIPanel(
            relative_rect = Rect((0, 0), (200, 640)), manager=self.manager
        )
        self.status_informations: dict = self.__init_label_informations() # TODO espaço onde podemos colocar inforações que nos interessam
        self.bottuns: list = self.__init_select_map_buttom()  # TODO botões para trocar de mapa ou fazer outras funcionalidades
        self.file_dialog = None


    def __init_label_informations(self):
        informartions = []
        for info, value in self.informations.items():
            info_l = f"{info}: {value}"

            informartions.append(
                UILabel(
                    Rect((10, 20 * len(informartions)), (200, 50)),
                    text=info_l,
                    manager=self.manager,
                    container=self.painel,
                    anchors={"right_target": self.painel},
                    # Colocar mais alinhamento
                )
            )
        return informartions


    def __init_select_map_buttom(self):
        return [
            UIButton(
                relative_rect=Rect((30, 590), (100, 50)),
                text="Mudar Mapa",
                container=self.painel,
                object_id=ObjectID("#select_map"),
                manager=self.manager,
            )
        ]


    def send_event(self, event, simulator):
        if event.type == UI_BUTTON_PRESSED:
            if "select_map" in str(event.ui_object_id):
                self.file_dialog = UIFileDialog(
                    Rect(160, 50, 440, 500),
                    self.manager,
                    window_title="Load Image...",
                    initial_file_path="SimulatorThings/maps/",
                    allow_picking_directories=True,
                    allow_existing_files_only=True,
                    allowed_suffixes={""},
                )
        
        if event.type == UI_FILE_DIALOG_PATH_PICKED:
            try:
                map_path = create_resource_path(event.text)
                self.__change_map(simulator, map_path)

            except error:
                pass

            if (event.type == UI_WINDOW_CLOSE and event.ui_element == self.file_dialog):
                self.file_dialog = None


    def __change_map(self, simulator, file_path):
        simulator.world = simulator._load_world(file_path, simulator.player)
        simulator.init_world()
        print("Mapa Mudado")
