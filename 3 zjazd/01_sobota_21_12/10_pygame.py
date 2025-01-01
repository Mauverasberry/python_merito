from time import sleep
import pygame

pygame.init() #zainicjalowanie
screen = pygame.display.set_mode((500,500)) #okreslanie rozmiaru okna
pygame.display.set_caption('Aplikacja pygame') #ustaw_podpis

run = True  #potrzebna by zamienic na False gdy klikniemy np. na x
while run: #podtrzymanie zycia programu by nie zniknęło okienko
    for event in pygame.event.get(): #przelatujemy po wszytskich przesluchiwaczach pygame
        if event.type == pygame.QUIT: #zamyka okno za pomocą x
            run = False
        elif event.type == pygame.KEYDOWN: #keydown - reaguje na przycisniecie klawisza
            # KEYUP - reaguje na puszczenie klawisza
            if event.key == pygame.K_q: #klawisz Q zamyka tez okno
                run = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #klikniecie myszki dowolnym jej przyciskiem
            if event.button == 1:  #reaguje na L przycisk myszy
                mouse_x, mouse_y = event.pos  #pobieramy pozycje myszy po kliknieciu
                # print(mouse_x, mouse_y) printuje pozycje myszy typu (175 305)
                screen.set_at((mouse_x, mouse_y), 'red') #na naszym screenie ustaw pixel w pozycji() i kolor ()
                # kolor mozna tez zapisaxc jako RGB (255,255,255)
    pygame.display.flip()  #wyswietl to co zostaloo namalowane

    sleep(.1)

    

