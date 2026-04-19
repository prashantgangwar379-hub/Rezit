from PIL import Image


MAX_DIMENSION = 1920


def resize_to_limit(image: Image.Image) -> Image.Image:
    """
    Resize image so that its largest dimension is at most MAX_DIMENSION.
    Maintains aspect ratio.

    Args:
        image (PIL.Image.Image): Input image

    Returns:
        PIL.Image.Image: Resized (or original) image
    """

    width, height = image.size

    # Check if resizing is needed
    if max(width, height) <= MAX_DIMENSION:
        return image  # No resize needed

    # Calculate scaling factor
    scale = MAX_DIMENSION / max(width, height)

    new_width = int(width * scale)
    new_height = int(height * scale)

    # Resize using high-quality downsampling
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    return resized_image