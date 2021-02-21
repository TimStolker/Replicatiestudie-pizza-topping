from skimage.viewer import ImageViewer
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb
from skimage import io
import matplotlib.pyplot as plt

image = io.imread('pizza3.jpg')

def colorPreserveTomatoSauce(image):
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] > 0.07 and hsv_img[:, :, 0][row][pixel] < 1:  #check op tomaten sauce
                hsv_img[:, :, 1][row][pixel] = 0.0

    return hsv_img

def colorPreservePinapple(image):
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] < 0.15 or hsv_img[:, :, 0][row][pixel] > 0.185:  #check op annanas
                hsv_img[:, :, 1][row][pixel] = 0.0

    return hsv_img

def colorPreserveHamAndSauce(image):
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] > 0.08 and hsv_img[:, :, 0][row][pixel] < 0.4:  #check op tomaten sauce en ham
                hsv_img[:, :, 1][row][pixel] = 0.0

    return hsv_img

tomatoSauceColor = colorPreserveTomatoSauce(image)
RGBTomatoSauceColor = hsv2rgb(tomatoSauceColor)
viewer = ImageViewer(RGBTomatoSauceColor)
viewer.show()

pineAppleColor = colorPreservePinapple(image)
RGBpineAppleColor = hsv2rgb(pineAppleColor)
viewer = ImageViewer(RGBpineAppleColor)
viewer.show()

hamAndSauceColor = colorPreserveHamAndSauce(image)
RGBhamAndSauceColor = hsv2rgb(hamAndSauceColor)
viewer = ImageViewer(RGBhamAndSauceColor)
viewer.show()
