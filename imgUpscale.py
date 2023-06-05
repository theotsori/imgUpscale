#!/usr/bin/python3

import cv2

def upsample_image(image, scale):
    """Upsamples an image by the given scale factor.

    Args:
        image: The image to upsample.
        scale: The scale factor to upsample by.

    Returns:
        The upsampled image.
    """

    # Get the dimensions of the image.
    height, width = image.shape[:2]

    # Calculate the new dimensions based on the scale factor.
    new_height = int(height * scale)
    new_width = int(width * scale)

    # Upsample the image using the Lanczos interpolation algorithm.
    upsampled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

    # Return the upsampled image.
    return upsampled_image

def main():
    # Read the image from disk.
    image = cv2.imread("2019me.jpg")
 
    # Upsample the image to 4K.
    upsampled_image = upsample_image(image, 4)

    # Save the upsampled image to disk.
    cv2.imwrite("upsampled2019.jpg", upsampled_image)

if __name__ == "__main__":
    main()
