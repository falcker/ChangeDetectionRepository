import imageio
from pathlib import Path
import os

def get_image_paths(root_dir : Path = Path(r'C:\Users\Gebruiker\Documents\Falcker\AI\data\Operator Rounds\output\stitching_module')):
    DATA_ROOT = os.environ.get("AI_DATA_ROOT", None)
    if not DATA_ROOT:
        print('something is wrong with the AI_DATA_ROOT environment variable.')
        exit 
    DATA_ROOT = Path(DATA_ROOT)

    # image_dir = DATA_ROOT / "Operator Rounds\input\PhotoStream"
    image_dir = DATA_ROOT / "Operator Rounds\output\stitching_module"
    image_paths = list(image_dir.iterdir())
    return image_paths

def image_path_to_data(img_paths):
    return [imageio.imread(img_path)[:,:,0:3] for img_path in img_paths]

before_img, after_img = image_path_to_data(get_image_paths()[0:2])
