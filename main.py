import pygame
from recursos import pedir_nome_estrela, salvar_marcacoes, carregar_marcacoes, excluir_marcacoes

pygame.init()

fundo = pygame.image.load("assets/fundo.jpg")
tamanho = (1000, 563)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("SPACE MARKER")

icone = pygame.image.load("assets/icone.png")
pygame.display.set_icon(icone)

branco = (255, 255, 255)
preto = (0, 0, 0)

estrelas = carregar_marcacoes()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salvar_marcacoes(estrelas)
            pygame.quit()
            quit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos
            nome = pedir_nome_estrela()
            if nome == "desconhecido":
                nome += f" ({pos[0]}, {pos[1]})"
            estrelas[pos] = nome
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F10:
                salvar_marcacoes(estrelas)
            elif evento.key == pygame.K_F11:
                estrelas = carregar_marcacoes()
            elif evento.key == pygame.K_F12:
                estrelas = {}
                excluir_marcacoes()
            elif evento.key == pygame.K_ESCAPE:
                salvar_marcacoes(estrelas)
                pygame.quit()
                quit()

    tela.fill(branco)
    tela.blit(fundo, (0, 0))

    for i, (pos, nome) in enumerate(estrelas.items()):
        pygame.draw.circle(tela, branco, pos, 5, 0)
        fonte = pygame.font.Font(None, 24)
        texto = fonte.render(nome, True, branco)
        tela.blit(texto, (pos[0] + 10, pos[1] - 10))
        if i > 0:
            pygame.draw.line(tela, branco, list(estrelas.keys())[i - 1], pos, 1)

    fonte = pygame.font.SysFont("comicsans", 14)
    texto = fonte.render("Pressione F10 para Salvar os pontos", True, branco)
    tela.blit(texto, (10, 10))
    texto = fonte.render("Pressione F11 para Carregar os pontos", True, branco)
    tela.blit(texto, (10, 40))
    texto = fonte.render("Pressione F12 para Deletar os pontos", True, branco)
    tela.blit(texto, (10, 70))

    pygame.display.update()
    clock.tick(60)

pygame.quit()