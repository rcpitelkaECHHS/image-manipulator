import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw

def show_logo(logo_file):
    logo = PIL.Image.open(logo_file)
    plt.imshow(logo)
    
def show_image(image_file):
    image = PIL.Image.open(os.getcwd() + '/Image Files/' + image_file)
    plt.imshow(image)
