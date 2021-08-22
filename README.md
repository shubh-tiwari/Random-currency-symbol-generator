# Synthetic currency symbol image generator
This repo can be used to generate syntheitc images of currency symbols to train classification and recognition models. Supported currency symbols currently are rupee, yen, pound, euro and dollar.

## Sample data
![Sample image](https://github.com/shubh-tiwari/currency-symbol-data-generator/blob/main/utils/images/generated_data.JPG)
#### More generated samples are present [here](https://github.com/shubh-tiwari/currency-symbol-data-generator/tree/main/generated_data)

## Kind of variations included
Any number of variations from the below list can be grouped together and applied to generate dataset.
1. Different backgrounds (white, gaussian, specific color, syntheic background)
2. Orientation (horizontal and vertical, flipped on either side)
3. Different font type and font colors
4. skewed and sheared images
5. Blurring to add distortions

#### To generate, use [this file](https://github.com/shubh-tiwari/currency-symbol-data-generator/blob/main/csdg/generate.py)
