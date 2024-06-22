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

# Definir o ícone da aplicação
icone = pygame.image.load("assets/icone.png")
pygame.display.set_icon(icone)

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Lista para armazenar as estrelas
estrelas = []

# Inicialização do Tkinter
nomeestrela = Tk()
nomeestrela.withdraw()

def pedir_nome_estrela():
    nome = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela (deixe vazio se desconhecida):")
    return nome if nome else "desconhecido"

def salvar_marcacoes():
    try:
        with open("marcacoes.txt", "w") as arquivo:
            for estrela in estrelas:
                pos, nome = estrela
                arquivo.write(f"{pos[0]},{pos[1]},{nome}\n")
        print("Marcações salvas com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar marcações: {e}")

def carregar_marcacoes():
    global estrelas
    try:
        with open("marcacoes.txt", "r") as arquivo:
            estrelas = []
            for linha in arquivo:
                x, y, nome = linha.strip().split(',')
                estrelas.append(((int(x), int(y)), nome))
        print("Marcações carregadas com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar marcações: {e}")

def excluir_marcacoes():
    global estrelas
    estrelas = []
    print("Todas as marcações foram excluídas.")

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos
            nome = pedir_nome_estrela()
            if nome == "desconhecido":
                nome += f" ({pos[0]}, {pos[1]})"
            estrelas.append((pos, nome))
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F10:
                salvar_marcacoes()
            elif evento.key == pygame.K_F11:
                carregar_marcacoes()
            elif evento.key == pygame.K_F12:
                excluir_marcacoes()

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

    fonte = pygame.font.SysFont("comicsans",14)
    texto = fonte.render("Pressione F10 para Salvar os pontos", True, branco)
    tela.blit(texto, (10, 10))
    texto = fonte.render("Pressione F11 para Carregar os pontos", True, branco)
    tela.blit(texto, (10, 40))
    texto = fonte.render("Pressione F12 para Deletar os pontos", True, branco)
    tela.blit(texto, (10, 70))

    # Atualizar a tela
    pygame.display.update()
    clock.tick(60)

pygame.quit()

