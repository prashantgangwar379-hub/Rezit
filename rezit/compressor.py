import os
from PIL import Image

def save_image(image: Image.Image, output_path: str, quality: int)-> None:
    """
    Saves the image as JPG with specified quality.

    Args:
        image(PIL.Image.Image): Image to save
        output_path(str): File path
        quality(int): Compression quality(1-95)
    """
    image.save(output_path, format="JPEG", quality=quality, optimize=True)

def get_file_size(path: str) ->int:
    """
    Returns file size in bytes.

    Args:
        path(str): file path

    Returns:
        int: Size in bytes
            
    """
    return os.path.getsize(path)