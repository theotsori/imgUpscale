#!/usr/bin/python3

import cv2
import sys

def upsample_image(image, scale):
    """Upsamples an image by the given scale factor.

    Args:
        image: The image to upsample (numpy array).
        scale: The scale factor to upsample by (float, > 1).

    Returns:
        The upsampled image (numpy array).

    Raises:
        ValueError: If the scale is not greater than 1.
    """
    if scale <= 1:
        raise ValueError("Scale factor must be greater than 1.")

    height, width = image.shape[:2]
    new_height = int(height * scale)
    new_width = int(width * scale)
    upsampled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
    return upsampled_image

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 upsample.py <input_image> <output_image>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    image = cv2.imread(input_image_path)
    if image is None:
        print(f"Error: Could not read the image '{input_image_path}'. Check the file path.")
        sys.exit(1)

    scale = 4  # You can make this dynamic if desired
    upsampled_image = upsample_image(image, scale)
    cv2.imwrite(output_image_path, upsampled_image)
    print(f"Upsampled image saved as '{output_image_path}'.")

if __name__ == "__main__":
    main()
