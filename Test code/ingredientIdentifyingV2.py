from skimage.viewer import ImageViewer
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb
from skimage import io

image = io.imread('pizza3.jpg')

def pizzaPixelCount(image):
    pizzaCounter = 0
    height, width, _ = image.shape
    for i in range(height):
        for j in range(width):
            if(image[i,j] is not [255,255,255]):
                pizzaCounter += 1
    return pizzaCounter

def colorPreserveTomatoSauce(image):
    sauceCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] > 0.04 and hsv_img[:, :, 0][row][pixel] < 1:  #check op tomaten sauce
                hsv_img[:, :, 1][row][pixel] = 0.0
            else:
                sauceCounter += 1

    return hsv_img, sauceCounter

def colorPreservePinapple(image):
    pinappleCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] < 0.15 or hsv_img[:, :, 0][row][pixel] > 0.185:  #check op annanas
                hsv_img[:, :, 1][row][pixel] = 0.0
            else:
                pinappleCounter += 1

    return hsv_img, pinappleCounter

def colorPreserveHamAndSauce(image):
    hamCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] > 0.08 and hsv_img[:, :, 0][row][pixel] < 0.4:  #check op tomaten sauce en ham
                hsv_img[:, :, 1][row][pixel] = 0.0
            else:
                hamCounter += 1

    return hsv_img, hamCounter

def colorPreserveBase(image):
    baseCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] < 0.10 or hsv_img[:, :, 0][row][pixel] > 0.15:  #check op annanas
                hsv_img[:, :, 1][row][pixel] = 0.0
            else:
                baseCounter += 1

    return hsv_img, baseCounter

def printResultsHawaii(pizza, sauce, pinapple, ham, base):
    saucePercentage = ((sauce/pizza)*100)
    pinapplePercentage = ((pinapple / pizza) * 100)
    hamPercentage = (((ham-sauce) / pizza) * 100)
    restPercentage = (((pizza - ham - pinapple - base) / pizza) * 100)
    basePercentage = ((base / pizza) * 100)
    print("percentage of sauce: ", saucePercentage)
    print("percentage of pinapple: ", pinapplePercentage)
    print("percentage of ham: ", hamPercentage)
    print("percentage of base: ", basePercentage)
    print("percentage of the rest of the pizza: ", restPercentage)

tomatoSauceColor, sauceCounter = colorPreserveTomatoSauce(image)
RGBTomatoSauceColor = hsv2rgb(tomatoSauceColor)
viewer = ImageViewer(RGBTomatoSauceColor)
viewer.show()

pineAppleColor, pinappleCounter = colorPreservePinapple(image)
RGBpineAppleColor = hsv2rgb(pineAppleColor)
viewer = ImageViewer(RGBpineAppleColor)
viewer.show()

hamAndSauceColor, hamCounter = colorPreserveHamAndSauce(image)
RGBhamAndSauceColor = hsv2rgb(hamAndSauceColor)
viewer = ImageViewer(RGBhamAndSauceColor)
viewer.show()

baseColor, baseCounter = colorPreserveBase(image)
RGBbaseColor = hsv2rgb(baseColor)
viewer = ImageViewer(RGBbaseColor)
viewer.show()

pizzaPixels = pizzaPixelCount(image)
printResultsHawaii(pizzaPixels, sauceCounter, pinappleCounter, hamCounter, baseCounter)
print(sauceCounter, pinappleCounter, hamCounter, baseCounter)
