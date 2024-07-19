"""
Image Editing:
-save image in different formats: .jpeg, .json
-cropping (entire image, one part of the image), flipping
-opacity
-insert text
-adding image
"""
import cv2
from PIL import Image

my_image = 'assets/image_3.jpg'

#save image in diff formats
def convert_image_format(input_image_path, output_image_path, output_format):
    try:
        # Open the image file
        img = Image.open(input_image_path)
        
        # Save it in the desired format
        img.save(output_image_path, format=output_format)
        
        print(f"Image saved successfully as {output_image_path} in {output_format} format.")
    except IOError:
        print(f"Unable to save image as {output_image_path} in {output_format} format.")

# Example usage:
input_image_path = 'assets/image_1.jpg'  # Replace with your input image path
output_image_path = 'output_image.png'  # Replace with your desired output image path
output_format = 'PNG'  # Desired output format (e.g., JPEG, PNG, BMP, etc.)

# Convert the image
"""
    JPEG: 'JPEG' or 'JPG'
    PNG: 'PNG'
    BMP: 'BMP'
    GIF: 'GIF'
    TIFF: 'TIFF' or 'TIF'
    WebP: 'WebP'
    ICO: 'ICO'
    PPM/PGM/PBM: 'PPM', 'PGM', 'PBM'
    PDF: 'PDF'
    EPS: 'EPS'
"""

#convert_image_format(input_image_path, output_image_path, output_format)


#Crop the base image

def crop_image(image_path, x, y, width, height):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    
    # Crop the image
    cropped_img = img[y:y+height, x:x+width]

    
    # Display the original and cropped images (optional)
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return cropped_img

# Example usage:
image_path = 'assets/image_1.jpg'  # Replace with your image path
x, y, width, height = 100, 50, 300, 200  # Define your ROI coordinates

# Crop the image
#cropped_image = crop_image(image_path, x, y, width, height)


#flip the image

def flip_img(image_path, direction):
    #0 means around x axis, 1 means y axis
    flipped_img = cv2.imread(image_path, 1)
    flipped_img = cv2.flip(flipped_img, direction)
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Flipped Image', flipped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#flip_img('assets/image_1.jpg', 0)

#insert text
# need to add parameters on where to add the text
def add_text(image_path, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    height = 500
    input_img = cv2.imread(image_path, 1)
    text_img = cv2.putText(input_img, text, (200, height -10), font, 4, [0,0,0], 5, cv2.LINE_AA)
    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Image with text', text_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#add_text('assets/image_3.jpg', "add some text")

#adding an image

import cv2

def add_image_overlay(background_image_path, overlay_image_path, x, y):
    # Read the background and overlay images
    background = cv2.imread(background_image_path)
    overlay = cv2.imread(overlay_image_path, -1)  # Use -1 to include alpha channel if present
    
    # Overlay the image onto the background
    y_end = y + overlay.shape[0]
    x_end = x + overlay.shape[1]
    alpha_overlay = overlay[:, :, 3] / 255.0
    alpha_background = 1.0 - alpha_overlay
    
    for c in range(0, 3):
        background[y:y_end, x:x_end, c] = (alpha_overlay * overlay[:, :, c] +
                                            alpha_background * background[y:y_end, x:x_end, c])
    
    # Display the result (optional)
    cv2.imshow('Result Image', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return background

# Example usage:
background_image_path = my_image  # Replace with your background image path
overlay_image_path = 'assets/image_5.jpg'  # Replace with your overlay image path
x, y = 100, 50  # Position where overlay image will be placed

# Add overlay image onto the background image
result_image = add_image_overlay(background_image_path, overlay_image_path, x, y)

