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

def modify_image(image_file, logo_file=None, logo_size=100, position='bottom_left', directory=None):
    if directory == None:
        directory = os.getcwd()
    new_directory = os.path.join(directory, 'Modified Image Files')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    image_v1 = plt.imread(directory + '/Image Files/' + image_file)
    height = len(image_v1)
    width = len(image_v1[0])
    for r in range(0, height):
        for c in range(1, width):
            if (float(r)/float(c)) > (float(height)/float(width)):
                color_value = int(round(sum(image_v1[r][c])/3))
                image_v1[r][c] = (color_value, color_value, color_value)
                
    plt.imsave(os.path.join(new_directory, image_file), image_v1)
    
    if logo_file != None:
        image_v2 = PIL.Image.open(os.path.join(new_directory, image_file))
        image_width, image_height = image_v2.size
        logo = PIL.Image.open(os.path.join(directory, logo_file))
        logo = logo.resize((logo_size, logo_size), PIL.Image.ANTIALIAS)
        logo_width, logo_height = logo.size
        if position == 'bottom_left':
            image_v2.paste(logo, (0, image_height-logo_height), logo)
        if position == 'bottom_right':
            image_v2.paste(logo, (image_width-logo_width, image_height-logo_height), logo)
        if position == 'top_left':
            image_v2.paste(logo, (0, 0), logo)
        if position == 'top_right':
            image_v2.paste(logo, (image_width-logo_width, 0), logo)
        image_v2.save(os.path.join(new_directory, image_file))