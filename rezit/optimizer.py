from rezit.compressor import save_image, get_file_size


def optimize_image(image, target_kb, tolerance_kb=10, min_quality=20):
    target_bytes = target_kb * 1024
    tolerance_bytes = tolerance_kb * 1024

    quality_step = 10
    quality_start = 90
    quality_soft_limit = 50

    min_dimension = 320

    best_size = None
    best_quality = None

    current_width, current_height = image.size

    output_path = "output/temp.jpg"

    while True:

        print(f"\nTrying resolution: {current_width}x{current_height}")

        last_size = None

        for quality in range(quality_start, min_quality - 1, -quality_step):

            save_image(image, output_path, quality)
            current_size = get_file_size(output_path)
            last_size = current_size

            print(f"Trying quality={quality}, size={current_size/1024:.2f} KB")

            if current_size <= target_bytes:

                if current_size >= (target_bytes - tolerance_bytes):
                    print("Within tolerance. Stopping early.")
                    return {
                        "size": current_size,
                        "quality": quality,
                        "width": current_width,
                        "height": current_height
                    }

                if best_size is None or current_size > best_size:
                    best_size = current_size
                    best_quality = quality

            if quality < quality_soft_limit:
                print("Quality dropped below soft limit → resizing preferred")
                break

        if last_size is None:
            break

        ratio = last_size / target_bytes

        if ratio > 2:
            scale = 0.7
        elif ratio > 1.3:
            scale = 0.85
        else:
            scale = 0.95

        new_width = int(current_width * scale)
        new_height = int(current_height * scale)

        if min(new_width, new_height) < min_dimension:
            print("Minimum dimension reached. Stopping.")
            break

        image = image.resize((new_width, new_height))
        current_width, current_height = image.size

    # Fallback result
    if best_size is not None:
        return {
            "size": best_size,
            "quality": best_quality,
            "width": current_width,
            "height": current_height
        }

    return None