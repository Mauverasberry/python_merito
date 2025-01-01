from time import sleep
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Aplikacja pygame')

button = False #na początku klawisz myszy nie jest wciśniety
color = (255,255,255)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            elif event.key == pygame.K_r:
                color = (255,0,0)
            elif event.key == pygame.K_c:
                screen.fill((0,0,0))  #czyszczenie planszy (wypelnianie jej na czarno) pod klawiszem c
            else:
                color = (255,255,255) #przy nacisnieciu dowolnego przycisku wraca do koloru bialego
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                button = True  #włączony przycisk myszy
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #czy jest puszczony L przycisk
                button = False
        elif event.type == pygame.MOUSEMOTION: #jesli myszka sie porusza
            if button: # w domysle == True
                mouse_x, mouse_y = event.pos
                pygame.draw.circle(screen, color, (mouse_x,mouse_y), 5)

    pygame.display.flip()

    sleep(.01)



