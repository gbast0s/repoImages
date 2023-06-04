from PIL import Image
import os

def resize_images(folder_paths):
    for folder_path in folder_paths:
        output_folder = folder_path + '_resized'
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(folder_path):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(folder_path, filename)
                output_path = os.path.join(output_folder, filename)

                with Image.open(image_path) as image:
                    resized_image = image.resize((180, 180), Image.ANTIALIAS)
                    resized_image.save(output_path)
                    print(f"Resized {filename} successfully.")

        print(f"All images in folder {folder_path} resized successfully.")

# Provide an array of folder paths where the images are located
folder_paths = [
    './train/angry',
    './train/happy',
    './train/sad',
    './valid/angry',
    './valid/happy',
    './valid/sad',
]

# Call the resize_images function with the array of folder paths
resize_images(folder_paths)