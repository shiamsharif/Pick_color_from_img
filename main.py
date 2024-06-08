
# python -m pip install colorgram.py  

import colorgram  # type: ignore

# where we store the colors
rgb_colors = []
num_of_color = 30

colors = colorgram.extract('./japan.jpg',num_of_color)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


# Print a list in side the tuple
print(rgb_colors)



# if vs code can not run the code then it run on the terminal directly.
# python main.py