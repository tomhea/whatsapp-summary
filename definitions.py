import os
import pathlib


PROJECT_ROOT_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = PROJECT_ROOT_DIR / 'resources'
CHATS_DIR = RESOURCES_DIR / 'chats'
