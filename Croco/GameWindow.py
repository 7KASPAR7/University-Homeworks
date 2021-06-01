import pygame as pg
from Button import Button
from PIL import ImageGrab
import torch
from NetWork import Net, get_dataset, dir_transforms, imshow
import torchvision.transforms as transforms
import random

def game():

    # screen
    pg.init()
    pg.font.init()
    pg.mixer.init()
    screen = pg.display.set_mode((800, 800))
    pg.display.set_caption("Croco")
    clock = pg.time.Clock()
    running = True
    shouldDraw = False
    screen.fill((255, 255, 255))

    # buttons
    topButton = Button()
    topButton.create_button(screen, (0, 255, 0), 0, 0, screen.get_width(), screen.get_height() * 0.1, 0, " ",(255, 0, 0))
    button = Button()
    button.create_button(screen, (255, 255, 0), screen.get_width() * 0.86, screen.get_height() * 0.03,screen.get_width() * 0.12, screen.get_height() * 0.07, 0, "Check", (255, 0, 0))
    clearButton = Button()
    clearButton.create_button(screen, (255, 255, 0), screen.get_width()*0.02, screen.get_height() * 0.03,
                         screen.get_width() * 0.12, screen.get_height() * 0.07, 0, "Clear", (255, 0, 0))

    # data transfrom
    data_dir, data_transforms = dir_transforms()
    _,_,classes,_ = get_dataset(data_dir, data_transforms)

    # setting Secret word
    secretWord = random.choice(classes)
    phrase = "Draw " + secretWord
    myfont = pg.font.SysFont('Comic Sans MS', 25)
    textsurface = myfont.render(phrase, False, (0, 0, 0))
    screen.blit(textsurface, (145, 15))
    isWin = False

    while running:
        clock.tick()
        for event in pg.event.get():

            # draw
            if event.type == pg.MOUSEBUTTONDOWN:
                if button.pressed(pg.mouse.get_pos()):
                    # check
                    image = ImageGrab.grab((900, 400, 1600, 1100))
                    image.save("screen.png")
                    shouldDraw = False
                    isWin = check(image, secretWord, screen, isWin)
                elif clearButton.pressed(pg.mouse.get_pos()):
                    pg.draw.rect(screen, (255, 255, 255), (0, screen.get_height() * 0.1, 800, 800), 0)
                else:
                    shouldDraw = True
            if event.type == pg.MOUSEBUTTONUP:
                shouldDraw = False
            if event.type == pg.QUIT:
                running = False

            if (topButton.pressed(pg.mouse.get_pos())):
                shouldDraw = False
            if (isWin):
                shouldDraw = False
            if shouldDraw:
                center = pg.mouse.get_pos()
                pg.draw.circle(screen, (0, 0, 0), center, 5)

        pg.display.flip()

    pg.quit()


def check(image, secretWord, screen, isWin):

    image = transforms.ToTensor()(image)
    image = transforms.Resize(128)(image)
    image = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])(image)

    PATH = './draw_net.pth'

    net = Net()
    net.load_state_dict(torch.load(PATH))
    outputs = net(image[None])
    #imshow(image)
    _, predicted = torch.max(outputs, 1)
    data_dir, data_transforms = dir_transforms()
    _,_,classes,_ = get_dataset(data_dir, data_transforms)
    #print('Predicted: ', ' '.join('%5s' % classes[predicted[0]]))

    # print word by computer
    myfont = pg.font.SysFont('Comic Sans MS', 25)
    pg.draw.rect(screen, (0,255,0), (470, 15, 220, 50), 0)
    textsurface = myfont.render("Is it " + classes[predicted] + "?", False, (0, 0, 0))
    screen.blit(textsurface, (470, 15))

    if (secretWord == classes[predicted] ):
        myfont = pg.font.SysFont('Comic Sans MS', 40)
        wintext = myfont.render("You are the champion, my friend", False, ((0, 0, 255)))
        pg.draw.rect(screen, (255, 255, 255), (120, 350, 570, 54), 0)
        screen.blit(wintext, (120, 350))
        isWin = True
    return isWin

game()