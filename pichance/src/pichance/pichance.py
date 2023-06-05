import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from toga.widgets import FileSelection

import cv2
import urllib.request

def upsample_image(image, scale):
    # Upsample the image using the Lanczos interpolation algorithm.
    upsampled_image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LANCZOS4)
    return upsampled_image

def upscale_image(widget):
    # Check if an image file has been selected.
    if widget.file_selection.filename:
        # Read the image from disk.
        image = cv2.imread(widget.file_selection.filename)

        # Upscale the image to 4x.
        scale_factor = 4
        upsampled_image = upsample_image(image, scale_factor)

        # Save the upsampled image to disk.
        output_filename = widget.file_selection.filename + "_upscaled.jpg"
        cv2.imwrite(output_filename, upsampled_image)

        # Update the label to display a success message.
        widget.label.text = "Image upscaled and ready for download!"

        # Set the download URL for the upscaled image.
        widget.download_button.enabled = True
        widget.download_button.url = urllib.request.pathname2url(output_filename)

def main():
    # Create the main application window.
    app = toga.App("Image Upscaler", "com.example.imageupscaler")

    # Create a file selection widget for image upload.
    file_selection = FileSelection()

    # Create a button widget for upscaling the image.
    upscale_button = toga.Button('Upscale', on_press=upscale_image)

    # Create a label widget to display messages.
    label = toga.Label('Upload an image and press the "Upscale" button.')

    # Create a download button widget for the upscaled image.
    download_button = toga.Button('Download', enabled=False)

    # Create a box to contain the widgets.
    box = toga.Box(children=[file_selection, upscale_button, label, download_button], style=Pack(direction=COLUMN, padding=20))

    # Define the download button behavior.
    def on_download_button_press(widget):
        # Open the upscaled image file.
        with open(widget.url, 'rb') as file:
            content = file.read()
        # Prompt the user to save the file.
        save_file_dialog = toga.save_file_dialog(file_extension='.jpg')
        if save_file_dialog.show_modal():
            save_file_path = save_file_dialog.path
            with open(save_file_path, 'wb') as save_file:
                save_file.write(content)

    # Set the download button behavior.
    download_button.on_press = on_download_button_press

    # Create a main window with the box as its content.
    main_window = toga.MainWindow(title="Image Upscaler", size=(400, 300))
    main_window.content = box

    # Start the application event loop.
    app.main_window = main_window
    app.run()

if __name__ == "__main__":
    main()
