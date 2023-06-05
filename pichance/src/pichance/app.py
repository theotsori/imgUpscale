import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import cv2
import urllib.request
from tkinter import filedialog
import os

class PicHance(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Create a button widget for image upload.
        upload_button = toga.Button('Upload Image', on_press=self.upload_image)

        # Create a button widget for upscaling the image.
        upscale_button = toga.Button('Upscale', on_press=self.upscale_image, enabled=False)

        # Create a label widget to display messages.
        self.label = toga.Label('Upload an image and press the "Upscale" button.')

        # Create a download button widget for the upscaled image.
        self.download_button = toga.Button('Download', on_press=self.download_image, enabled=False)

        # Add widgets to the main box
        main_box.add(upload_button)
        main_box.add(upscale_button)
        main_box.add(self.label)
        main_box.add(self.download_button)

        # Create a main window
        self.main_window = toga.MainWindow(title=self.formal_name, size=(400, 300))
        self.main_window.content = main_box
        self.main_window.show()

    def upload_image(self, widget):
        # Open a file dialog for image selection.
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.image_path = file_path
            self.label.text = f"Image selected: {self.image_path}"
            self.download_button.enabled = False

    def upscale_image(self, widget):
        # Read the image from disk.
        image = cv2.imread(self.image_path)

        # Upscale the image to 4x.
        scale_factor = 4
        upsampled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LANCZOS4)

        # Save the upsampled image to disk.
        output_filename = self.image_path + "_upscaled.jpg"
        cv2.imwrite(output_filename, upsampled_image)

        # Update the label to display a success message.
        self.label.text = "Image upscaled and ready for download!"

        # Set the download path for the upscaled image.
        self.download_path = output_filename
        self.download_button.enabled = True

    def download_image(self, widget):
        # Prompt the user to save the file.
        save_file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Image", "*.jpg")])
        if save_file_path:
            # Copy the upscaled image to the desired save path.
            os.replace(self.download_path, save_file_path)
            self.label.text = "Image downloaded successfully!"

    def on_close(self):
        # Ensure the temporary file is deleted when the app is closed
        if hasattr(self, 'download_path') and os.path.exists(self.download_path):
            os.remove(self.download_path)

def main():
    return PicHance()


if __name__ == '__main__':
    main().main_loop()
