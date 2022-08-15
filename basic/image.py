from simpleimage import SimpleImage
def main():
    image = SimpleImage("download.jpg")
    image.show

    dark(image)
    image.show()
def dark(image):
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2
