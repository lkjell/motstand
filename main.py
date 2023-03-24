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

resistorSizeW = 200
resistorSizeH = 100

motstand = pygame.Rect(
        winsizeW // 2 - resistorSizeW//2, 
        winsizeH // 2 - resistorSizeH//2 - 200, 
        resistorSizeW,
        resistorSizeH,
        )

bandW = 10
bandH = motstand.height

x, y = motstand.topleft
w = motstand.width
h = motstand.height

band1 = pygame.Rect(x + 50, y, bandW, bandH)

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

def draw_resistor(c1, c2, c3, c4, bg=(230, 242, 255)):
    pygame.draw.rect(screen, bg, motstand)
    pygame.draw.rect(screen, c1, band1)
    pygame.draw.rect(screen, c2, band2)
    pygame.draw.rect(screen, c3, band3)
    pygame.draw.rect(screen, c4, band4)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    draw_resistor("red", "blue", "green", "yellow", "violet")

    # rgb(230, 242, 255)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
