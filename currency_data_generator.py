import numpy as np
from PIL import ImageDraw, ImageFont
import matplotlib.pyplot as plt
import utils

class Generator(object):
    def __init__(self, bgr_type=0, bgr_folder=None, bgr_color=None, font_color=(0,0,0), 
                    blur=0, orientation=0, flip=0, skew_angle=0, shear_param=0):
        """Initializes the parameters :
            1. bgr_type = 0: Gaussian, 1: white, 2: specified color, 3: from folder
            2. bgr_folder = Folder containing background images (require if bgr_type=3)
            3. bgr_color = specified color for background (require if bgr_type=2)
            4. font_color = font color of the pasted currency symbol
            5. blur = blur parameter
            6. orientation = 0 for horizontal else vertical
            7. flip = 0 : no flip, 1: leftright flip 2. topbottom flip
            8. skew_angle = Angle to skew the final image
            9. shear_param = Parameter to shear horizontal by specified pixels
        """
        self.bgr_type = bgr_type
        if self.bgr_type==3:
            self.bgr_folder = bgr_folder
        if self.bgr_type==2:
            self.bgr_color = bgr_color
        self.font_color = font_color
        self.orientation = orientation
        self.flip = flip
        self.skew_angle = skew_angle
        self.shear_param = shear_param
        self.blur = blur

    def __call__(self, currency):
        self.generate_symbol_image(currency)

    @staticmethod
    def get_currency_text(currency):
        """functions required the specified currency text"""
        currency_dict = {
            "yen" : "\u00a5",
            "rupee" : "\u20b9",
            "baht" : "\u0e3f",
            "dollar" : "\u0024",
            "euro" : "\u20ac",
            "pound" : "\u00a3",
            "bitcoin" : "\u20bf"
        }
        return currency_dict[currency]

    def generate_bgr(self):
        """Function to generate background"""
        if self.bgr_type==0:
            return utils.get_gaussian_background(32, 32)
        elif self.bgr_type==1:
            return utils.get_white_background(32,32)
        elif self.bgr_type==2:
            return utils.get_color_background(32, 32, self.bgr_color)
        elif self.bgr_type==3:
            return utils.get_bgr_image(32, 32, self.bgr_folder)
        else:
            print("Background type is not specified between 0-3. Returning gaussian background")
            return utils.get_gaussian_background(32, 32)

    def paste_symbol(self):
        """function to draw symbol on the given bacground"""
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("fonts/Lato-Black.ttf", 30)
        return draw.text((6, -3),self.currency_text,self.font_color,font=font)
    
    def change_orientation(self):
        # Changing orientation to vertical
        if self.orientation:
            self.image = utils.orientation_vertical(self.image)
        # Flipping image - topbottom or leftright
        if self.flip == 1:
            self.image = utils.mirror_leftright(self.image)
        elif self.flip == 2:
            self.image = utils.mirror_upside(self.image)

    def add_rotational_variations(self):
        if self.skew_angle:
            self.image = utils.rotate(self.image, self.skew_angle)
        if self.shear_param:
            self.image = utils.shear(np.asarray(self.image).astype(np.uint8), self.shear_param)

    def add_distortions(self):
        if self.blur:
            self.image = utils.blur(self.image, self.blur)

    def generate_symbol_image(self, currency):
        """Funtion to generate the final image"""
        self.image = self.generate_bgr()
        self.currency_text = self.get_currency_text(currency)
        self.paste_symbol()
        self.change_orientation()
        self.add_rotational_variations()
        self.add_distortions()

if __name__=="__main__":
    gen1 = Generator(shear_param=3)
    gen1("rupee")
    plt.imshow(gen1.image)
    plt.show()
    gen1("yen")
    plt.imshow(gen1.image)
    plt.show()
