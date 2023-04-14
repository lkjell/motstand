# Example file showing a circle moving on screen
from itertools import product
import pygame

import color_gen as cg


# pygame setup
pygame.init()

winsizeW = 800
winsizeH = 600


screen = pygame.display.set_mode((winsizeW, winsizeH))
clock = pygame.time.Clock()
running = True
dt = 0

def motstand_create_single(posX, posY, width, height, bandW):
    resistorSizeW = width #200
    resistorSizeH = height #100

    motstandPosx = posX #winsizeW // 2 - resistorSizeW//2
    motstandPosy = posY #winsizeH // 2 - resistorSizeH//2 + 200

    motstand = pygame.Rect(
            motstandPosx,
            motstandPosy,
            resistorSizeW,
            resistorSizeH,
            )

    bandW = bandW #10
    bandH = motstand.height

    x, y = motstand.topleft
    w = motstand.width
    h = motstand.height

    band1 = pygame.Rect(x + 5*bandW, y, bandW, bandH)

    x, y = band1.topleft
    w = band1.width
    h = band1.height

    band2 = pygame.Rect(x + bandW*2, y, bandW, bandH)

    x, y = band2.topleft
    w = band2.width
    h = band2.height

    band3 = pygame.Rect(x + bandW*2, y, bandW, bandH)

    x, y = band3.topleft
    w = band3.width
    h = band3.height

    band4 = pygame.Rect(x + bandW*2*2, y, bandW, bandH)

    return (motstand, band1, band2, band3, band4)



def draw_resistor(motstand, c1, c2, c3, c4, bg=(230, 242, 255)):
    colors = [bg, c1, c2, c3, c4]

    for c, m in zip(colors, motstand):
        pygame.draw.rect(screen, c, m)

def motstandPoscalc(motstandSize, winSize, X, Y, r, c):
    (motstandW, motstandH) = motstandSize
    (winsizeW, winsizeH) = winSize
    posX = (r + 1) * (winsizeW - motstandW*X) / (X + 1) + r*motstandW
    posY = (c + 1) * (winsizeH - motstandH*Y) / (Y + 1) + c*motstandH

    return posX, posY


def motstand_create(motstandSize, X, Y):
    (motstandW, motstandH) = motstandSize
    motstand = []

    for c, r in product(range(Y), range(X)):
        posX, posY = motstandPoscalc((motstandW, motstandH), 
                                     (winsizeW, winsizeH), X, Y, r, c)
        motstand.append(motstand_create_single(posX, posY, motstandW, motstandH, 5))

    return motstand

motstandW = 100
motstandH = 50
X = 5
Y = 4

motstand_colors = [cg.random_color() for _ in range(X*Y//2)]
motstand_colors += motstand_colors

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # motstandW = 100
    # posX = (winsizeW - 2*motstandW) / (1 + 2)

    # motstand = motstand_create(posX, 0, motstandW, 50, 5)
    # motstand1 = motstand_create(posX + motstandW + posX, 0, motstandW, 50, 5)


    motstand = motstand_create((motstandW, motstandH), X, Y)
    # posX = motstandPoscalc(motstandW, winsizeW, N, 0)
    # motstand = motstand_create(posX, 0, motstandW, 50, 5)
    #
    # posX = motstandPoscalc(motstandW, winsizeW, N, 1)
    # motstand1 = motstand_create(posX, 0, motstandW, 50, 5)
    #
    # posX = motstandPoscalc(motstandW, winsizeW, N, 2)
    # motstand2 = motstand_create(posX, 0, motstandW, 50, 5)

    for m, colors in zip(motstand, motstand_colors):
        draw_resistor(m, *colors, "violet")
        # draw_resistor(m, "red", "blue", "green", "yellow", "violet")

    # draw_resistor(motstand1, "red", "blue", "green", "yellow", "violet")
    # draw_resistor(motstand2, "red", "blue", "green", "yellow", "violet")

    # rgb(230, 242, 255)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
