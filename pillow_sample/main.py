from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display
import arabic_reshaper

# define paths
image_address = "./sample_images/image1.jpg"
font_base_path = "./fonts/"

# define fonts
english = ImageFont.truetype(font_base_path +'english.TTF', size=40)  # english font
titr = ImageFont.truetype(font_base_path +'titr.ttf', size=40)        # persian font 



with Image.open(image_address) as image:
    draw = ImageDraw.Draw(image)
    
    # draw persian text on image
    (x, y) = (100, 500)
    message = "پیام فارسی"
    
    # if you had trouble with persian text uncomment these 2 lines
    # message = arabic_reshaper.reshape(message)
    # message = get_display(message , base_dir='R')
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=titr)
    
    # draw english text on image
    (x, y) = (50, 200)
    message = "test message"
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=english)
    
    # save out put
    image.save('./outputs/out.jpg')