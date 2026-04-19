from PIL import Image


def load_image(path: str) -> Image.Image:
    """
    Loads an image from the given path.

    Args:
        path (str): Path to the image file

    Returns:
        PIL.Image.Image: Loaded image object
    """
    try:
        image = Image.open(path)
        return image
    except Exception as e:
        raise RuntimeError(f"Failed to load image: {e}")