from PIL import Image, ImageDraw
import random
import math

class Cell():
    def __init__(self, x, y):
        pass

def render_square(w, h):
    image = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    putpixel = image.putpixel

    y_start = 0
    y_end = image.height
    step_size = int(image.width / 15)

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=64)

    x_start = 0
    x_end = image.width
    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=64)
    
    del draw


    image.save('test.png')
    # image.show()


render_square(500, 500)