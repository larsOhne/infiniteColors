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
    increment = (1 + 5.**0.5)*0.05  # golden ratio

    # all elements, the colors are generated for are read from text, separated by linebreaks
    with open("default.elems", "r") as input_file:
        elements = [line.replace("\n","") for line in input_file.readlines()]


    # generate hues by incrementing for each element and use remainder 
    color_elements = []
    for i in range(0, len(elements)):
        hue = (0.5 + increment*i) % 1.  

        main_color = {
            "name": "Accent",
            "rgb": hsv_to_rgb(hue, saturation, brightness),
            "hex": ""
        }
        colors = [main_color]

        # dark accents
        for j in range(1,3):
            ad_b = brightness - j*0.2
            sat_b = brightness - j*0.1
            colors.append({
            "name": f"Dark Accent {j}",
            "rgb": hsv_to_rgb(hue, sat_b, ad_b),
            "hex": ""
        })

        # light accents
        for j in range(1,3):
            ad_b = brightness + j*0.3
            sat_b = brightness - j*0.1
            colors.append({
            "name": f"Light Accent {j}",
            "rgb": hsv_to_rgb(hue, sat_b, ad_b),
            "hex": ""
        })

        # complementary color
        compl_hue = (hue + 0.5) % 1.
        compl_color = {
            "name": "Compl. Accent",
            "rgb": hsv_to_rgb((hue + 0.5) % 1., saturation, brightness)
        }
        colors.append(compl_color)

        
        # Compl. dark accents
        for j in range(1,2):
            ad_b = brightness - j*0.2
            sat_b = brightness - j*0.1
            colors.append({
            "name": f"Compl. Dark Accent {j}",
            "rgb": hsv_to_rgb(compl_hue, sat_b, ad_b),
            "hex": ""
        })

        # Compl. light accents
        for j in range(1,2):
            ad_b = brightness + j*0.3
            sat_b = brightness - j*0.1
            colors.append({
            "name": f"Compl. Light Accent {j}",
            "rgb": hsv_to_rgb(compl_hue, sat_b, ad_b),
            "hex": ""
        })

        c_elem = {
            "id": i,
            "name": elements[i],
            "hue": hue,
            "sat": saturation,
            "bright": brightness,
            "colors": colors
        }

        color_elements.append(c_elem)


    return color_elements
