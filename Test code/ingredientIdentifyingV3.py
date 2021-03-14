from skimage.viewer import ImageViewer
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb
from skimage import io
filename = 'pizza2.jpg'
image = io.imread(filename)
#Lage saturation < 0.1
#hoge value > 0.9

def pizzaPixelCount(image):
    pizzaCounter = 0
    height, width, _ = image.shape
    for i in range(height):
        for j in range(width):
            if(image[i,j][0] < 250 and image[i,j][1] < 250 and image[i,j][2] < 250):
                pizzaCounter += 1

    print("totaal:",height*width)
    print("pizza:",pizzaCounter)
    return pizzaCounter

def colorPreserveTomatoSauce(image):
    sauceCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] > 0.03 and hsv_img[:, :, 0][row][pixel] < 1 and hsv_img[:, :, 1][row][pixel] < 0.68 or hsv_img[:, :, 2][row][pixel] > 0.9:  #check op tomaten sauce
                hsv_img[:, :, 1][row][pixel] = 0.0
            else:
                hsv_img[:, :, 1][row][pixel] = 1.0
                sauceCounter += 1

    return hsv_img, sauceCounter

def colorPreservePepperoni(image):
    pepperoniCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] > 0.03 and hsv_img[:, :, 0][row][pixel] < 1 and hsv_img[:, :, 1][row][pixel] < 0.55 or hsv_img[:, :, 2][row][pixel] > 0.9:  #check op tomaten sauce
                hsv_img[:, :, 1][row][pixel] = 0.0
            else:
                hsv_img[:, :, 1][row][pixel] = 1.0
                pepperoniCounter += 1

    return hsv_img, pepperoniCounter

def colorPreservePinapple(image):
    pinappleCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] < 0.15 or hsv_img[:, :, 0][row][pixel] > 0.185 or hsv_img[:, :, 2][row][pixel] > 0.99:  #check op annanas
                hsv_img[:, :, 1][row][pixel] = 0.0
            else:
                hsv_img[:, :, 1][row][pixel] = 1.0
                pinappleCounter += 1

    return hsv_img, pinappleCounter

def colorPreserveHamAndSauce(image):
    hamCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] > 0.08 and hsv_img[:, :, 0][row][pixel] < 0.4 or hsv_img[:, :, 2][row][pixel] > 0.9:  #check op tomaten sauce en ham
                hsv_img[:, :, 1][row][pixel] = 0.0
            else:
                hsv_img[:, :, 1][row][pixel] = 1.0
                hamCounter += 1

    return hsv_img, hamCounter

def colorPreserveBase(image):
    baseCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] < 0.10 or hsv_img[:, :, 0][row][pixel] > 0.15 or hsv_img[:, :, 2][row][pixel] > 0.9:  #check op annanas
                hsv_img[:, :, 1][row][pixel] = 0.0
            else:
                hsv_img[:, :, 1][row][pixel] = 1.0
                baseCounter += 1

    return hsv_img, baseCounter

def printResultsHawaii(pizza, sauce, pinapple, ham, base):
    saucePercentage = ((sauce/pizza)*100)
    pinapplePercentage = ((pinapple / pizza) * 100)
    hamPercentage = (((ham-sauce) / pizza) * 100)
    basePercentage = ((base / pizza) * 100)
    restPercentage = (((pizza - ham - pinapple - base) / pizza) * 100)
    print("percentage of sauce: ", saucePercentage)
    print("percentage of pinapple: ", pinapplePercentage)
    print("percentage of ham: ", hamPercentage)
    print("percentage of base: ", basePercentage)
    print("percentage of the rest of the pizza: ", restPercentage)

def printResultsPepperoni(pizza, sauce, pepperoni, base):
    saucePercentage = ((sauce / pizza) * 100)
    pepperoniPercentage = ((pepperoni / pizza) * 100)
    basePercentage = ((base / pizza) * 100)
    restPercentage = (((pizza - pepperoni - base - sauce) / pizza) * 100)
    print("percentage of sauce: ", saucePercentage)
    print("percentage of pepperoni: ", pepperoniPercentage)
    print("percentage of base: ", basePercentage)
    print("percentage of the rest of the pizza: ", restPercentage)

if filename == 'pizza3.jpg': #ananas pizza
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

elif filename == 'pizza2.jpg': #pepperoni pizza
    tomatoSauceColor, sauceCounter = colorPreserveTomatoSauce(image)
    RGBTomatoSauceColor = hsv2rgb(tomatoSauceColor)
    viewer = ImageViewer(RGBTomatoSauceColor)
    viewer.show()

    pepperoniColor, pepperoniCounter = colorPreservePepperoni(image)
    RGBPepperoniColor = hsv2rgb(pepperoniColor)
    viewer = ImageViewer(RGBPepperoniColor)
    viewer.show()

    baseColor, baseCounter = colorPreserveBase(image)
    RGBbaseColor = hsv2rgb(baseColor)
    viewer = ImageViewer(RGBbaseColor)
    viewer.show()

    pizzaPixels = pizzaPixelCount(image)
    printResultsPepperoni(pizzaPixels, sauceCounter, pepperoniCounter, baseCounter)
