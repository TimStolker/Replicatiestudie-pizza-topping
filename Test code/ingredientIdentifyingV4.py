from skimage.viewer import ImageViewer
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb
from skimage import io
import matplotlib.pyplot as plt



pizzaKind = 'Hawaii'
filename = 'PizzaHawaii.jpg'

image = io.imread(filename)

viewer = ImageViewer(image)
viewer.show()
xs = image.shape[0] // 2
ys = image.shape[1] // 2

splits = [[image[0:xs, 0:ys], image[0:xs, ys:]], [image[xs:, 0:ys], image[xs:, ys:]]]

def pizzaPixelCount(image):
    pizzaCounter = 0
    height, width, _ = image.shape
    for i in range(height):
        for j in range(width):
            if(image[i,j][0] < 250 and image[i,j][1] < 250 and image[i,j][2] < 250):
                pizzaCounter += 1
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

def colorPreservePinapple(image): # minder aggresief
    pinappleCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] < 0.16 or hsv_img[:, :, 0][row][pixel] > 0.185 or hsv_img[:, :, 2][row][pixel] > 0.99:  #check op annanas
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

def colorPreserveBase(image): #moet ook op donkerder kunnen, minder aggresief
    baseCounter = 0
    hsv_img = rgb2hsv(image)
    for row in range(len(hsv_img[:, :, 0])):
        for pixel in range(len(hsv_img[:, :, 0][row])):
            if hsv_img[:, :, 0][row][pixel] < 0.10 or hsv_img[:, :, 0][row][pixel] > 0.13 or hsv_img[:, :, 2][row][pixel] > 0.9 :  #check op annanas
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

def printResultsPepperoni(pizza, pepperoni, base):
    pepperoniPercentage = ((pepperoni / pizza) * 100)
    basePercentage = ((base / pizza) * 100)
    restPercentage = (((pizza - pepperoni - base) / pizza) * 100)
    print("percentage of pepperoni: ", pepperoniPercentage)
    print("percentage of base: ", basePercentage)
    print("percentage of the rest of the pizza: ", restPercentage)

def printToppingQuarters(type, splits):
    pizzaPixels = pizzaPixelCount(image)
    quarterPizzaPixels = pizzaPixels/4

    baseColor1, baseCounter1 = colorPreserveBase(splits[0][0])
    baseColor2, baseCounter2 = colorPreserveBase(splits[0][1])
    baseColor3, baseCounter3 = colorPreserveBase(splits[1][0])
    baseColor4, baseCounter4 = colorPreserveBase(splits[1][1])

    if type == 'Hawaii':
        tomatoSauceColor1, sauceCounter1 = colorPreserveTomatoSauce(splits[0][0])
        tomatoSauceColor2, sauceCounter2 = colorPreserveTomatoSauce(splits[0][1])
        tomatoSauceColor3, sauceCounter3 = colorPreserveTomatoSauce(splits[1][0])
        tomatoSauceColor4, sauceCounter4 = colorPreserveTomatoSauce(splits[1][1])

        pineAppleColor1, pinappleCounter1 = colorPreservePinapple(splits[0][0])
        pineAppleColor2, pinappleCounter2 = colorPreservePinapple(splits[0][1])
        pineAppleColor3, pinappleCounter3 = colorPreservePinapple(splits[1][0])
        pineAppleColor4, pinappleCounter4 = colorPreservePinapple(splits[1][1])

        hamAndSauceColor1, hamCounter1 = colorPreserveHamAndSauce(splits[0][0])
        hamAndSauceColor2, hamCounter2 = colorPreserveHamAndSauce(splits[0][1])
        hamAndSauceColor3, hamCounter3 = colorPreserveHamAndSauce(splits[1][0])
        hamAndSauceColor4, hamCounter4 = colorPreserveHamAndSauce(splits[1][1])

        print( 'Tomato Sauce: ', ' Q1= ',sauceCounter1 / quarterPizzaPixels * 100, ' Q2= ',sauceCounter2 / quarterPizzaPixels * 100, ' Q3= ',sauceCounter3 / quarterPizzaPixels * 100, ' Q4= ',sauceCounter4 / quarterPizzaPixels * 100 )
        print( 'Pineapple: ', ' Q1= ',pinappleCounter1 / quarterPizzaPixels * 100, ' Q2= ',pinappleCounter2 / quarterPizzaPixels * 100, ' Q3= ',pinappleCounter3 / quarterPizzaPixels * 100, ' Q4= ',pinappleCounter4 / quarterPizzaPixels * 100 )
        print( 'Ham: ', ' Q1= ',(hamCounter1-sauceCounter1) / quarterPizzaPixels * 100, ' Q2= ',(hamCounter2-sauceCounter2) / quarterPizzaPixels * 100, ' Q3= ',(hamCounter3-sauceCounter3) / quarterPizzaPixels * 100, ' Q4= ',(hamCounter4-sauceCounter4) / quarterPizzaPixels * 100 )
        print( 'Base: ', ' Q1= ',baseCounter1 / quarterPizzaPixels * 100, ' Q2= ',baseCounter2 / quarterPizzaPixels * 100, ' Q3= ',baseCounter3 / quarterPizzaPixels * 100, ' Q4= ',baseCounter4 / quarterPizzaPixels * 100 )


    elif type == 'Salame':
        pepperoniColor1, pepperoniCounter1 = colorPreservePepperoni(splits[0][0])
        pepperoniColor2, pepperoniCounter2 = colorPreservePepperoni(splits[0][1])
        pepperoniColor3, pepperoniCounter3 = colorPreservePepperoni(splits[1][0])
        pepperoniColor4, pepperoniCounter4 = colorPreservePepperoni(splits[1][1])

        print('Pepperoni: ', ' Q1= ', pepperoniCounter1 / quarterPizzaPixels * 100, ' Q2= ', pepperoniCounter2 / quarterPizzaPixels * 100, ' Q3= ', pepperoniCounter3 / quarterPizzaPixels * 100, ' Q4= ', pepperoniCounter4 / quarterPizzaPixels * 100)
        print('Base: ', ' Q1= ', baseCounter1 / quarterPizzaPixels * 100, ' Q2= ', baseCounter2 / quarterPizzaPixels * 100, ' Q3= ',baseCounter3 / quarterPizzaPixels * 100, ' Q4= ', baseCounter4 / quarterPizzaPixels * 100)
    else:
        return 'Not a valid type'

if pizzaKind == 'Hawaii': #ananas pizza
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
    printToppingQuarters(pizzaKind,splits)



elif pizzaKind == 'Salame': #pepperoni pizza
    pepperoniColor, pepperoniCounter = colorPreservePepperoni(image)
    RGBPepperoniColor = hsv2rgb(pepperoniColor)
    viewer = ImageViewer(RGBPepperoniColor)
    viewer.show()

    baseColor, baseCounter = colorPreserveBase(image)
    RGBbaseColor = hsv2rgb(baseColor)
    viewer = ImageViewer(RGBbaseColor)
    viewer.show()

    pizzaPixels = pizzaPixelCount(image)
    printResultsPepperoni(pizzaPixels, pepperoniCounter, baseCounter)
    printToppingQuarters(pizzaKind, splits)
