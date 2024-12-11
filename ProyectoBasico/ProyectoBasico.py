import pygame

pygame.init()
pantalla = pygame.display.set_mode((450, 450))
pygame.display.set_caption("TICTACTOE")

fondo = pygame.image.load("recursos/fondo.png")
fondo_inicio = pygame.image.load("recursos/fondo_inicio.png")
circulo = pygame.image.load("recursos/circulo.png")
equis = pygame.image.load("recursos/x.png")

fondo = pygame.transform.scale(fondo, (450, 450))
fondo_inicio = pygame.transform.scale(fondo_inicio, (450, 450))
circulo = pygame.transform.scale(circulo, (125, 125))
equis = pygame.transform.scale(equis, (125, 125))

cordenadas = [[(40, 50), (165, 50), (290, 50)],
              [(40, 175), (165, 175), (290, 175)],
              [(40, 300), (165, 300), (290, 300)]]

tablero = [['', '', ''],
           ['', '', ''],
           ['', '', '']]

turno = 'X'
reloj = pygame.time.Clock()

def graficar_tablero():
    pantalla.blit(fondo, (0, 0))
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == 'X':
                dibujar_x(fila, columna)
            elif tablero[fila][columna] == 'O':
                dibujar_o(fila, columna)

def dibujar_x(fila, columna):
    pantalla.blit(equis, cordenadas[fila][columna])

def dibujar_o(fila, columna):
    pantalla.blit(circulo, cordenadas[fila][columna])

def ganardor():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
            return True
    return False

def mostrar_texto(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def pantalla_inicio():
    pantalla.blit(fondo_inicio, [0,0])
    mostrar_texto(pantalla, "TICTACTOE", 65, 450 // 2, 450 // 4)
    mostrar_texto(pantalla, "Oprime una tecla", 27, 450 // 2, 450 // 2)
    #mostrar_texto(pantalla, "Oprime una tecla", 20, 450 // 2, 450 * 3/4)
    pygame.display.flip()
    esperar = True
    while esperar:
        reloj.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                esperar = False

def pantalla_ganador(turno):
    pantalla.blit(fondo_inicio, [0,0])
    mostrar_texto(pantalla, f"El ganador es {turno}", 65, 450 // 2, 450 // 4)
    mostrar_texto(pantalla, "Oprime una tecla para volver a jugar", 27, 450 // 2, 450 // 2)
    pygame.display.flip()
    esperar = True
    while esperar:
        reloj.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                esperar = False

def verificar_empate(tablero):
    empate = all(casilla == 'X' or casilla == 'O' for row in tablero for casilla in row)
    if empate:
        pantalla.blit(fondo_inicio, [0,0])
        mostrar_texto(pantalla, f"Ninguno ha ganado", 50, 450 // 2, 450 // 4)
        mostrar_texto(pantalla, "Oprime una tecla para volver a jugar", 27, 450 // 2, 450 // 2)
        pygame.display.flip()
        esperar = True
        while esperar:
            reloj.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    esperar = False
    return empate
    
def limpiar_tablero(tablero):
    tablero = [['', '', ''],
               ['', '', ''],
               ['', '', '']] 
    return tablero


start = pantalla_inicio()

while not start:
    reloj.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseX < 425):
                fila = (mouseY - 50) // 125
                columna = (mouseX - 40) // 125
                
                if tablero[fila][columna] == '':
                    tablero[fila][columna] = turno
                    start = ganardor()
                    if start:
                        pantalla_ganador(turno)
                        tablero = limpiar_tablero(tablero)
                        start = False
                    if verificar_empate(tablero):
                        tablero = limpiar_tablero(tablero)
                        start = False
                    turno = 'O' if turno == 'X' else 'X'
        
    graficar_tablero()
    pygame.display.update()
pygame.quit()