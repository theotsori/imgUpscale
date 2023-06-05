# Image Upsampling

This Python script performs image upsampling using the OpenCV library. It takes an input image, upsamples it by a specified scale factor, and saves the upsampled image to disk.

## Prerequisites

- Python 3.x
- OpenCV library (`cv2`)

## Usage

1. Ensure that you have the necessary prerequisites installed.

2. Download the script and save it to your desired location.

3. Place the input image you want to upsample in the same directory as the script and name it "2019me.jpg" (or modify the code to specify the correct filename).

4. Open a terminal or command prompt and navigate to the directory containing the script.

5. Run the script by executing the following command:

    ```bash
    python script_name.py
    ```

   Make sure to replace `script_name.py` with the actual name of the script file.

6. The script will read the input image, upsample it using the Lanczos interpolation algorithm, and save the upsampled image as "upsampled2019.jpg" in the same directory.

## Function

### `upsample_image(image, scale)`

This function takes an image and a scale factor as input and returns the upsampled image. It uses the following steps to upsample the image:

1. Get the dimensions of the input image.
2. Calculate the new dimensions based on the scale factor.
3. Upsample the image using the Lanczos interpolation algorithm with the `cv2.resize()` function.
4. Return the upsampled image.

### `main()`

The `main()` function serves as the entry point of the script. It performs the following tasks:

1. Reads the input image from disk.
2. Calls the `upsample_image()` function to upsample the image with a scale factor of 4.
3. Saves the upsampled image to disk as "upsampled2019.jpg".

## Notes

- The script uses the Lanczos interpolation algorithm (`cv2.INTER_LANCZOS4`) for image upsampling. You can modify this if you prefer a different interpolation algorithm by changing the `interpolation` parameter in the `cv2.resize()` function.
- Ensure that the input image is in the same directory as the script and has the correct filename specified in the code.
- The script overwrites any existing "upsampled2019.jpg" file in the directory, so be cautious if you have a file with the same name.
- You can modify the code to suit your specific image and scaling requirements.

Feel free to explore and modify the code to enhance the image upsampling functionality according to your needs.
