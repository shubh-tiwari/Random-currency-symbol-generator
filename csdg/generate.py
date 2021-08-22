"""The script to generate the random data"""
import os
import random as rnd
import numpy as np
from generator import Generator

# Number of data to generate per currency
num = 20

save_folder = '../generated_data'
currency_list = ["yen", "rupee", "dollar",
                    "euro", "pound"]

if not os.path.exists(save_folder):
    print("here")
    print(os.mkdir(save_folder))

for currency in currency_list:
    currency_folder = os.path.join(save_folder, currency)
    if not os.path.exists(currency_folder):
        os.mkdir(currency_folder)
    
    gen = Generator()
    for i in range(num):
        # Adding different kind of randomness
        gen.orientation = rnd.choice([0,1])
        gen.skew_angle = rnd.randint(0,4)
        gen.shear_param = rnd.randint(-4,4)
        gen.bgr_type = rnd.choice([0,1,2,3])
        gen.blur = rnd.choice([0,1])
        gen.font_color = tuple(np.random.choice(range(256), size=3))
        if gen.bgr_type==2:
            gen.bgr_color = tuple(np.random.choice(range(256), size=3))
        gen.flip = rnd.choice([0,1,2])

        # Generate and save the generated image
        gen(currency)
        gen.image.save(os.path.join(currency_folder, str(i+1)+'.png'))