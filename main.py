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
background = "purple"

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



def draw_resistor(motstand, c1, c2, c3, c4, bg=(230, 242, 255), state=0):
    if state == 0:
        pygame.draw.rect(screen, "black", motstand[0])
        return
    elif state == 1:
        colors = [bg, c1, c2, c3, c4]

        for c, m in zip(colors, motstand):
            pygame.draw.rect(screen, c, m)
    elif state == 2:
        pass
        # pygame.draw.rect(screen, background, motstand[0])
    else:
        print("Not implemented state")


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

def reset_state(states):
    for i in range(len(states)):
        if states[i] != 2:
            states[i] = 0

motstandW = 100
motstandH = 50
X = 5
Y = 4

motstand_colors = [cg.random_color() for _ in range(X*Y//2)]
motstand_colors += motstand_colors

motstand = motstand_create((motstandW, motstandH), X, Y)

current_motstand = None
prev_motstand = None

# states: 0 off
# states: 1 on
# states: 2 hidden

states = [0] * X*Y
num_click = 0
reset_timer = False
fps = 60
time_counter = 0

while running:
    if reset_timer:
        time_counter += 1
        if time_counter >= fps:
           time_counter = 0 
           num_click = 0
           reset_timer = False
           reset_state(states)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for idx, m in enumerate(motstand):
                if reset_timer:
                    break

                if m[0].collidepoint(pos):
                    prev_motstand = current_motstand
                    current_motstand = idx

                    state = states[idx]
                    if state == 0:
                        states[idx] = 1
                    elif state == 1:
                        break
                        # states[idx] = 0
                    elif state == 2:
                        break
                    else:
                        raise ("State not implemented", state)

                    print(f"Resistor index: {idx}, state from state to {states[idx]}")

                    num_click += 1
                    print(f"Number of clicks: {num_click}")
                    if num_click >= 2:
                        print("current_motstand:", current_motstand)
                        print("prev_motstand:", prev_motstand)

                        if (motstand_colors[prev_motstand] == motstand_colors[current_motstand]):
                            states[prev_motstand] = 2
                            states[current_motstand] = 2

                        reset_timer = True
                    # if num_click >= 2:
                    #     num_click = 0
                    #     reset_state(states)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background)

    for m, colors, s in zip(motstand, motstand_colors, states):
        draw_resistor(m, *colors, (120,120,120), s)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(fps) / 1000

pygame.quit()
