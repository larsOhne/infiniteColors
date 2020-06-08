import colorsys
import os
import math

def hsv_to_rgb(hue, sat, bright):
    r,g,b = colorsys.hsv_to_rgb(hue, sat, bright)
    
    return {"r": int(r*255), "g": int(g*255), "b": int(b*255)}



def generate_colors():
    # specify brightness and saturation
    brightness = 0.6
    saturation = 0.9

    # increment by which hue is incremented
    increment = (1 + 5.**0.5)*0.5  # golden ratio

    # all elements, the colors are generated for are read from text, separated by linebreaks
    with open("default.elems", "r") as input_file:
        elements = [line.replace("\n","") for line in input_file.readlines()]


    # generate hues by incrementing for each element and use remainder 
    color_elements = []
    for i in range(0, len(elements)):
        hue = increment*i % 1. 

        main_color = {
            "name": "Accent 0",
            "rgb": hsv_to_rgb(hue, saturation, brightness),
            "hex": ""
        }

        compl_color = {
            "name": "Compl. Accent",
            "rgb": hsv_to_rgb((hue + 0.5) % 1., saturation, brightness)
        }

        colors = [main_color, compl_color]

        c_elem = {
            "name": elements[i],
            "hue": hue,
            "sat": saturation,
            "bright": brightness,
            "colors": colors
        }

        color_elements.append(c_elem)


    return color_elements
