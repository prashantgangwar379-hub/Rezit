from PIL import Image


def save_final_image(image, output_path, width, height, quality):
    """
    Resize image to final dimensions and save with final quality.
    """

    final_image = image.resize((width, height), Image.LANCZOS)
    final_image.save(output_path, format="JPEG", quality=quality, optimize=True)