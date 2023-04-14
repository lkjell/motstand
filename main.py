# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()

winsizeW = 800
winsizeH = 600


screen = pygame.display.set_mode((winsizeW, winsizeH))
clock = pygame.time.Clock()
running = True
dt = 0

def motstand_create(posX, posY, width, height, bandW):
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

    # pygame.draw.rect(screen, bg, motstand)
    # pygame.draw.rect(screen, c1, band1)
    # pygame.draw.rect(screen, c2, band2)
    # pygame.draw.rect(screen, c3, band3)
    # pygame.draw.rect(screen, c4, band4)

def motstandPosXcalc(motstandW, winsizeW, N, index):
    # pos = (winsizeW - mostandW*N) / (N + 1)

    pos = (index + 1) * (winsizeW - motstandW*N) / (N + 1) + index*motstandW
    return pos


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

    motstandW = 100
    N = 3
    posX = motstandPosXcalc(motstandW, winsizeW, N, 0)
    motstand = motstand_create(posX, 0, motstandW, 50, 5)

    posX = motstandPosXcalc(motstandW, winsizeW, N, 1)
    motstand1 = motstand_create(posX, 0, motstandW, 50, 5)

    posX = motstandPosXcalc(motstandW, winsizeW, N, 2)
    motstand2 = motstand_create(posX, 0, motstandW, 50, 5)

    draw_resistor(motstand, "red", "blue", "green", "yellow", "violet")
    draw_resistor(motstand1, "red", "blue", "green", "yellow", "violet")
    draw_resistor(motstand2, "red", "blue", "green", "yellow", "violet")

    # rgb(230, 242, 255)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
