import pygame
from tkinter import Tk, simpledialog

# Inicialização do Pygame
pygame.init()
# Carregar a imagem do fundo
fundo = pygame.image.load("assets/fundo.jpg")
tamanho = (1000, 563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("SPACE MARKER")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Lista para armazenar as estrelas
estrelas = []

# Inicialização do Tkinter
nomeestrela = Tk()
nomeestrela.withdraw()  # Esconder a janela principal do Tkinter

def pedir_nome_estrela():
    # Função para pedir o nome da estrela
    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    return nome

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos
            nome = pedir_nome_estrela()
            if nome:
                estrelas.append((pos, nome))

    # Preencher a tela com a cor branca
    tela.fill(branco)
    # Desenhar o fundo
    tela.blit(fundo, (0, 0))

    # Desenhar as estrelas e as linhas entre elas
    for i, (pos, nome) in enumerate(estrelas):
        pygame.draw.circle(tela, branco, pos, 5, 0)
        fonte = pygame.font.Font(None, 24)
        texto = fonte.render(nome, True, branco)
        tela.blit(texto, (pos[0] + 10, pos[1] - 10))
        if i > 0:
            pygame.draw.line(tela, branco, estrelas[i - 1][0], pos, 1)

    # Atualizar a tela
    pygame.display.update()
    clock.tick(60)

pygame.quit()