import textwrap

IMAGE_WIDTH = 25
IMAGE_HIGHT = 6
IMAGE_SIZE = IMAGE_HIGHT * IMAGE_WIDTH
fewest_zeroes = IMAGE_SIZE
layer_fewest_zeroes = ''
with open("day8_input.txt") as fi:
    image = fi.read()
layers = textwrap.wrap(image, IMAGE_SIZE)
for item in layers:
    if item.count('0') < fewest_zeroes:
        fewest_zeroes = item.count('0')
        layer_fewest_zeroes = item
print(layer_fewest_zeroes.count('1')*layer_fewest_zeroes.count('2'))



