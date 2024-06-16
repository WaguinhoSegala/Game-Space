import pygame
pygame.init() 
tamanho  = ( 1000, 563) 
clock = pygame.time.Clock() 
tela = pygame.display.set_mode(tamanho) 
pygame.display.set_caption("Game Título") 
fundo = pygame.image.load("fundo.jpg")  
branco  = (255,255,255) 
preto = (0,0,0)
while True: 
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
 

    tela.fill(branco) 
    tela.blit(fundo, (0,0) )
    pygame.display.update() 
    clock.tick(60) 

pygame.quit()
