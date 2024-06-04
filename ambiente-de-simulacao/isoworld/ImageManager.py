import pygame
from Config import Config
import os

class ImageManager:
    def __init__(self):
        self.tile_images = []
        self.object_images = []
        self.agent_images = []

    def load_images(self):
        # Define paths for different types of game assets
        tile_paths = [
            'assets/basic111x128/platformerTile_48_ret.png',  # grass
            'assets/ext/isometric-blocks/PNG/Platformer tiles/platformerTile_33.png',  # brick
            'assets/ext/isometric-blocks/PNG/Abstract tiles/abstractTile_12.png',  # blue grass
            'assets/ext/isometric-blocks/PNG/Abstract tiles/abstractTile_09.png'  # gray brick
        ]
        object_paths = [
            None,  # default -- never drawn
            'assets/basic111x128/tree_small_NW_ret.png',  # normal tree
            'assets/basic111x128/blockHuge_N_ret.png',  # building block
            'assets/basic111x128/tree_small_NW_ret_red.png'  # burning tree
        ]
        agent_paths = [
            None,  # default -- never drawn
            'assets/basic111x128/invader_ret.png',  # invader
            'assets/basic111x128/ghost_pinky.png',  # purple ghost
            'assets/basic111x128/baby.png'  # baby
        ]

        self.tile_images = [self.load_image(path) for path in tile_paths if path]
        self.object_images = [self.load_image(path) if path else None for path in object_paths]
        self.agent_images = [self.load_image(path) if path else None for path in agent_paths]

    def load_image(self, path):
        try:
            print(path)
            original_image = pygame.image.load(os.path.join('', path)).convert_alpha()
            scaled_image = pygame.transform.scale(
                original_image,
                (int(original_image.get_width() * Config.SCALE_MULTIPLIER),
                 int(original_image.get_height() * Config.SCALE_MULTIPLIER))
            )
            return scaled_image
        except Exception as e:
            
            print(f"Error loading image {path}: {e}")
            raise e
            return None