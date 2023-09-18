from PIL import Image
import numpy as np


# Braille character mapping
braille_mapping = [
    "⠀",
    "⠁",
    "⠃",
    "⠇",
    "⠉",
    "⠛",
    "⠻",
    "⢻",
    "⣻",
    "⣽",
    "⣾",
    "⣿",
]

def greyscale(image):
    image = Image.convert('L')
    return image

def image_to_braille(image_path):
    # Open and convert the image to grayscale
    image = greyscale(Image.open(image_path))
    # Get the width and height of the image
    width, height = image.size
    #define the Braille character size (each character represents a 2x4 pixel area)
    char_width = 2
    char_height = 4
    
    braille_art = ""

    braille_art = lightscale(height, width, image, char_height, char_width, braille_art);
    return braille_art;
    

def lightscale(height, width, image, char_height, char_width, braille_art):
    for y in range(0, height, char_height):
        for x in range(0, width, char_width):
            # Calculate the average brightness for the 2x4 pixel area
            total_brightness = 0
            for j in range(char_height):
                for i in range(char_width):
                    total_brightness += image.getpixel((x + i, y + j))    
            
            braille_art += brightMapping(total_brightness, char_width, char_height)
        # Add a newline character at the end of each row
        braille_art += "\n"
    return braille_art;




def brightMapping(totalBrightness, char_width, char_height):
    # Calculate the average brightness and map it to a Braille character
    avg_bright = totalBrightness / (char_width * char_height)
    braille_index = int(avg_bright / 255 * (len(braille_mapping) - 1))
    braille_char = braille_mapping[braille_index]
    return braille_char;



def convertToBraille(image):
    braille_art = image_to_braille(image)
    #Test result image
    print(braille_art)
    return braille_art

