from rezit.loader import load_image
from rezit.preprocess import prepare_image
from rezit.resizer import resize_to_limit
from rezit.optimizer import optimize_image
from rezit.utils import save_final_image
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description="Rezit - Image Size Optimizer")

    parser.add_argument("--input", required=True, help="Path to input image")
    parser.add_argument("--target", type=int, required=True, help="Target size in KB")
    parser.add_argument("--tolerance", type=int, default=10)
    parser.add_argument("--min_quality", type=int, default=20)

    args = parser.parse_args()

    image_path = args.input

    if not os.path.exists(image_path):
        print("Error: Input file does not exist.")
        return

    os.makedirs("output", exist_ok=True)

    image = load_image(image_path)
    image = prepare_image(image)
    image = resize_to_limit(image)

    result = optimize_image(
        image,
        target_kb=args.target,
        tolerance_kb=args.tolerance,
        min_quality=args.min_quality
    )

    if result:
        original_name = os.path.splitext(os.path.basename(image_path))[0]
        output_file = f"output/{original_name}_rezit.jpg"

        save_final_image(
            image,
            output_file,
            result["width"],
            result["height"],
            result["quality"]
        )

        print("\nFinal Result:")
        print(f"Saved as: {output_file}")
        print(f"Size: {result['size']/1024:.2f} KB")
        print(f"Quality: {result['quality']}")
        print(f"Resolution: {result['width']}x{result['height']}")
    else:
        print("Optimization failed.")


if __name__ == "__main__":
    main()