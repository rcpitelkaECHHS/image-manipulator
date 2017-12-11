import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw

def show_logo(logo_file):
    logo = PIL.Image.open(logo_file)
    plt.imshow(logo)
    
