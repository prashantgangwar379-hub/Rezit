from PIL import Image

def prepare_image(image: Image.Image) -> Image.Image:
    """
    Converts image to RGB and handles trasparency if present.

    Args:
        image (PIL.Image.Image): Input image

    Returns:
        PIL.Image.Image: RGB image ready for processing
    """
   # Case: Image has alpha channel (RGBA or LA)
    if image.mode in ("RGBA", "LA"):
        # Create white background
        background = Image.new("RGB", image.size, (255, 255, 255))

        # Paste image on top using alpha channel as mask
        background.paste(image, mask=image.split()[-1])

        return background

    # Case: Image is palette-based (like some PNGs)
    elif image.mode == "P":
        return image.convert("RGB")

    # Case: Already RGB
    elif image.mode == "RGB":
        return image

    # Any other mode → convert
    else:
        return image.converts("RGB") 