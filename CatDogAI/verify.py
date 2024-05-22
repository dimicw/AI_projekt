import os
from PIL import Image

def check_images(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(subdir, file)
            try:
                # Open the image file
                img = Image.open(file_path)
                # This line checks if the image is loadable
                img.verify()
            except (IOError, SyntaxError) as e:
                print('Bad file:', file_path)

check_images('images/train/')