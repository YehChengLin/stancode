"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    # Todo: create a new blank img that is as big as the original one

    # Loop over the picture
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel_me = img.get_pixel(x, y)
            new_img_p1 = new_img.get_pixel(x, y)


            
            # Todo: get pixel of new_img at x,y

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                pixe1_1 = img.get_pixel(x+1, y+1)
                pixe1_2 = img.get_pixel(x+1, y)
                pixe1_3 = img.get_pixel(x, y+1)
                new_img_p1.red = (pixel_me.red+pixe1_1.red+pixe1_2.red+pixe1_3.red)/4
                new_img_p1.green = (pixel_me.green + pixe1_1.green + pixe1_2.green + pixe1_3.green) / 4
                new_img_p1.blue = (pixel_me.blue + pixe1_1.blue + pixe1_2.blue + pixe1_3.blue) / 4

            elif x == (img.width-1) and y == 0:
                # Get pixel at the top-right corner of the image.
                pixe1_1 = img.get_pixel(x-1, y + 1)
                pixe1_2 = img.get_pixel(x - 1, y)
                pixe1_3 = img.get_pixel(x, y + 1)
                new_img_p1.red = (pixel_me.red + pixe1_1.red + pixe1_2.red + pixe1_3.red) / 4
                new_img_p1.green = (pixel_me.green + pixe1_1.green + pixe1_2.green + pixe1_3.green) / 4
                new_img_p1.blue = (pixel_me.blue + pixe1_1.blue + pixe1_2.blue + pixe1_3.blue) / 4

            elif x == 0 and y ==(img.height-1):
                # Get pixel at the bottom-left corner of the image
                pixe1_1 = img.get_pixel(x + 1, y - 1)
                pixe1_2 = img.get_pixel(x + 1, y)
                pixe1_3 = img.get_pixel(x, y - 1)
                new_img_p1.red = (pixel_me.red + pixe1_1.red + pixe1_2.red + pixe1_3.red) / 4
                new_img_p1.green = (pixel_me.green + pixe1_1.green + pixe1_2.green + pixe1_3.green) / 4
                new_img_p1.blue = (pixel_me.blue + pixe1_1.blue + pixe1_2.blue + pixe1_3.blue) / 4

            elif x == (img.width-1) and y ==(img.height-1):
                # Get pixel at the bottom-right corner of the image
                pixe1_1 = img.get_pixel(x, y - 1)
                pixe1_2 = img.get_pixel(x - 1, y)
                pixe1_3 = img.get_pixel(x-1, y - 1)
                new_img_p1.red = (pixel_me.red + pixe1_1.red + pixe1_2.red + pixe1_3.red) / 4
                new_img_p1.green = (pixel_me.green + pixe1_1.green + pixe1_2.green + pixe1_3.green) / 4
                new_img_p1.blue = (pixel_me.blue + pixe1_1.blue + pixe1_2.blue + pixe1_3.blue) / 4

            elif y == 0:
                # Get top edge's pixels (without two corners)
                pixe1_1 = img.get_pixel(x-1, y)
                pixe1_2 = img.get_pixel(x+1, y)
                pixe1_3 = img.get_pixel(x-1, y + 1)
                pixel_4 = img.get_pixel(x, y + 1)
                pixel_5 = img.get_pixel(x+1, y + 1)
                new_img_p1.red = (pixel_me.red + pixe1_1.red + pixe1_2.red + pixe1_3.red+pixel_4.red+pixel_5.red) / 6
                new_img_p1.green = (pixel_me.green + pixe1_1.green + pixe1_2.green + pixe1_3.green+pixel_4.green+pixel_5.green) / 6
                new_img_p1.blue = (pixel_me.blue + pixe1_1.blue + pixe1_2.blue + pixe1_3.blue+pixel_4.blue+pixel_5.blue)/ 6

            elif y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                pixe1_1 = img.get_pixel(x - 1, y)
                pixe1_2 = img.get_pixel(x + 1, y)
                pixe1_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_5 = img.get_pixel(x + 1, y - 1)
                new_img_p1.red = (pixel_me.red + pixe1_1.red + pixe1_2.red + pixe1_3.red + pixel_4.red + pixel_5.red) / 6
                new_img_p1.green = (pixel_me.green + pixe1_1.green + pixe1_2.green + pixe1_3.green + pixel_4.green + pixel_5.green) / 6
                new_img_p1.blue = (pixel_me.blue + pixe1_1.blue + pixe1_2.blue + pixe1_3.blue + pixel_4.blue + pixel_5.blue) / 6

            elif x == 0:
                # Get left edge's pixels (without two corners)
                pixe1_1 = img.get_pixel(x, y-1)
                pixe1_2 = img.get_pixel(x+1, y-1)
                pixe1_3 = img.get_pixel(x+1, y)
                pixel_4 = img.get_pixel(x+1, y + 1)
                pixel_5 = img.get_pixel(x, y + 1)
                new_img_p1.red = (pixel_me.red + pixe1_1.red + pixe1_2.red + pixe1_3.red + pixel_4.red + pixel_5.red) / 6
                new_img_p1.green = (pixel_me.green + pixe1_1.green + pixe1_2.green + pixe1_3.green + pixel_4.green + pixel_5.green) / 6
                new_img_p1.blue = (pixel_me.blue + pixe1_1.blue + pixe1_2.blue + pixe1_3.blue + pixel_4.blue + pixel_5.blue) / 6

            elif x ==(img.width-1):
                # Get right edge's pixels (without two corners)
                pixe1_1 = img.get_pixel(x, y - 1)
                pixe1_2 = img.get_pixel(x - 1, y - 1)
                pixe1_3 = img.get_pixel(x - 1, y)
                pixel_4 = img.get_pixel(x - 1, y + 1)
                pixel_5 = img.get_pixel(x, y + 1)
                new_img_p1.red = (pixel_me.red + pixe1_1.red + pixe1_2.red + pixe1_3.red + pixel_4.red + pixel_5.red) / 6
                new_img_p1.green = (pixel_me.green + pixe1_1.green + pixe1_2.green + pixe1_3.green + pixel_4.green + pixel_5.green) / 6
                new_img_p1.blue = (pixel_me.blue + pixe1_1.blue + pixe1_2.blue + pixe1_3.blue + pixel_4.blue + pixel_5.blue) / 6

            else:
                # Inner pixels.
                pixe1_1 = img.get_pixel(x-1, y)
                pixe1_2 = img.get_pixel(x + 1, y)
                pixe1_3 = img.get_pixel(x - 1, y-1)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_5 = img.get_pixel(x+1, y - 1)
                pixel_6 = img.get_pixel(x-1, y + 1)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_8 = img.get_pixel(x+1, y + 1)
                new_img_p1.red = (pixel_me.red + pixe1_1.red + pixe1_2.red + pixe1_3.red + pixel_4.red + pixel_5.red+pixel_6.red+pixel_7.red+pixel_8.red) /9
                new_img_p1.green = (pixel_me.green + pixe1_1.green + pixe1_2.green + pixe1_3.green + pixel_4.green + pixel_5.green++pixel_6.green+pixel_7.green+pixel_8.green) / 9
                new_img_p1.blue = (pixel_me.blue + pixe1_1.blue + pixe1_2.blue + pixe1_3.blue + pixel_4.blue + pixel_5.blue+pixel_6.blue+pixel_7.blue+pixel_8.blue) / 9
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
