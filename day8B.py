import textwrap

IMAGE_WIDTH = 25
IMAGE_HIGHT = 6
IMAGE_SIZE = IMAGE_HIGHT * IMAGE_WIDTH
rendered_image = list('2'*IMAGE_SIZE)
with open("day8_input.txt") as fi:
    image = fi.read()
layers = textwrap.wrap(image, IMAGE_SIZE)
for item in reversed(layers):
    for count, figure in enumerate(item):
        if figure == '2':
            pass
        elif figure in ['0', '1']:
            rendered_image[count] = figure
image_str = ''.join(rendered_image)
rend_image_layers = textwrap.wrap(image_str, IMAGE_WIDTH)
rend_image_layers = '\n'.join(rend_image_layers)
print(rend_image_layers)
