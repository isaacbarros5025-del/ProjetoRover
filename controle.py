
import pygame   
import socket   


tela = pygame.display.set_mode((300, 300))

fonte = pygame.font.SysFont(None, 40)

cliente = socket.socket()

cliente.connect(("192.168.0.116", 5000))

while True:

    
    tela.fill((30, 30, 30))

    
    texto = fonte.render("Use W A S D", True, (255, 255, 255))

    
    tela.blit(texto, (60, 130))

    
    pygame.display.update()

    
    for e in pygame.event.get():

        
        if e.type == pygame.QUIT:
            pygame.quit()  

        
        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_w:
                cliente.send(b"w")  

            if e.key == pygame.K_s:
                cliente.send(b"s")  

            if e.key == pygame.K_a:
                cliente.send(b"a")  

            if e.key == pygame.K_d:
                cliente.send(b"d")  

        if e.type == pygame.KEYUP:
            cliente.send(b"p") 