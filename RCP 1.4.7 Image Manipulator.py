import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw

def show_logo(logo_file):
    logo = plt.imread(logo_file)
    plt.imshow(logo)
    
def show_image(image_file):
    image = plt.imread(os.getcwd() + '/Image Files/' + image_file)
    plt.imshow(image)

def dramatize_image(image_file, logo=None):
    image = plt.imread(os.getcwd() + '/Image Files/' + image_file)
    height = len(image)
    width = len(image[0])
    for r in range(0, height):
        for c in range(1, width):
            if r/c > (height/width):
                color_value = int(round(sum(image[r][c])/3))
                image[r][c] = (color_value, color_value, color_value)
    plt.imshow(image)